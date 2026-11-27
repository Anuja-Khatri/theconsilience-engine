"""Rebuild the receipt set in results/demo/files/ from the files the public demo serves.

    mkdir -p /tmp/demo && cd /tmp/demo
    for f in run_manifest.json iitxgnwt_judge.json iitxgnwt_decidability.json \
             iitxorch-or_judge.json iitxorch-or_decidability.json; do
      curl -sS -O https://consilience-demo.netlify.app/results/$f
    done
    python results/demo/make_receipts.py /tmp/demo

The script checks each downloaded file against the SHA-256 recorded below (the bytes the
demo served on 2026-11-17), applies two removals and nothing else, and writes the result
with a fixed layout so that the output is byte-for-byte reproducible:

1. every "extractor_model" field is removed (it names the AI model that drafted the
   claim statements; we leave model identifiers out of published records);
2. the "text" of every provenance excerpt ("prov") is removed, keeping its passage id and
   page locator (the excerpts are passages of the theory papers; we do not republish
   them here).

It then writes MANIFEST.json and checks every output hash against the expected one.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "files"
DEMO = "https://consilience-demo.netlify.app/results/"
RETRIEVED = "2026-11-17"

# name: (SHA-256 of the bytes the demo serves, SHA-256 of the file written here)
FILES = {
    "run_manifest.json": (
        "078e53fbd4698d7c5f34210c45e41fc26157dd442154a9b6f27434b3004309f5", "090449d2faa6f1b9761352c546dfe33119c01e426a7f6831bffd4d19368ea7dc"),
    "iitxgnwt_judge.json": (
        "91f4bbec746ea145d69b9aa6e05752a4dd12547e622a277cdcdf1a573f3acfdf", "e4ad57fddd0781d98233afa852d015fb4fdb107004b0fc020c152a85134615c0"),
    "iitxgnwt_decidability.json": (
        "90c392fa2d70235d5e422feb9d80af3465c534666bb75386207ecec7fff46d6e", "feb08368788e466fc6cfeb7465f6e531291592cb827076854814652dcd903113"),
    "iitxorch-or_judge.json": (
        "63cdc761108c1619021ec844df80f5ede826972e0ac5599d568549a1026c988f", "91caa2c3ca5e943f886598ac972e2f834ba242adfb8cf0c842bb4cb667a0589a"),
    "iitxorch-or_decidability.json": (
        "16b5bacf53c359bc06b937bca46215eb4d58ca5379944562ac148746cdb4024c", "e7a75abb8abf941fa6e83e54cdd7b9fdd313bdf3fe81ee212bd77ca0f2728d2e"),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def strip(obj):
    """Remove extractor_model everywhere and the text of provenance excerpts."""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k == "extractor_model":
                continue
            if k == "prov" and isinstance(v, list):
                out[k] = [{kk: vv for kk, vv in p.items() if kk != "text"} for p in v]
                continue
            out[k] = strip(v)
        return out
    if isinstance(obj, list):
        return [strip(v) for v in obj]
    return obj


def render(obj) -> bytes:
    return (json.dumps(obj, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    src = Path(argv[1])
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "description": "Results of the public cross-theory demo, as receipts. See README.md.",
        "served_by": DEMO,
        "retrieved": RETRIEVED,
        "transform": "results/demo/make_receipts.py: remove every 'extractor_model' field and "
                     "the 'text' of every 'prov' excerpt; write json.dumps(indent=2, "
                     "ensure_ascii=False) plus a newline. Nothing else is changed.",
        "files": [],
    }
    bad = []
    for name, (want_served, want_out) in FILES.items():
        raw = (src / name).read_bytes()
        got_served = sha256(raw)
        if got_served != want_served:
            bad.append(f"{name}: the demo file hashes to {got_served}, expected {want_served}")
            continue
        out = render(strip(json.loads(raw)))
        (OUT / name).write_bytes(out)
        got_out = sha256(out)
        if got_out != want_out:
            bad.append(f"{name}: output hashes to {got_out}, expected {want_out}")
        manifest["files"].append({
            "path": f"results/demo/files/{name}",
            "sha256": got_out,
            "served_at": DEMO + name,
            "served_sha256": got_served,
        })
    (HERE / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    for b in bad:
        print("MISMATCH", b, file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
