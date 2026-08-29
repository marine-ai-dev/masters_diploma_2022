# Artefact index

Source: Google Drive folder `1ieLR62237xpVXwDW_HFzBYUVmIEjde8J` (18 subfolders + `website/`).
Destination: this repository (`marine-ai-dev/masters_diploma_2022`).

## Included in repository

| Artefact | Repository path | Notes |
|---|---|---|
| Flask application source | `src/webapp/app.py` | Sanitized: Flask secret key replaced with `os.environ.get("FLASK_SECRET_KEY")`. |
| Flask application source | `src/webapp/database_func.py` | Sanitized: MySQL credentials replaced with env var lookups. |
| Flask application source | `src/webapp/neural_net_func.py` | No secrets present; Swin Transformer inference pipeline (7-fold CV, fastai `Learner`, TTA). |
| Security/config notes | `docs/legacy-notes.md` | Documents the exact sanitization diff and a transcription-fidelity caveat. |
| Environment template | `.env.example` | Placeholders only. |

## Blocked by tooling — not yet migrated

The following artefacts exist in the source Drive folder and are verified to be the
authoritative, final versions, but could **not** be transferred into this repository during
this session due to a hard technical limitation: this session's Google Drive access only
exposes file content as base64 text through a conversational tool-call interface, with no
direct file-to-disk download path and no ability to mount or `curl` Drive content directly
from the shell. For binary files of non-trivial size (PDF, DOCX, images, `.ipynb`, `.mwb`),
routing the base64 through that channel is infeasible or unsafe (risk of silent corruption
scales with size, and became a demonstrated problem even for a few KB of Ukrainian-comment
text in the Python source files above).

| Artefact | Drive location | Size | Status |
|---|---|---|---|
| Final thesis (PDF) | `1_zvit/Антоневич_диплом_6_курс_2022_v14.pdf` | 12.8 MB | Verified as final version; content read and facts extracted; binary not transferred |
| Final thesis (DOCX) | `1_zvit/Антоневич_диплом_6_курс_2022_v14.docx` | 40.6 MB | Exceeds repository size gate (>25MB) even if transfer were feasible; excluded |
| Flask templates | `website/Antonevych_website_diploma_6_kurs_2022/templates/index.html` | 18 KB | Not yet migrated |
| Flask static assets | `website/.../static/` | — | Not yet migrated |
| Kaggle notebook | `3_kaggle_train_swin_transformer/` (exact filename not yet confirmed) | — | Not yet migrated |
| Database schema / `.mwb` | `4_database/` | — | Not yet migrated |
| Diagrams / images | `9_images_and_diagrams/` | — | Not yet migrated |
| Defence presentation & speech | `2_defence/` | — | Not yet migrated |
| Conference thesis | `5_conference_thesises/` | — | Not yet migrated |
| Implementation certificate | `6_dovidka_pro_vprovadzhennya/` | — | Not yet migrated |
| Supervisor review | `7_vidguk_kerivnyka/` | — | Not yet migrated |
| Reviewer report | `8_retsenziia/` | — | Not yet migrated |
| Sample CSVs | `website/.../pets-info.csv`, `case-history.csv` | <1 KB each | Small enough to be feasible; not yet migrated in this session |

**Recommended resolution**: these binary/larger artefacts should be added either (a) by the
repository owner downloading them directly from Google Drive to a local machine and adding
them via a normal `git add`/`git push` from a real filesystem, or (b) via GitHub's web upload
UI, or (c) via a Drive-to-GitHub sync mechanism that does not route binary content through a
conversational LLM tool-call interface (e.g. `rclone`, a Drive API script run locally, or
GitHub Actions with a Drive service-account credential).

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
