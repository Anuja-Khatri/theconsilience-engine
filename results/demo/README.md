# Receipts: results of the cross-theory demo

This folder pins the results of the public consciousness-science demo
(<https://consilience-demo.netlify.app>) at a commit of a public repository, so that
anything published from them can link to an exact, unchanging file and carry its hash.

## What is here

| File | What it is |
|---|---|
| `files/run_manifest.json` | The demo's record of its last regeneration: corpus hash `ccc6db4ceb29`, generated 2026-08-13 10:59 UTC, holdout check PASS, the two theory pairs it covers. Its "26 passed" refers to the demo pipeline's own test suite, which is not in this repository. |
| `files/iitxgnwt_judge.json` | IIT against GNWT: both theories' claim cards (the claims as typed fields with a one-sentence statement), the correspondences the demo found (every one marked `draft`), and the disagreements (forks), with the shared observables the demo names for each. |
| `files/iitxgnwt_decidability.json` | IIT against GNWT: for each disagreement, whether the demo's check rules it decidable with current instruments, and on which shared observable. |
| `files/iitxorch-or_judge.json` | IIT against Orch-OR, same layout. |
| `files/iitxorch-or_decidability.json` | IIT against Orch-OR, same layout. |
| `MANIFEST.json` | The SHA-256 of each file here, and of the file the demo serves. |
| `make_receipts.py` | Rebuilds `files/` from the files the demo serves, and checks every hash. |

Check the hashes yourself:

```bash
python3 -c "import hashlib,json;m=json.load(open('results/demo/MANIFEST.json'));[print(hashlib.sha256(open(f['path'],'rb').read()).hexdigest()==f['sha256'],f['path']) for f in m['files']]"
```

## Where the files come from

On 2026-11-17 the five files were downloaded from `https://consilience-demo.netlify.app/results/`.
They are byte-for-byte the files the demo's pipeline wrote into its deploy folder in the
project's own (private) repository. That repository is not public, so this is stated
rather than linkable; this folder is the public copy.

How the demo made them: the theory papers were split into passages; a language model
drafted typed claim cards from the passages; a person reviewed each card (every card in
these files is `"status": "approved"`); then deterministic code built the claim graphs, compared the two theories
field by field (axis, polarity, value, stated conditions) and ruled on decidability.
The comparison code is not in this repository (see below).

Two things were removed, and nothing else was changed:

1. the `extractor_model` field on each claim card (it names the AI model that drafted
   the card; we leave model identifiers out of published records);
2. the `text` of each provenance excerpt (`prov`), keeping the passage id and the page
   locator. The excerpts are passages of the theory papers, and we do not republish
   them here; the demo still shows them.

The files are rewritten with two-space indentation so that single records can be linked
by line number. `make_receipts.py` does exactly this, and checks the result against the
hashes in `MANIFEST.json`, so anyone can confirm that these files are the demo's results
with those two removals.

## How to read the claim statements

Each claim card has a `statement`. **It is a paraphrase of the theory paper, drafted by a
language model and reviewed by a person. It is not a quotation.** Each card lists the
passages it rests on (`passage_ids`) and, under `prov`, up to two of them with a page
locator (`"p.4"`). A page locator is the page number of the PDF the pipeline read, which
can differ from the journal's printed page numbers.

The passage ids name the source document:

| Prefix | Document |
|---|---|
| `iit_3_0` | Oizumi, Albantakis, Tononi (2014), PLOS Computational Biology, doi:10.1371/journal.pcbi.1003588 |
| `iit_4_0` | Albantakis et al. (2023), PLOS Computational Biology, doi:10.1371/journal.pcbi.1011465 |
| `iit_nrn_2016` | Tononi, Boly, Massimini, Koch (2016), Nature Reviews Neuroscience, doi:10.1038/nrn.2016.44 |
| `gnwt_neuron_2011` | Dehaene, Changeux (2011), Neuron, doi:10.1016/j.neuron.2011.03.018 |
| `gnwt_neuron_2020` | Mashour, Roelfsema, Changeux, Dehaene (2020), Neuron, doi:10.1016/j.neuron.2020.01.026 |
| `gnwt_science_2017` | Dehaene, Lau, Kouider, "What is consciousness, and could machines have it?" (Science 2017, doi:10.1126/science.aan8871); the pipeline read the reprint in *Robotics, AI, and Humanity* (Springer 2021, doi:10.1007/978-3-030-54173-6_4), so its page locators refer to that reprint |
| `orchor_2014` | Hameroff, Penrose (2014), "Consciousness in the universe", Physics of Life Reviews, doi:10.1016/j.plrev.2013.08.002 |
| `orchor_anesthesia` | Hameroff (2022), Frontiers in Molecular Neuroscience, doi:10.3389/fnmol.2022.869935 |

## What the results do and do not say

- A disagreement ("fork") is two claims on the same axis with different values. The
  decidability files say whether the demo's check finds a shared observable that both
  claims commit to with instruments that exist today. That is a statement about the
  claim cards, not a verdict on either theory.
- Every correspondence in these files is marked `draft`. None is a verdict, and none
  has been published as one.

## The COGITATE blind test

The demo was also checked blind against the preregistered predictions of the COGITATE
adversarial collaboration (IIT against GNWT). The result: **2 of 3 after a disclosed
re-review, originally 1 of 3, p = 0.075** against a 1,000-key permutation null. That is
suggestive only. Method and full numbers are in the flagship paper,
[10.5281/zenodo.23672883](https://zenodo.org/records/23672883).

The demo's own comparison file for this test (`iitxgnwt_vs_cogitate.json`) is not copied
here: its per-prediction labels are working labels that do not state the result in the
form above, and the paper is the account of record. No nanopublication is made for the
COGITATE test, because none of our templates fits a recovery score.

## Left out on purpose

- **The comparison and extraction code.** It lives in the private repository with the
  extraction prompts and other working files. It has not been reviewed for publication,
  so it is not copied here. The reference code in `judge/` in this repository is not
  what produced these results.
- **The other files the demo serves** (other theory pairs, the pairing matrix, the
  evidence summary, the INTREPID comparison). The run manifest covers only the two pairs
  above, and nothing published from this folder needs the others.

## Licence

The files in `files/` are results data. The claim statements paraphrase published
papers, which remain their authors' work; cite the papers above when you use them.
