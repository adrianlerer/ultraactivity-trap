# Replication Guide

**Project**: The Ultraactivity Trap  
**Author**: Ignacio Adrián Lerer  
**Version**: 1.0  
**Date**: January 2025

---

## Overview

This guide provides step-by-step instructions to replicate all analyses, figures, and tables in "The Ultraactivity Trap: How Temporal Asymmetry Transforms Repeated Games into Terminal Betrayal."

**Expected time**: ~45 minutes on standard laptop (MacBook Pro M1, 16GB RAM)

---

## Prerequisites

### Software Requirements

- **Python**: 3.9 or higher
- **R**: 4.2 or higher
- **Git**: For cloning repository
- **LaTeX**: (Optional) For recompiling paper

### System Requirements

- **RAM**: Minimum 8GB, recommended 16GB
- **Disk space**: ~2GB for repository and outputs
- **OS**: macOS, Linux, or Windows (with WSL recommended)

---

## Quick Start (Automated)

```bash
# 1. Clone repository
git clone https://github.com/adrianlerer/ultraactivity-trap.git
cd ultraactivity-trap

# 2. Install Python dependencies
pip install -r code/requirements.txt

# 3. Install R packages (if using R scripts)
Rscript -e "install.packages(c('tidyverse', 'stargazer', 'lfe', 'estimatr'))"

# 4. Run complete replication
bash replication/run_all.sh
```

This will:
- Clean all raw data
- Calculate JurisRank, RootFinder, and CLI scores
- Run all analyses
- Generate all figures and tables
- Create replication report

**Output**: Check `replication/expected_outputs/` for generated files

---

## Step-by-Step (Manual)

If you want to understand each step or run components individually:

### Step 1: Data Cleaning

```bash
cd code/01_data_cleaning

# Clean Argentina reform attempts data
python clean_argentina_reforms.py

# Clean CSJN decisions data  
python clean_csjn_decisions.py

# Clean comparative cases data
python clean_comparative_cases.py
```

**Outputs**: `data/processed/*.csv` files

**Validation**: Check that processed files have expected row counts:
- `argentina_reforms_coded.csv`: 23 rows
- `csjn_decisions_processed.csv`: 2,847 rows
- `comparative_cases.csv`: 5 rows

### Step 2: Measurement Instruments

```bash
cd ../02_measurement

# Calculate JurisRank scores
python jurisrank.py

# Trace RootFinder genealogies
python rootfinder.py

# Calculate CLI components
python cli_calculator.py

# Run crystallization drivers model
python drivers_model.py
```

**Outputs**:
- `data/processed/jurisrank_scores.csv`
- `data/processed/rootfinder_genealogies.csv`
- `data/processed/cli_components.csv`
- `data/processed/crystallization_drivers.csv`

**Validation**: 
- JurisRank for ultraactivity (ARG, 2024) should be ~0.87
- CLI for Argentina (2024) should be 0.87
- CLI for Chile (2024) should be 0.24

### Step 3: Statistical Analysis

```bash
cd ../03_analysis

# Comparative analysis
Rscript comparative_analysis.R

# Temporal dynamics
Rscript temporal_dynamics.R

# Predictions (USA 2025-2035)
python predictions.py
```

**Outputs**:
- `results/regression_results.txt`
- `results/temporal_trends.csv`
- `results/usa_predictions.csv`

**Validation**:
- Main regression coefficient (ultraactivity → reform failure) should be ~-0.78 (p < 0.001)
- USA CLI projection for 2035 should be ~0.49

### Step 4: Visualizations

```bash
cd ../04_visualizations

# Generate all figures
Rscript create_figures.R
python create_tables.py
```

**Outputs**: `paper/figures/figure*.png`

**Validation**: Compare with `replication/expected_outputs/figures/`

### Step 5: Replication Report

```bash
cd ../../replication

# Generate replication report
python generate_report.py
```

**Output**: `replication/replication_report.pdf`

This compares your outputs with expected outputs and flags any discrepancies.

---

## Troubleshooting

### Issue: Missing Python packages

**Solution**:
```bash
pip install --upgrade pip
pip install -r code/requirements.txt
```

### Issue: Missing R packages

**Solution**:
```bash
Rscript -e "install.packages(c('tidyverse', 'stargazer', 'lfe', 'estimatr'), repos='https://cloud.r-project.org')"
```

### Issue: JurisRank calculation fails

**Problem**: Large citation network requires significant RAM

**Solution**: 
```python
# In jurisrank.py, adjust memory settings:
import os
os.environ['PYTHONHASHSEED'] = '0'
```

Or use smaller sample:
```bash
python jurisrank.py --sample 0.5  # Use 50% random sample
```

### Issue: Figures don't match exactly

**Expected**: Minor differences in floating-point precision across systems are normal

