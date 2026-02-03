"""The planted dependency pins must be genuinely importable.

A pin that nothing imports produces a manifest-versus-source disagreement that
looks like a tool defect and is not. This test is the guard against the
TypeScript corpus's structurally-zero-span trap reappearing here.

It also guards the reverse: paramiko 2.4.1 imports `six` WITHOUT declaring it.
On the Python 3.6 family that never showed, because cryptography 2.3 declared
six and supplied it by accident. cryptography 42.0.0 dropped six, so on 3.7 a
runtime-only install raises ModuleNotFoundError. `six` is therefore pinned
explicitly in the support section of requirements-runtime.txt, and imported
here so the guard cannot rot.
"""
import pytest

pytest.importorskip("requests")
pytest.importorskip("jinja2")
pytest.importorskip("urllib3")
pytest.importorskip("cryptography")
pytest.importorskip("paramiko")
pytest.importorskip("six")   # paramiko 2.4.1 imports six without declaring it

from orderlab.platform.integrations import (           # noqa: E402
    dependency_versions,
    render_invoice,
)

EXPECTED = {
    "requests": "2.31.0",
    "urllib3": "2.0.6",
    "jinja2": "3.1.3",
    "cryptography": "42.0.0",
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
