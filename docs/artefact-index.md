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
| Flask static CSS | `src/webapp/static/css/style.css` | `ab942736154223bdf3db38d60342059206474f212f5c06c502cea2383868b61d` | Retrieved via Drive API, decoded and byte-verified (exact size match) without manual retyping. |
| Flask static JS | `src/webapp/static/js/additional_scripts.js` | `519e7c01cbd76843e61acfeaa737ac43691571a3f1a2af156dc26c46511af692` | Same method; exact size match. |
| Flask static JS | `src/webapp/static/js/main.min.js` | `af32a924d56ac55b11e485739dd8106d197d1a2e4633534cdba6cf0184ee9806` | First attempt at this file had a 24-byte transcription error caught by comparing decoded size against Drive metadata; re-decoded via a file-based (non-retyped) path with matching size. |
| Implementation certificate | `academic/implementation-certificate/Антоневич_довідка_про_впровадження_диплом_6_курс_2022.pdf` | `64fb9257de9ec975ae21469774b633650ba949eb816cfb365d94ab8c2ede8b72` | From the Cherkasy City Society for the Protection of Animals "Друг". |
| Supervisor review | `academic/supervisor-review/Антоневич_відгук_керівника_диплом_6_курс_2022_v2.pdf` | `d152aba3378c9b2f11940e48532df2745d1815945f6bdbff00a88123e2099341` | Final v2. |
| Reviewer report | `academic/reviewer-report/Антоневич_рецензія_диплом_6_курс_2022_v3.docx` | `e7484e80bad915662882af736ad0ae192d7b1f0b63b05c45e8e128faaddee7d0` | Final v3; original filename had a duplicate-download `(2)` suffix, renamed for clarity. |
| Curated diagram | `assets/architecture/structure_diagram.png` | `30ff6e62f3b51f0eb75a0938e1fbd201e7c11dc64e9a3afdb88035c7aa97c69e` | Project structure diagram, original author's work. |
| Curated diagram | `assets/architecture/neural_network_diagram.png` | `17ff29b7f31870609b1014e4529b9a285bd5f2f1c33b43bd25c13fa462c67eca` | Neural network diagram. |
| Curated diagram | `assets/research/research_logical_structure.png` | `6102ff9773db9aebf646cd7a5d076169332ddde7504225eec7affd5f55c09878` | Research methodology / logical structure diagram. |
| Curated diagram | `assets/research/k_fold_diagram.png` | `775960aae575765f1bb970357019bdf4daeaf81a29d627307f7cd6073f3c8a7e` | Stratified K-fold cross-validation diagram. |
| Curated diagram | `assets/research/pattern_recognition_systems.png` | `4c73d98c2821234103ddefc5c140dde26365b6c162589f074545c646dd1d1238` | Pattern-recognition systems comparison diagram. |
| Curated diagram | `assets/ui/website_page_diagram.png` | `598dc96c82da7d3b6782c43a6cd1a3effda76edc27ba9ea628b5ec6e2ab4cc95` | One representative web-app page/interface diagram (1 of 6 available; the rest remain in the source Drive archive to avoid an unstructured image dump). |
| Security/config notes | `docs/legacy-notes.md` | — | Documents the exact sanitization diff and a transcription-fidelity caveat. |
| Environment template | `.env.example` | — | Placeholders only. |

**Transfer method note**: all binary artefacts above were retrieved via direct Google Drive
file download to the local filesystem (either through a live, user-authenticated browser
session, or downloaded directly by the repository owner) and moved into the repository with
`cp`/`unzip`/`shasum` — not by routing binary content through a conversational tool-call as
base64 text. SHA-256 hashes were verified identical between the Drive download and the
repository copy for every file listed with a hash above.

## Not migrated

| Artefact | Drive location | Size | Status |
|---|---|---|---|
| Final thesis (DOCX) | `1_zvit/Антоневич_диплом_6_курс_2022_v14.docx` | 40.6 MB | Exceeds repository size gate (>25MB); excluded regardless of transfer feasibility |
| Sample CSVs | `website/.../pets-info.csv`, `case-history.csv` | <1 KB each | Redundant with `database/sample_data/pets_data.csv`; not migrated |
| Remaining 5 of 6 website-page diagrams | `9_images_and_diagrams/Pawpularity_diploma_website_template-Page-{2..6}.drawio.png` | — | One representative page diagram is included (`assets/ui/website_page_diagram.png`); the rest remain in Drive to avoid an image dump |
| Screenshot-style images (`image_2022-04-23_*.png`) | `9_images_and_diagrams/` | — | Ambiguous/undocumented content; not curated in |

## Excluded intentionally

| Artefact | Reason |
|---|---|
| Thesis drafts v1–v13 | Superseded by final v14; remain in the Drive source archive |
| `.DS_Store`, `__pycache__`, `.idea`, `.ipynb_checkpoints` | Editor/OS metadata, not source |
| Multi-GB video recordings (`15_videozapys_roboty_web-dodatku`, `16_videozapys_roboty_bazy_danykh`) | Exceed any reasonable Git file-size policy; linked from `docs/demo.md` instead |
| Full PetFinder.my Pawpularity Kaggle dataset (`static/dataset/`) | Third-party dataset with its own licensing; not redistributed here |
| Trained model checkpoints (`static/models/`, `model_fold_0`…`model_fold_6`) | ~15 GB of binary weights; excluded per explicit repository-owner instruction, remain in the source Drive archive |
| `static/images/` (loader.gif/svg, hero/pricing/cta illustrations, logo.svg, facebook/instagram/kaggle brand logos) | Bundled third-party HTML template assets with unclear redistribution rights; several are official third-party brand logos |
| `database/schema/Antonevych_database_diploma_6_kurs.mwb.bak` | Redundant backup of the included `.mwb` |
| `database/diagrams/ERR_diagram_diploma_6_kurs_2.paint` | Proprietary format; PNG exports already included |
| `Антоневич_відгук_керівника_диплом_6_курс_2022` (JPEG scan) | Redundant with the included PDF of the same document |
| `2_defence/pptx_templates/` | Third-party PowerPoint design template, not project content |

## Preserved externally

All artefacts listed as "not yet migrated" above remain available at their original Google
Drive locations under the source folder `1ieLR62237xpVXwDW_HFzBYUVmIEjde8J`, which the
repository owner retains access to.
