# Legacy notes

This repository archives a 2022 Master's diploma project. The source code is preserved as
faithfully as possible; the only intentional deviations from the historical originals are
described below.

## Security sanitization (`src/webapp/`)

- **`app.py`**: the hardcoded Flask `secret_key` string literal was replaced with
  `os.environ.get("FLASK_SECRET_KEY")`. The historical secret value is not present anywhere
  in this repository or its Git history.
- **`database_func.py`**: the hardcoded MySQL host/database/user/password literals were
  replaced with `os.environ.get(...)` lookups (`MYSQL_HOST`, `MYSQL_DATABASE`, `MYSQL_USER`,
  `MYSQL_PASSWORD`), and an `import os` line was added (not present in the original) to
  support this. The historical password value is not present anywhere in this repository or
  its Git history.
- No other algorithmic behaviour was intentionally changed in either file.

## Transcription fidelity note

The original source files were retrieved from Google Drive as base64-encoded API responses.
During archival, a small number of non-executable Ukrainian-language inline comments in
`app.py` and `neural_net_func.py` could not be verified character-for-character against the
original with full confidence, due to limitations in how long encoded payloads round-trip
through the migration tooling used for this archival. Rather than risk silently publishing a
fabricated comment as if it were the historical original, those specific comment lines were
replaced with the marker:

```
# [історичний коментар не вдалось перевірити символ-в-символ під час архівації]
```

This affects **only comment text** (no executable code, string literals, route definitions,
SQL, or function signatures) in a handful of lines. All executable logic was verified to
compile correctly (`python3 -m py_compile`) and was cross-checked structurally across
multiple independent retrievals from the source.

## Old thesis drafts

Only the final thesis version (`v14`) is included in this repository, as both the PDF and
the source `.docx`. Versions v1–v13 remain available in the original Google Drive source
folder and are not duplicated here to avoid repository bloat; see `docs/artefact-index.md`.
