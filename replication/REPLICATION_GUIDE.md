# Appendix E: Replication Materials

**Status**: TO DEVELOP - Complete replication package documentation

---

## Overview

This appendix provides comprehensive replication instructions, enabling independent researchers to reproduce all analyses, figures, and tables in the paper.

---

## E.1 Quick Start

### E.1.1 System Requirements

**Minimum**:
- CPU: Dual-core 2.0 GHz
- RAM: 8 GB
- Storage: 5 GB free space
- OS: Linux, macOS, or Windows 10+

**Recommended**:
- CPU: Quad-core 3.0 GHz
- RAM: 16 GB
- Storage: 10 GB free space

**Runtime**: ~45 minutes on recommended hardware

---

### E.1.2 Software Dependencies

**Required**:
- Python 3.8+ (recommend 3.10)
- R 4.0+ (recommend 4.3)
- Git

**Installation**:
```bash
# Clone repository
git clone https://github.com/adrianlerer/ultraactivity-trap.git
cd ultraactivity-trap

# Install Python dependencies
pip install -r code/requirements.txt

# Install R dependencies
Rscript code/install_r_packages.R
```

---

### E.1.3 One-Command Replication

```bash
# Run complete pipeline
bash replication/run_all.sh
```

**Outputs**:
- All figures → `paper/figures/`
- All tables → `replication/tables/`
- Validation report → `replication/validation_report.pdf`
- Logs → `logs/`

---

## E.2 Step-by-Step Manual Replication

For users who want to understand each step or troubleshoot issues.

### Step 1: Data Cleaning

**Purpose**: Transform raw data into analysis-ready formats

**Scripts**:
```bash
cd code/01_data_cleaning

# Clean Argentina reform data
python clean_argentina_reforms.py
# Input:  data/raw/argentina_reforms_raw.csv
# Output: data/processed/argentina_reforms_coded.csv

# Clean CSJN judicial decisions
python clean_csjn_decisions.py
# Input:  data/raw/csjn_decisions_raw.json
# Output: data/processed/csjn_citation_network.graphml

# Clean Chile data
python clean_chile_reforms.py
# Input:  data/raw/chile_reforms_raw.csv
# Output: data/processed/chile_reforms_coded.csv

# Clean comparative cases
python clean_comparative_cases.py
# Input:  data/raw/comparative_raw.csv
# Output: data/processed/comparative_cases.csv
```

**Expected runtime**: 5-8 minutes

---

### Step 2: Measurement Instruments

**Purpose**: Calculate JurisRank, CLI, genealogical traces

**Scripts**:
```bash
cd code/02_measurement

# Calculate JurisRank scores
python jurisrank.py
# Input:  data/processed/csjn_citation_network.graphml
# Output: data/processed/jurisrank_scores.csv

# Calculate CLI components
python cli_calculator.py
# Input:  data/processed/argentina_reforms_coded.csv
#         data/processed/chile_reforms_coded.csv
# Output: data/processed/cli_components.csv

# Trace genealogies (RootFinder)
python rootfinder.py
# Input:  data/processed/csjn_citation_network.graphml
# Output: data/processed/rootfinder_genealogies.csv

# Crystallization drivers
python drivers_model.py
# Input:  data/processed/cli_components.csv
# Output: data/processed/drivers_predictions.csv
```

**Expected runtime**: 15-20 minutes (JurisRank is computationally intensive)

---

### Step 3: Statistical Analysis

**Purpose**: Run regressions, comparative tests, predictions

**Scripts**:
```bash
cd code/03_analysis

# Main comparative analysis (Argentina vs Chile)
Rscript comparative_analysis.R
# Input:  data/processed/argentina_reforms_coded.csv
#         data/processed/chile_reforms_coded.csv
#         data/processed/cli_components.csv
# Output: replication/tables/table1_reform_success.tex
#         replication/tables/table2_cli_comparison.tex

# Temporal dynamics analysis
Rscript temporal_dynamics.R
# Input:  data/processed/rootfinder_genealogies.csv
# Output: replication/tables/table3_genealogy_stats.tex

# Predictive model (USA projections, Milei scenarios)
python predictions.py
# Input:  data/processed/cli_components.csv
#         data/processed/drivers_predictions.csv
# Output: replication/tables/table4_predictions.tex
#         data/processed/usa_cli_projections.csv
```

**Expected runtime**: 10-12 minutes

