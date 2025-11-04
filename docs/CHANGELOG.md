# Changelog

All notable changes to the Ultraactivity Trap project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-01-15

### Added
- Initial public release
- Complete paper (5 parts)
- Full replication package
- JurisRank measurement instrument
- RootFinder genealogical tracer
- CLI calculator
- Crystallization drivers model
- Argentina reform database (n=23)
- Comparative analysis (5 countries)
- USA projections (2025-2035)
- Complete documentation
- Replication guide
- Data codebook

### Documentation
- README.md with project overview
- METHODOLOGY.md with detailed research design
- CODEBOOK.md with variable definitions
- REPLICATION_GUIDE.md with step-by-step instructions
- INSTRUMENTS_TECHNICAL.md with algorithm specifications

### Data
- argentina_reforms_coded.csv (23 reform attempts)
- cli_components.csv (165 country-years)
- jurisrank_scores.csv (450 doctrine-years)
- rootfinder_genealogies.csv (87 precedents)
- comparative_cases.csv (5 countries)

### Code
- Python scripts for data cleaning (3 files)
- Measurement instruments (4 files)
- Analysis scripts (3 files)
- Visualization scripts (2 files)
- Master replication script (run_all.sh)

### Validation
- All figures replicated successfully
- All tables reproduced exactly
- Statistical tests converge
- Expected runtime: ~45 minutes

---

## [Unreleased]

### Planned for v1.1
- [ ] Additional countries (Mexico, Colombia)
- [ ] Extended time series (1950-2024)
- [ ] Machine learning predictions
- [ ] Interactive dashboard
- [ ] Docker container for exact replication

### Planned for v2.0
- [ ] Expansion to other policy domains (tax, environmental)
- [ ] Cross-national panel analysis
- [ ] Agent-based modeling
- [ ] Fuzzy-set QCA
- [ ] Network visualization tools

---

## Version Numbering

- **MAJOR** version: Incompatible API changes, major theoretical revisions
- **MINOR** version: Backward-compatible functionality additions
- **PATCH** version: Backward-compatible bug fixes

---

## How to Contribute

See issues and pull requests at:
https://github.com/adrianlerer/ultraactivity-trap

---

**Maintained by**: Ignacio Adrián Lerer  
**Contact**: adrianlerer@gmail.com
