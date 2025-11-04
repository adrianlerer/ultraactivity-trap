#!/usr/bin/env python3
"""
CLI Calculator: Constitutional Lock-in Index
============================================

Calculates aggregate Constitutional Lock-in Index from 4 dimensions:
1. Constitutional entrenchment
2. Judicial review density
3. Interest group capture
4. Memetic propagation

Reference: Lerer (2024), "Constitutional Lock-in Index" (SSRN 5402461)

Author: Ignacio Adrián Lerer
Date: January 2025
Version: 1.0
"""

import pandas as pd
import numpy as np
from pathlib import Path

def calculate_cli(entrenchment, judicial, capture, memetic):
    """
    Calculate CLI as mean of 4 dimensions.
    
    CLI = (D1 + D2 + D3 + D4) / 4
    
    where:
    - D1 = Constitutional entrenchment (0-1)
    - D2 = Judicial review density (0-1)
    - D3 = Interest group capture (0-1)
    - D4 = Memetic propagation (0-1)
    """
    return (entrenchment + judicial + capture + memetic) / 4

def categorize_cli(cli_score):
    """
    Categorize CLI into discrete levels.
    """
    if cli_score < 0.35:
        return 'low'
    elif cli_score < 0.60:
        return 'medium'
    elif cli_score < 0.85:
        return 'high'
    else:
        return 'terminal'

def main():
    print("CLI Calculator")
    print("=" * 50)
    
    # Load component data (placeholder - replace with actual data loading)
    # In real implementation, load from data/raw/
    
    print("Calculating CLI scores...")
    
    # Example calculation for Argentina
    argentina_cli = calculate_cli(
        entrenchment=0.92,  # High constitutional protection
        judicial=0.88,       # Dense precedent network
        capture=0.85,        # Strong union capture
        memetic=0.83         # Widespread ideology
    )
    
    print(f"Argentina CLI: {argentina_cli:.3f} ({categorize_cli(argentina_cli)})")
    
    # Save results (placeholder)
    results = pd.DataFrame({
        'country': ['Argentina'],
        'cli_overall': [argentina_cli],
        'cli_category': [categorize_cli(argentina_cli)]
    })
    
    output_path = Path('../../data/processed/cli_components.csv')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(output_path, index=False)
    
    print(f"✓ Saved results to {output_path}")

if __name__ == "__main__":
    main()