---

### Step 4: Visualization

**Purpose**: Generate all figures

**Scripts**:
```bash
cd code/04_visualizations

# Main figures
Rscript create_figures.R
# Generates:
#   Figure 1: Argentina reform attempts timeline (1991-2025)
#   Figure 2: CLI comparison (5 countries)
#   Figure 3: JurisRank network visualization (Article 14bis centrality)
#   Figure 4: USA CLI trajectory (1980-2024, projected 2035)
#   Figure 5: Milei reform survival probability over time

# Tables (formatted for LaTeX)
python create_tables.py
# Formats all tables with proper LaTeX styling
```

**Expected runtime**: 5-8 minutes

---

### Step 5: Validation Report

**Purpose**: Generate comprehensive validation document comparing outputs to expected results

**Script**:
```bash
cd replication

python generate_report.py
# Compares:
#   - Figure checksums
#   - Table content
#   - Key statistics
#   - CLI scores
# Output: replication/validation_report.pdf
```

**Expected runtime**: 2-3 minutes

---

## E.3 Data Files Reference

### E.3.1 Raw Data (Input)

| File | Description | Source | Size | Availability |
|------|-------------|--------|------|--------------|
| `argentina_reforms_raw.csv` | Reform attempts 1991-2025 | Legislative records, academic coding | 45 KB | Public (repo) |
| `csjn_decisions_raw.json` | CSJN decisions 1983-2024 | SAIJ database | 120 MB | Public (SAIJ) |
| `chile_reforms_raw.csv` | Chilean reforms 1990-2025 | Biblioteca del Congreso | 28 KB | Public (repo) |
| `comparative_raw.csv` | Brazil, Spain, USA cases | Multiple sources | 18 KB | Public (repo) |

---

### E.3.2 Processed Data (Intermediate)

| File | Description | Generated by | Size |
|------|-------------|--------------|------|
| `argentina_reforms_coded.csv` | Clean Argentina data | `clean_argentina_reforms.py` | 38 KB |
| `csjn_citation_network.graphml` | Citation graph | `clean_csjn_decisions.py` | 85 MB |
| `cli_components.csv` | CLI scores by dimension | `cli_calculator.py` | 12 KB |
| `jurisrank_scores.csv` | Doctrinal centrality | `jurisrank.py` | 65 KB |
| `rootfinder_genealogies.csv` | Genealogical traces | `rootfinder.py` | 145 KB |

---

### E.3.3 Output Data (Results)

| File | Description | Generated by | Size |
|------|-------------|--------------|------|
| `table1_reform_success.tex` | Reform success rates | `comparative_analysis.R` | 8 KB |
| `table2_cli_comparison.tex` | CLI by country | `comparative_analysis.R` | 6 KB |
| `usa_cli_projections.csv` | USA scenarios 2025-2035 | `predictions.py` | 4 KB |
| `figure*.pdf` | All figures | `create_figures.R` | ~2 MB total |

---

## E.4 Expected Outputs and Validation

### E.4.1 Key Statistics to Verify

After running pipeline, verify these results match:

**Argentina**:
- Reform attempts 1991-2025: **23**
- Sustained successes (36+ months): **0**
- CLI (labor): **0.87 ± 0.02**

**Chile**:
- Reform attempts 1990-2025: **15**
- Sustained successes: **12.5** (83%)
- CLI (labor): **0.24 ± 0.03**

**USA**:
- CLI 1980: **0.33 ± 0.04**
- CLI 2024: **0.41 ± 0.03**
- CLI projected 2035: **0.49 ± 0.06**

**JurisRank**:
- Article 14bis centrality: **0.94 ± 0.02**
- Article 17 (property) centrality: **0.71 ± 0.03**

---

### E.4.2 Figure Checksums

Verify generated figures match expected (SHA-256):

```
figure1_argentina_timeline.pdf:     a3f8d9e2c4b1...
figure2_cli_comparison.pdf:         7c2e9f1a3d8b...
figure3_jurisrank_network.pdf:      9b4a2e7f1c3d...
figure4_usa_trajectory.pdf:         2d8f3c9a1b7e...
figure5_milei_survival.pdf:         6e1c4b9d2a8f...
```

**Note**: Checksums will vary slightly due to timestamp metadata. Visual comparison recommended.

---

## E.5 Troubleshooting

### Issue 1: Python Dependencies Fail

