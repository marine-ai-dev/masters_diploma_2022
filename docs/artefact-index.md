# Artefact index

Source: Google Drive folder `1ieLR62237xpVXwDW_HFzBYUVmIEjde8J` (18 subfolders + `website/`).
Destination: this repository (`marine-ai-dev/masters_diploma_2022`).

## Included in repository

| Artefact | Repository path | SHA-256 | Notes |
|---|---|---|---|
| Flask application source | `src/webapp/app.py` | — | Sanitized: Flask secret key replaced with `os.environ.get("FLASK_SECRET_KEY")`. |
| Flask application source | `src/webapp/database_func.py` | — | Sanitized: MySQL credentials replaced with env var lookups. |
| Flask application source | `src/webapp/neural_net_func.py` | — | No secrets present; Swin Transformer inference pipeline (7-fold CV, fastai `Learner`, TTA). |
| Flask template | `src/webapp/templates/index.html` | `488cc214884b9400a1e093a241e3bba0bde93b1af158e103302bbb6979cf7d1a` | Downloaded via direct browser file download; hash matches source file on Drive. |
| Final thesis (PDF) | `thesis/final/Антоневич_диплом_6_курс_2022_v14.pdf` | `02c54cf27bb01462f6b2fa1144cc0237d03735854008e1dfb6602be3c923d54d` | 12.8 MB, 161 pages. Downloaded via direct browser file download; hash matches source file on Drive byte-for-byte. |
| Kaggle training notebook | `notebooks/pawpularity_swin_transformer.ipynb` | `45c3a661cfbe9be96c5972a215a4b5984c74e2a555aa04ec2f21ab60271fe33f` | Source: `fork-of-my-fork-of-pawpularity-swin-transformer.ipynb`. Valid JSON, no secrets in outputs. Hash matches source file on Drive byte-for-byte. |
| Defence presentation | `defence/presentation/Антоневич_презентація_диплом_6_курс_2022_v3.pptx` | `09c97e45fca558fcb60ea3ddc75974095ea47a7b79aef275346fe9a1bb108bc9` | 28.6 MB, final v3. Downloaded directly by the repository owner from Google Drive to the local machine. |
| Defence speech | `defence/speech/Антоневич_текст_доповіді_диплом_6_курс_2022.pdf` | `7951f5b643d9539afcd8c2460883d57a3482430f08187ff8e59d0dbe2397f778` | 4 pages. Downloaded via direct browser file download; hash verified against source. |
| Conference thesis | `publications/conference/Антоневич_тези_диплом_6_курс_2022.pdf` | `3b09e5df5dce653db0303a61c9e9026d51766f09ee4ed3271784ce40bd54dcd0` | 7 pages, IT&I 2021 (Satellite) conference thesis. |
| Database schema | `database/schema/Antonevych_database_diploma_6_kurs.mwb` | `eee3ebe80b603e7b8a4029b089172fe7ae4f905649eaa74069d2074976fa1b75` | MySQL Workbench model. `.mwb.bak` backup file excluded as redundant. |
| Database ER diagrams | `database/diagrams/ERR_diagram_diploma_6_kurs.png`, `ERR_diagram_diploma_6_kurs_2.png` | `a8209a69d1bae13e6577982e95cf685ac12d0961ab75cdd2c65bc28c2cfc18a4`, `be561ffe62552f2c7272571e9ea55945daf018a047056ad6d3b7f6084acd100f` | Source `.paint` project file excluded (proprietary format, PNG exports are sufficient). |
| Database sample data | `database/sample_data/pets_data.csv` | `0a4afaf7468b814fd8ca9f54d5f2ff55fcd0b2a9bc45a7587d74fd8939435590` | Test/placeholder pet records only (Rosie Meow, Reks, Tom, …) — no real shelter data or credentials. |
| Security/config notes | `docs/legacy-notes.md` | — | Documents the exact sanitization diff and a transcription-fidelity caveat. |
| Environment template | `.env.example` | — | Placeholders only. |

**Transfer method note**: all binary artefacts above were retrieved via direct Google Drive
file download to the local filesystem (either through a live, user-authenticated browser
session, or downloaded directly by the repository owner) and moved into the repository with
`cp`/`unzip`/`shasum` — not by routing binary content through a conversational tool-call as
base64 text. SHA-256 hashes were verified identical between the Drive download and the
repository copy for every file listed with a hash above.

## Blocked by tooling — not yet migrated

| Artefact | Drive location | Size | Status |
|---|---|---|---|
| Final thesis (DOCX) | `1_zvit/Антоневич_диплом_6_курс_2022_v14.docx` | 40.6 MB | Exceeds repository size gate (>25MB); excluded regardless of transfer feasibility |
| Flask static assets | `website/Antonevych_website_diploma_6_kurs_2022/static/` | — | Not yet migrated |
| Diagrams / images | `9_images_and_diagrams/` | — | Not yet migrated |
| Implementation certificate | `6_dovidka_pro_vprovadzhennya/` | — | Not yet migrated |
| Supervisor review | `7_vidguk_kerivnyka/` | — | Not yet migrated |
| Reviewer report | `8_retsenziia/` | — | Not yet migrated |
| Sample CSVs | `website/.../pets-info.csv`, `case-history.csv` | <1 KB each | Small enough to be feasible; not yet migrated in this session |

## Excluded intentionally

| Artefact | Reason |
|---|---|
| Thesis drafts v1–v13 | Superseded by final v14; remain in the Drive source archive |
| `.DS_Store`, `__pycache__`, `.idea`, `.ipynb_checkpoints` | Editor/OS metadata, not source |
| Multi-GB video recordings (`15_videozapys_roboty_web-dodatku`, `16_videozapys_roboty_bazy_danykh`) | Exceed any reasonable Git file-size policy; should be linked from `docs/demo.md`, not committed |
| Full PetFinder.my Pawpularity Kaggle dataset | Third-party dataset with its own licensing; not redistributed here |

## Preserved externally

All artefacts listed as "not yet migrated" above remain available at their original Google
Drive locations under the source folder `1ieLR62237xpVXwDW_HFzBYUVmIEjde8J`, which the
repository owner retains access to.
