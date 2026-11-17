"""The demo receipt set in results/demo/ matches its manifest and leaves out what it says
it leaves out. Runs offline."""

import hashlib
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "results" / "demo"
MANIFEST = json.loads((DEMO / "MANIFEST.json").read_text(encoding="utf-8"))
FILES = [ROOT / f["path"] for f in MANIFEST["files"]]


def test_manifest_lists_every_file_and_nothing_else():
    assert sorted(p.name for p in (DEMO / "files").iterdir()) == sorted(p.name for p in FILES)


@pytest.mark.parametrize("entry", MANIFEST["files"], ids=lambda e: Path(e["path"]).name)
def test_file_hash_matches_manifest(entry):
    data = (ROOT / entry["path"]).read_bytes()
    assert hashlib.sha256(data).hexdigest() == entry["sha256"]
    assert entry["served_at"].startswith("https://consilience-demo.netlify.app/results/")


@pytest.mark.parametrize("path", FILES, ids=lambda p: p.name)
def test_no_model_identifier_and_no_excerpt_text(path):
    text = path.read_text(encoding="utf-8")
    assert "extractor_model" not in text
    lowered = text.lower()
    for marker in ("claude", "gpt-", "sonnet", "haiku", "opus", "gemini"):
        assert marker not in lowered, marker

    def walk(o):
        if isinstance(o, dict):
            if "prov" in o:
                for p in o["prov"]:
                    assert set(p) == {"id", "locator"}, p
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(json.loads(text))


def test_transform_reproduces_layout():
    """Re-rendering each file with the script's own writer gives the same bytes."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("make_receipts", DEMO / "make_receipts.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for path in FILES:
        data = path.read_bytes()
        assert mod.render(mod.strip(json.loads(data))) == data
        assert mod.FILES[path.name][1] == hashlib.sha256(data).hexdigest()


def test_every_claim_card_was_reviewed_and_correspondences_are_drafts():
    for name in ("iitxgnwt_judge.json", "iitxorch-or_judge.json"):
        j = json.loads((DEMO / "files" / name).read_text(encoding="utf-8"))
        for side in ("left", "right"):
            assert all(n["status"] == "approved" for n in j[side]["nodes"])
        assert all(c["status"] == "draft" for c in j["correspondences"])