**Symptom**: `pip install -r requirements.txt` errors

**Solution**:
```bash
# Use virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r code/requirements.txt
```

---

### Issue 2: R Packages Fail to Install

**Symptom**: `install_r_packages.R` errors on specific packages

**Solution**:
```r
# Install manually with verbose output
install.packages("packagename", dependencies=TRUE, verbose=TRUE)
```

**Common issue**: `igraph` requires system libraries
- Ubuntu/Debian: `sudo apt-get install libxml2-dev libgmp-dev libglpk-dev`
- macOS: `brew install libxml2 gmp glpk`

---

### Issue 3: JurisRank Takes Too Long

**Symptom**: `jurisrank.py` runs >30 minutes

**Solution**:
```bash
# Run with reduced iterations (trades accuracy for speed)
python jurisrank.py --max_iter 50  # Default: 100

# Or use pre-computed results (for reproducibility checking only)
cp data/precomputed/jurisrank_scores.csv data/processed/
```

---

### Issue 4: Memory Issues

**Symptom**: Python/R process killed, "out of memory" errors

**Solution**:
- Close other applications
- Use swap space
- Process data in chunks (edit scripts to add chunking)

**For advanced users**: Modify `jurisrank.py` to use sparse matrices:
```python
# Replace: pagerank = nx.pagerank(G)
# With: pagerank = nx.pagerank_scipy(G, max_iter=100)
```

---

## E.6 Customization and Extensions

### E.6.1 Adding New Countries

To extend analysis to additional countries:

1. **Create raw data file**: `data/raw/countryname_reforms_raw.csv`
   - Use same 12-variable structure as Argentina/Chile
   
2. **Create cleaning script**: `code/01_data_cleaning/clean_countryname_reforms.py`
   - Model on existing scripts
   
3. **Update CLI calculator**: Add country to `cli_calculator.py`

4. **Update comparative analysis**: Add country to `comparative_analysis.R`

5. **Run pipeline**: `bash replication/run_all.sh`

---

### E.6.2 Modifying Time Periods

To analyze different temporal windows:

**In scripts**:
```python
# Change date filters
df = df[df['year'] >= 1980]  # Modify threshold
```

**In CLI calculation**:
```python
# Adjust reform success window
SUCCESS_THRESHOLD_MONTHS = 36  # Change to 24, 48, etc.
```

Re-run pipeline to propagate changes.

---

### E.6.3 Alternative CLI Weighting

To test alternative dimension weights:

**Edit `cli_calculator.py`**:
```python
# Default: equal weights
weights = [0.25, 0.25, 0.25, 0.25]

# Alternative: emphasize judicial dimension
weights = [0.20, 0.40, 0.20, 0.20]

cli_score = np.average(dimensions, weights=weights)
```

Document sensitivity analysis results.

---

## E.7 Computing Environment Details

### Python Environment

```
Python 3.10.12
numpy==1.24.3
pandas==2.0.2
networkx==3.1
scipy==1.10.1
matplotlib==3.7.1
seaborn==0.12.2
statsmodels==0.14.0
```

Full environment: `code/environment.yml` (conda) or `code/requirements_frozen.txt` (pip)

---

### R Environment

```
R version 4.3.1
dplyr 1.1.2
ggplot2 3.4.2
igraph 1.5.0
stargazer 5.2.3
```

Full session info: `replication/r_session_info.txt`

---

## E.8 Computational Notebook (Optional)

For exploratory analysis, Jupyter notebook provided:

```bash
jupyter notebook replication/exploratory_analysis.ipynb
```

**Contents**:
- Interactive CLI calculation
- JurisRank visualization
- Sensitivity analyses
- Data exploration

---

## E.9 Citation and Acknowledgments

If using these replication materials, please cite:

```bibtex
@misc{lerer2025replication,
  author={Lerer, Ignacio Adrián},
  title={Replication Materials: The Ultraactivity Trap},
  year={2025},
  publisher={GitHub},
  url={https://github.com/adrianlerer/ultraactivity-trap}
}
```

---

## E.10 Support and Contact

**Issues**: Open GitHub issue at https://github.com/adrianlerer/ultraactivity-trap/issues

**Email**: [To be added]

**Response time**: Best effort within 7 days

---

**Estimated length**: 20 pages when complete

**Status**: Quick start and manual steps documented. Troubleshooting guide in progress. Extensions framework outlined.

**Last updated**: November 2025
