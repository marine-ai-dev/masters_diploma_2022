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
| Security/config notes | `docs/legacy-notes.md` | — | Documents the exact sanitization diff and a transcription-fidelity caveat. |
| Environment template | `.env.example` | — | Placeholders only. |

**Transfer method note**: `templates/index.html`, the thesis PDF, and the notebook were
retrieved via a live, user-authenticated browser session (direct Google Drive file download
to the local filesystem, then `cp`/`shasum` to move them into the repository) — not by
routing binary content through a conversational tool-call as base64 text. SHA-256 hashes were
verified identical between the Drive download and the repository copy for all three.

## Blocked by tooling — not yet migrated

The following artefacts exist in the source Drive folder and are verified to be the
authoritative, final versions, but have not yet been transferred into this repository. The
browser-based direct-download method above worked reliably for the three files listed above,
but became unreliable (downloads silently not completing) for subsequent files in the same
session — this appears to be transient flakiness in the download bridge rather than a fixed
limitation, and should be retried.

| Artefact | Drive location | Size | Status |
|---|---|---|---|
| Final thesis (DOCX) | `1_zvit/Антоневич_диплом_6_курс_2022_v14.docx` | 40.6 MB | Exceeds repository size gate (>25MB); excluded regardless of transfer feasibility |
| Flask static assets | `website/Antonevych_website_diploma_6_kurs_2022/static/` | — | Not yet migrated |
| Defence presentation | `2_defence/Антоневич_презентація_диплом_6_курс_2022_v3.pptx` | 28.6 MB | Download attempted but did not complete reliably in this session; retry needed |
| Defence speech | `2_defence/Антоневич_текст_доповіді_диплом_6_курс_2022.pdf` | 226 KB | Download attempted but did not complete reliably in this session; retry needed |
| Database schema / `.mwb` | `4_database/` | — | Not yet migrated |
| Diagrams / images | `9_images_and_diagrams/` | — | Not yet migrated |
| Conference thesis | `5_conference_thesises/` | — | Not yet migrated |
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
