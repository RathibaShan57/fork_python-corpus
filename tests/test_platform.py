"""The planted dependency pins must be genuinely importable.

A pin that nothing imports produces a manifest-versus-source disagreement that
looks like a tool defect and is not. This test is the guard against the
TypeScript corpus's structurally-zero-span trap reappearing here.
"""
import pytest

pytest.importorskip("requests")
pytest.importorskip("jinja2")
pytest.importorskip("urllib3")
pytest.importorskip("cryptography")
pytest.importorskip("paramiko")

from orderlab.platform.integrations import (           # noqa: E402
    dependency_versions,
    render_invoice,
)

EXPECTED = {
    "requests": "2.20.0",
    "urllib3": "1.24.1",
    "jinja2": "2.10",
    "cryptography": "2.3",
    "paramiko": "2.4.1",
}


def test_every_planted_pin_is_imported_and_reports_its_version():
    resolved = dependency_versions()
    assert sorted(resolved) == sorted(EXPECTED)


def test_resolved_versions_match_the_manifest_pins():
    resolved = dependency_versions()
    mismatched = {name: (resolved[name], want)
                  for name, want in EXPECTED.items()
                  if resolved[name] != want}
    assert not mismatched, "installed versions disagree with the pins: {0}".format(
        mismatched)


def test_invoice_template_renders():
    text = render_invoice("A-1", "US", 123.45, 2)
    assert "A-1" in text and "123.45" in text
