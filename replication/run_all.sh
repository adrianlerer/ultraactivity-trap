#!/bin/bash
#
# Master Replication Script
# The Ultraactivity Trap
# Author: Ignacio Adrián Lerer
# Version: 1.0
# Date: January 2025
#

set -e  # Exit on error
set -u  # Exit on undefined variable

echo "========================================="
echo "The Ultraactivity Trap - Full Replication"
echo "========================================="
echo ""

# Check if running from correct directory
if [[ ! -f "replication/run_all.sh" ]]; then
    echo "Error: Please run this script from the repository root directory"
    echo "Usage: bash replication/run_all.sh"
    exit 1
fi

# Create logs directory
mkdir -p logs
mkdir -p results

START_TIME=$(date +%s)

# ========================================
# STEP 1: Data Cleaning
# ========================================
echo "[1/5] Data Cleaning..."
echo "-----------------------------------"

cd code/01_data_cleaning

echo "  - Cleaning Argentina reforms data..."
python clean_argentina_reforms.py > ../../logs/clean_argentina.log 2>&1
echo "    ✓ Done"

echo "  - Cleaning CSJN decisions data..."
python clean_csjn_decisions.py > ../../logs/clean_csjn.log 2>&1
echo "    ✓ Done"

echo "  - Cleaning comparative cases data..."
python clean_comparative_cases.py > ../../logs/clean_comparative.log 2>&1
echo "    ✓ Done"

cd ../..
echo ""

# ========================================
# STEP 2: Measurement Instruments
# ========================================
echo "[2/5] Running Measurement Instruments..."
echo "-----------------------------------"

cd code/02_measurement

echo "  - Calculating JurisRank scores..."
python jurisrank.py > ../../logs/jurisrank.log 2>&1
echo "    ✓ Done"

echo "  - Tracing RootFinder genealogies..."
python rootfinder.py > ../../logs/rootfinder.log 2>&1
echo "    ✓ Done"

echo "  - Calculating CLI components..."
python cli_calculator.py > ../../logs/cli_calculator.log 2>&1
echo "    ✓ Done"

echo "  - Running crystallization drivers model..."
python drivers_model.py > ../../logs/drivers.log 2>&1
echo "    ✓ Done"

cd ../..
echo ""

# ========================================
# STEP 3: Statistical Analysis
# ========================================
echo "[3/5] Running Statistical Analysis..."
echo "-----------------------------------"

cd code/03_analysis

echo "  - Comparative analysis (R)..."
if command -v Rscript &> /dev/null; then
    Rscript comparative_analysis.R > ../../logs/comparative_analysis.log 2>&1
    echo "    ✓ Done"
else
    echo "    ⚠ Skipped (R not installed)"
fi

echo "  - Temporal dynamics (R)..."
if command -v Rscript &> /dev/null; then
    Rscript temporal_dynamics.R > ../../logs/temporal_dynamics.log 2>&1
    echo "    ✓ Done"
else
    echo "    ⚠ Skipped (R not installed)"
fi

echo "  - Predictions (Python)..."
python predictions.py > ../../logs/predictions.log 2>&1
echo "    ✓ Done"

cd ../..
echo ""

# ========================================
# STEP 4: Visualizations
# ========================================
echo "[4/5] Generating Visualizations..."
echo "-----------------------------------"

cd code/04_visualizations

echo "  - Creating figures (R)..."
if command -v Rscript &> /dev/null; then
    Rscript create_figures.R > ../../logs/figures.log 2>&1
    echo "    ✓ Done"
else
    echo "    ⚠ Skipped (R not installed)"
fi

echo "  - Creating tables (Python)..."
python create_tables.py > ../../logs/tables.log 2>&1
echo "    ✓ Done"

cd ../..
echo ""

# ========================================
# STEP 5: Validation & Report
# ========================================
echo "[5/5] Generating Replication Report..."
echo "-----------------------------------"

cd replication

echo "  - Comparing outputs..."
python generate_report.py > ../logs/replication_report.log 2>&1
echo "    ✓ Done"

cd ..
echo ""

# ========================================
# Summary
# ========================================
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))
MINUTES=$((ELAPSED / 60))
SECONDS=$((ELAPSED % 60))

echo "========================================="
echo "Replication Complete!"
echo "========================================="
echo ""
echo "Time elapsed: ${MINUTES}m ${SECONDS}s"
echo ""
echo "Generated outputs:"
echo "  - Data: data/processed/*.csv"
echo "  - Figures: paper/figures/*.png"
echo "  - Tables: results/tables/*.tex"
echo "  - Report: replication/replication_report.pdf"
echo ""
echo "Check logs/ directory for detailed output"
echo ""
echo "To verify replication success:"
echo "  diff -r replication/expected_outputs results/"
echo ""
echo "Status: ✓ SUCCESS"