**Acceptable difference**: <0.01 for continuous variables, <1% for percentages

**Not acceptable**: Qualitatively different patterns, sign flips, or missing data points

### Issue: R scripts fail on Windows

**Problem**: Path separators (`/` vs `\`)

**Solution**: Use Windows Subsystem for Linux (WSL) or:
```R
# In R scripts, replace:
file.path("path", "to", "file")  # Instead of "path/to/file"
```

---

## Expected Outputs

### Data Files

| File | Rows | Columns | Key Variables |
|------|------|---------|---------------|
| `argentina_reforms_coded.csv` | 23 | 20 | reform_id, success, cli_t |
| `jurisrank_scores.csv` | 450 | 14 | doctrine_id, jurisrank_score |
| `cli_components.csv` | 165 | 16 | country, year, cli_overall |
| `rootfinder_genealogies.csv` | 87 | 17 | precedent_id, generation |

### Figures

| Figure | Type | Description |
|--------|------|-------------|
| `figure1_bicycle_tank_game.png` | Diagram | Game theory illustration |
| `figure2_cli_evolution.png` | Line plot | CLI over time (5 countries) |
| `figure3_memetic_spread.png` | Network | Genealogical tree |
| `figure4_comparative_cli.png` | Bar chart | Cross-country CLI comparison |
| `figure5_predictions.png` | Line plot | USA CLI projections |

### Tables

| Table | Description |
|-------|-------------|
| Table 1 | Summary statistics |
| Table 2 | Regression results (ultraactivity → reform failure) |
| Table 3 | CLI decomposition by country |
| Table 4 | Comparative case descriptions |
| Table 5 | USA predictions (2025-2035) |

---

## Validation Checklist

Use this checklist to verify successful replication:

- [ ] **Data cleaning**
  - [ ] All processed CSV files created
  - [ ] Row counts match expected
  - [ ] No missing values in key variables
  
- [ ] **Measurement**
  - [ ] JurisRank scores calculated (Argentina ultraactivity ~0.87)
  - [ ] CLI components calculated (Argentina ~0.87, Chile ~0.24)
  - [ ] RootFinder identified 5 generations
  
- [ ] **Analysis**
  - [ ] Regression coefficient ~-0.78 (p < 0.001)
  - [ ] USA CLI projection 2035 ~0.49
  - [ ] All statistical tests converge
  
- [ ] **Visualizations**
  - [ ] All 5 figures generated
  - [ ] Figures match expected outputs (qualitatively)
  - [ ] No missing data points or plotting errors
  
- [ ] **Replication report**
  - [ ] Report generated successfully
  - [ ] No major discrepancies flagged
  - [ ] All tests pass

---

## Computational Environment

To ensure exact replication, use the provided computational environment:

### Docker (Recommended)

```bash
# Build Docker image
docker build -t ultraactivity-trap .

# Run replication in container
docker run -v $(pwd)/results:/app/results ultraactivity-trap
```

### Virtual Environment (Alternative)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r code/requirements.txt

# Run replication
bash replication/run_all.sh
```

---

## Reporting Issues

If you encounter problems:

1. **Check troubleshooting section** above
2. **Verify software versions** match requirements
3. **Review error logs** in `logs/` directory
4. **Open GitHub issue**: https://github.com/adrianlerer/ultraactivity-trap/issues

When reporting issues, please include:
- Operating system and version
- Python version (`python --version`)
- R version (`R --version`)
- Error message and full stack trace
- Steps to reproduce

---

## Contributing Improvements

Found a bug or have suggestions? Pull requests welcome!

1. Fork repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Make changes
4. Run replication to verify (`bash replication/run_all.sh`)
5. Commit changes (`git commit -m "Describe improvement"`)
6. Push to branch (`git push origin feature/improvement`)
7. Open pull request

---

## Computational Details

### Random Seeds

All analyses use fixed seeds for reproducibility:
- Python: `np.random.seed(42)`
- R: `set.seed(42)`

### Parallel Computing

For faster execution, some scripts support parallel processing:

```bash
# JurisRank with 4 cores
python jurisrank.py --cores 4

# R analysis with parallel backend
Rscript comparative_analysis.R --cores 4
```

### Memory Optimization

If running into memory issues:

```python
# In Python scripts, use chunking:
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process(chunk)
```

---

## Citation

If you replicate or extend this work, please cite:

> Lerer, I. A. (2025). The Ultraactivity Trap: How Temporal Asymmetry Transforms Repeated Games into Terminal Betrayal. SSRN Working Paper. https://github.com/adrianlerer/ultraactivity-trap

---

## Contact

**Ignacio Adrián Lerer**  
Email: adrianlerer@gmail.com  
GitHub: @adrianlerer

---

**Last updated**: January 15, 2025  
**Version**: 1.0.0
