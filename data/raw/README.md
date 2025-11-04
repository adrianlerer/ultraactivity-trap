# Raw Data

This directory contains original, unmodified data files from primary sources.

## Files (to be added)

- `argentina_reforms_raw.csv` - Raw reform attempts from legislative archives
- `csjn_decisions_raw.csv` - CSJN decisions from SAIJ database
- `chile_reforms_raw.csv` - Chilean reform attempts
- `comparative_cases_raw.csv` - Cross-country data compilation

## Data Collection

All raw data files are immutable. Processing scripts in `code/01_data_cleaning/` transform these into cleaned versions in `data/processed/`.

## Sources

See `../CODEBOOK.md` for detailed source documentation for each file.

**Note**: Large data files (>100MB) are stored via Git LFS. Clone with `git lfs pull` to download.
