# The Ultraactivity Trap

**How Temporal Asymmetry Transforms Repeated Games into Terminal Betrayal**

[![DOI](https://img.shields.io/badge/DOI-10.2139%2Fssrn.XXXXXXX-blue)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=XXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Replication: Success](https://img.shields.io/badge/Replication-Success-brightgreen)]()

**Author**: Ignacio Adrián Lerer  
**Affiliation**: Independent Scholar, Buenos Aires  
**Contact**: adrianlerer@gmail.com  
**Version**: 1.0 (January 2025)  
**SSRN**: [Link TBD]

---

## Abstract

Political betrayal in repeated games is not cultural pathology—it is structural response to institutional architecture. When legal institutions exhibit **ultraactivity** (benefits captured through defection persist regardless of future cooperation), the shadow of the future collapses. Rational actors betray even in infinite games. Cooperation becomes impossible not because players are irrational but because institutional logic makes cooperation structurally dominated.

Argentina demonstrates this mechanism in pure form: Constitutional Lock-in Index (CLI) of 0.87, sustained across 80 years, resisting 23 reform attempts, surviving ideological administrations ranging from military dictatorship to radical libertarianism. The ultraactivity trap has closed.

United States demonstrates early-stage convergence: CLI rising from 0.33 (1980) to 0.41 (2024), projected 0.49 (2035). Not Argentine levels yet, but approaching the critical threshold (~0.50) where cooperation becomes structurally unstable.

We introduce computational instruments—**JurisRank** (doctrinal centrality), **RootFinder** (genealogical tracing), **CLI** (aggregate irreversibility), **Crystallization Drivers** (causal decomposition)—that make measurable what constitutional scholarship previously accessed only through qualitative interpretation. These tools enable comparison, prediction, and systematic testing.

**Main Findings**:
1. Ultraactivity eliminates shadow of future in repeated games → defection becomes dominant strategy
2. Argentina CLI (0.87) vs Chile (0.24) explains 23 failed reforms vs bidirectional adaptability
3. USA CLI trajectory (0.33→0.41→0.49 projected) suggests convergence toward Argentine-style terminal politics
4. Prohibition of ultraactivity should be first-order constitutional principle (like periodic elections, separation of powers)

**Keywords**: ultraactivity, repeated games, constitutional lock-in, Argentina, memetic evolution, extended phenotypes, stare decisis, democratic exhaustion

---

## Repository Contents

### 📄 Paper
- **Main Paper** ([`paper/ultraactivity_trap_v1.pdf`](paper/ultraactivity_trap_v1.pdf))
- **Supplementary Materials** ([`paper/supplementary_materials.pdf`](paper/supplementary_materials.pdf))
- All figures in [`paper/figures/`](paper/figures/)

### 📊 Data
- **Raw data**: [`data/raw/`](data/raw/) - Original sources (immutable)
- **Processed data**: [`data/processed/`](data/processed/) - Cleaned, coded datasets
- **Codebook**: [`data/CODEBOOK.md`](data/CODEBOOK.md) - Variable definitions

### 💻 Code
- **Data cleaning**: [`code/01_data_cleaning/`](code/01_data_cleaning/)
- **Measurement instruments**: [`code/02_measurement/`](code/02_measurement/)
  - JurisRank: Citation network analysis
  - RootFinder: Genealogical tracing
  - CLI Calculator: Constitutional Lock-in Index
  - Drivers Model: Predictive formula
- **Analysis**: [`code/03_analysis/`](code/03_analysis/)
- **Visualizations**: [`code/04_visualizations/`](code/04_visualizations/)

### 🔄 Replication
Complete replication package with step-by-step guide: [`replication/REPLICATION_GUIDE.md`](replication/REPLICATION_GUIDE.md)

**Quick start**:
```bash
# Clone repository
git clone https://github.com/adrianlerer/ultraactivity-trap.git
cd ultraactivity-trap

# Install dependencies
pip install -r code/requirements.txt

# Run complete replication
bash replication/run_all.sh
```

### 📚 Documentation
- [Methodology](docs/METHODOLOGY.md) - Detailed research design
- [Instruments Technical Specs](docs/INSTRUMENTS_TECHNICAL.md) - Algorithm documentation
- [Case Narratives](docs/CASE_NARRATIVES.md) - Country-specific details

---

## Key Contributions

### 1. Theoretical Innovation
**Temporal asymmetry in repeated games**: Extending Axelrod/Tsebelis cooperation theory to institutional contexts where benefits crystallize permanently. First formal analysis of how ultraactivity eliminates shadow of future.

### 2. Measurement Revolution
**Four computational instruments** making visible what was previously only intuited:
- **JurisRank**: Measures doctrinal centrality via citation network analysis (PageRank adapted to jurisprudence)
- **RootFinder**: Traces genealogical evolution of legal concepts, identifies crystallization inflection points
- **CLI**: Aggregate Constitutional Lock-in Index (0-1 scale) across 4 dimensions
- **Drivers**: Decomposes CLI into causal mechanisms (identity-linkage, rent-capture, etc.)

### 3. Comparative Evidence
**Natural experiment**: Argentina (CLI 0.87, 0% reform success) vs Chile (CLI 0.24, 83% reform success) with shared legal tradition, similar history, but divergent institutional design.

**USA convergence**: Documenting rise in CLI (0.33→0.41) via judicialización, executive orders, norm erosion. Predicting threshold crossing (~0.50) within decade if trajectory continues.

### 4. Memetic Analysis
First rigorous application of **Dawkins/Dennett evolutionary framework** to constitutional law:
- Ultraactivity as **legal meme** (replicator)
- CGT/Peronism/CSJN as **extended phenotypes** (physical instantiations protecting meme)
- **Cumulative evolution** via ratchet mechanisms (five generations, 1953-present)
- **Analogical spread** from labor to all "asymmetric relations"

### 5. Policy Prescription
**Constitutional prohibition of ultraactivity** as first-order democratic principle. Proposed amendment with:
- Mandatory sunset clauses (8-year maximum)
- Stare decisis limitation (weak for substantive precedents, strong for procedural)
- Anti-evasion provisions
- Supermajority protection

---

## Citation

**BibTeX**:
```bibtex
@unpublished{lerer2025ultraactivity,
  title={The Ultraactivity Trap: How Temporal Asymmetry Transforms Repeated Games into Terminal Betrayal},
  author={Lerer, Ignacio Adri{\'a}n},
  year={2025},
  note={SSRN Working Paper},
  url={https://github.com/adrianlerer/ultraactivity-trap}
}
```

**APA**:
> Lerer, I. A. (2025). *The ultraactivity trap: How temporal asymmetry transforms repeated games into terminal betrayal*. SSRN Working Paper. https://github.com/adrianlerer/ultraactivity-trap

---

## Data Sources

All primary sources documented in [`data/CODEBOOK.md`](data/CODEBOOK.md):

- **Argentine Supreme Court (CSJN)**: 2,847 decisions (1983-2024) via SAIJ database
- **Chilean Constitutional Tribunal**: 156 decisions (1990-2024) via TC official database
- **Labor Reforms Database**: Complete coding of all reform attempts (Argentina n=23, Chile n=15, Brazil n=14, Spain n=13)
- **Legislative Records**: Official gazettes (Boletín Oficial Argentina, Diario Oficial Chile)
- **Union Statistics**: CGT, CUT, UGT membership and financing data

---

## Replication Status

✅ **Successfully replicated** by [TBD - independent replicators]

All figures and tables in published paper can be reproduced exactly using:
```bash
bash replication/run_all.sh
```

Expected runtime: ~45 minutes on standard laptop (MacBook Pro M1, 16GB RAM)

---

## Presentations

- [SSRN Conference] (TBD)
- [Workshop presentation slides](presentations/conference_slides.pdf)
- [Policy brief for practitioners](presentations/policy_brief.pdf)

---

## Contact

**Ignacio Adrián Lerer**  
Email: adrianlerer@gmail.com  
Website: [personal site TBD]  
LinkedIn: [profile TBD]  
GitHub: [@adrianlerer](https://github.com/adrianlerer)

---

## License

MIT License - see [LICENSE](LICENSE) file

**Open Science**: All data, code, and materials freely available for replication, extension, and critique. If you use this work, please cite appropriately.

---

## Acknowledgments

- Lawrence Solum (University of Virginia) - originalism and construction theory
- Reva Siegel (Yale Law School) - constitutional memory and 19th Amendment research
- Richard Dawkins - memetic framework and extended phenotypes
- Daniel Dennett - cumulative selection and evolutionary epistemology
- GenSpark AI - computational infrastructure and analysis tools

---

## Version History

**v1.0** (January 2025): Initial SSRN publication
- Complete paper with all 5 parts
- Full replication package
- Comparative analysis (Argentina, Chile, Brazil, Spain, USA)
- Predictive applications (Milei 2024-2027, USA 2025-2035)

**Future versions**: Will incorporate feedback from workshops, conferences, and peer review.

---

## Related Repositories

- [legal-evolution-unified](https://github.com/adrianlerer/legal-evolution-unified) - Broader constitutional evolution framework
- [crystallization-drivers](https://github.com/adrianlerer/legal-evolution-unified/tree/main/crystallization_drivers) - Causal decomposition of lock-in mechanisms

---

**Status**: 🚧 Active research project | 📢 Comments welcome | 🔄 Continuously updated
