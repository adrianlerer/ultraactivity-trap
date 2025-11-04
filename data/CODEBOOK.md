# Data Codebook

**Project**: The Ultraactivity Trap  
**Author**: Ignacio Adrián Lerer  
**Version**: 1.0  
**Date**: January 2025

---

## Overview

This codebook describes all variables in the datasets used for "The Ultraactivity Trap" analysis. Data is organized into raw (original sources) and processed (cleaned, coded) folders.

---

## Table of Contents

1. [argentina_reforms_coded.csv](#argentina_reforms_coded)
2. [cli_components.csv](#cli_components)
3. [jurisrank_scores.csv](#jurisrank_scores)
4. [rootfinder_genealogies.csv](#rootfinder_genealogies)
5. [comparative_cases.csv](#comparative_cases)

---

## 1. argentina_reforms_coded.csv

**Description**: Complete coding of all labor reform attempts in Argentina (1983-2024)

**Unit of analysis**: Reform attempt (n=23)

### Variables

| Variable | Type | Range | Description |
|----------|------|-------|-------------|
| `reform_id` | string | ARG_REF_001 to ARG_REF_023 | Unique identifier |
| `year` | integer | 1983-2024 | Year of reform attempt |
| `president` | string | - | President during attempt |
| `party` | categorical | Peronist, Radical, PRO, LLA | Governing party |
| `reform_type` | categorical | deregulation, flexibilization, full_repeal | Type of reform |
| `legislative_status` | categorical | proposed, committee, floor_vote, enacted | Legislative progress |
| `csjn_review` | binary | 0/1 | Whether Supreme Court reviewed |
| `csjn_decision` | categorical | upheld, struck_down, partial, NA | Court decision |
| `ultraactivity_affected` | binary | 0/1 | Whether ultraactivity was targeted |
| `success` | binary | 0/1 | Reform succeeded (1) or failed (0) |
| `cgt_opposition` | ordinal | 0-5 | Intensity of CGT opposition |
| `strike_days` | integer | 0-365 | Days of strikes mobilized |
| `media_coverage` | ordinal | 1-5 | Media attention level |
| `international_pressure` | binary | 0/1 | IMF/World Bank conditionality |
| `economic_crisis` | binary | 0/1 | Reform during economic crisis |
| `jurisrank_ultraactivity` | float | 0-1 | JurisRank centrality score (year of reform) |
| `cli_t` | float | 0-1 | CLI score at time t |
| `cli_t_plus_2` | float | 0-1 | CLI score 2 years after reform |
| `notes` | text | - | Qualitative notes |
| `sources` | text | - | Primary sources (semicolon separated) |

### Data Sources

- **Legislative records**: Honorable Congreso de la Nación Argentina (HCDN/HCSEN)
- **CSJN decisions**: SAIJ database (saij.gob.ar)
- **CGT mobilization**: CGT official communications, press releases
- **Media coverage**: La Nación, Clarín, Página/12 archives
- **Economic data**: INDEC, World Bank WDI

### Notes

- `success = 1` only if reform was enacted AND survived judicial review
- `jurisrank_ultraactivity` calculated from citation network at time t
- Missing values coded as `NA` (not applicable) vs `NULL` (data unavailable)

---

## 2. cli_components.csv

**Description**: Constitutional Lock-in Index components across countries and time

**Unit of analysis**: Country-year (n=165, 5 countries × 33 years)

### Variables

| Variable | Type | Range | Description |
|----------|------|-------|-------------|
| `country_code` | string | ISO 3166-1 alpha-3 | Country identifier |
| `country_name` | string | - | Full country name |
| `year` | integer | 1990-2024 | Year of observation |
| `constitutional_entrenchment` | float | 0-1 | Dimension 1: Amendment difficulty |
| `judicial_review_density` | float | 0-1 | Dimension 2: Court precedent strength |
| `interest_group_capture` | float | 0-1 | Dimension 3: Institutional capture |
| `memetic_propagation` | float | 0-1 | Dimension 4: Ideological spread |
| `cli_overall` | float | 0-1 | Aggregate CLI (mean of 4 dimensions) |
| `cli_category` | categorical | low, medium, high, terminal | Categorical CLI (0-0.35, 0.35-0.60, 0.60-0.85, 0.85-1.0) |
| `reform_attempts` | integer | 0-50 | Number of reform attempts (cumulative) |
| `reform_success_rate` | float | 0-1 | Proportion of successful reforms |
| `government_alternation` | binary | 0/1 | Whether government changed that year |
| `democracy_score` | float | 0-10 | V-Dem polyarchy index |
| `gdp_per_capita` | float | - | GDP per capita (constant 2015 USD) |
| `data_quality` | categorical | high, medium, low | Data completeness/reliability |
| `notes` | text | - | Qualitative observations |
| `sources` | text | - | Primary sources |

### CLI Calculation Formula

```
CLI = (constitutional_entrenchment + judicial_review_density + 
       interest_group_capture + memetic_propagation) / 4
```

### Countries Included

- **ARG**: Argentina (1990-2024, n=35)
- **CHL**: Chile (1990-2024, n=35)
- **BRA**: Brazil (1990-2024, n=35)
- **ESP**: Spain (1990-2024, n=35)
- **USA**: United States (1990-2024, n=35)

### Data Sources

- **Constitutional entrenchment**: Comparative Constitutions Project
- **Judicial review**: Supreme Court/Constitutional Court databases
- **Interest group capture**: Transparency International, union membership data
- **Memetic propagation**: Media analysis, legal citation networks
- **Democracy scores**: V-Dem Institute
- **Economic data**: World Bank WDI

---

## 3. jurisrank_scores.csv

**Description**: JurisRank centrality scores for key legal doctrines

**Unit of analysis**: Legal doctrine-year (n=450)

### Variables

| Variable | Type | Range | Description |
|----------|------|-------|-------------|
| `doctrine_id` | string | - | Unique doctrine identifier |
| `doctrine_name` | string | - | Common name of doctrine |
| `country` | string | ISO 3166-1 alpha-3 | Country |
| `year` | integer | 1980-2024 | Year of measurement |
| `jurisrank_score` | float | 0-1 | PageRank-based centrality |
| `in_citations` | integer | 0-500 | Number of incoming citations |
| `out_citations` | integer | 0-100 | Number of outgoing citations |
| `centrality_rank` | integer | 1-N | Rank among all doctrines (year) |
| `doctrine_age` | integer | 0-100 | Years since doctrine established |
| `crystallization_status` | categorical | nascent, growing, crystallized, declining | Lifecycle stage |
| `temporal_derivative` | float | -1 to 1 | Change in JurisRank (3-year moving average) |
| `network_density` | float | 0-1 | Local network density around doctrine |
| `betweenness_centrality` | float | 0-1 | Betweenness in citation network |
| `notes` | text | - | Qualitative observations |

### JurisRank Algorithm

Adaptation of PageRank (Brin & Page 1998) to legal citation networks:

```
JR(d) = (1-δ)/N + δ × Σ [JR(c_i) / L(c_i)]
```

Where:
- `d` = doctrine
- `δ` = damping factor (0.85)
- `N` = total doctrines in network
- `c_i` = citing doctrine
- `L(c_i)` = number of doctrines cited by c_i

### Data Sources

- **Argentina**: SAIJ database, 2,847 CSJN decisions
- **Chile**: Tribunal Constitucional database, 156 decisions
- **USA**: Westlaw/LexisNexis, Supreme Court citations

---

## 4. rootfinder_genealogies.csv

**Description**: Genealogical evolution of ultraactivity doctrine

**Unit of analysis**: Precedent in genealogical chain (n=87)

### Variables

| Variable | Type | Range | Description |
|----------|------|-------|-------------|
| `precedent_id` | string | - | Unique identifier |
| `case_name` | string | - | Full case citation |
| `court` | string | - | Court that issued decision |
| `date` | date | YYYY-MM-DD | Decision date |
| `generation` | integer | 1-5 | Generation in evolutionary tree |
| `parent_id` | string | - | Precedent ID of parent (NULL if root) |
| `children_ids` | string | - | Comma-separated children IDs |
| `mutation_type` | categorical | extension, restriction, reinterpretation, innovation | Type of doctrinal change |
| `analogical_distance` | float | 0-1 | Distance from original ultraactivity (labor) |
| `domain` | categorical | labor, tax, administrative, constitutional | Legal domain |
| `outcome` | categorical | upheld, expanded, limited, overruled | Effect on ultraactivity |
| `vote_split` | string | - | Voting split (e.g., "5-4", "unanimous") |
| `dissent_strength` | float | 0-1 | Intensity of dissent (if any) |
| `citation_count` | integer | 0-500 | Times cited by later cases |
| `ratchet_effect` | binary | 0/1 | Whether decision created irreversible precedent |
| `summary` | text | - | Brief summary of holding |
| `sources` | text | - | Full citation and database link |

### Genealogical Generations

1. **Generation 1** (1953-1957): Founding - Ley 14250, CSJN constitutionalization
2. **Generation 2** (1958-1975): Labor consolidation - Extension to all sectors
3. **Generation 3** (1976-1990): Analogical spread - Beyond labor (tax, admin)
4. **Generation 4** (1991-2010): Entrenchment - Rejection of reform attempts
5. **Generation 5** (2011-present): Terminal lock-in - Even libertarian govt respects

### Data Sources

- **CSJN decisions**: SAIJ database (saij.gob.ar)
- **Legal doctrine**: Argentine labor law treatises
- **Legislative history**: Congressional records

---

## 5. comparative_cases.csv

**Description**: Comparative cases across countries for validation

**Unit of analysis**: Country (n=5)

### Variables

| Variable | Type | Range | Description |
|----------|------|-------|-------------|
| `country_code` | string | ISO 3166-1 alpha-3 | Country identifier |
| `country_name` | string | - | Full name |
| `region` | categorical | Latin America, Europe, North America | Geographic region |
| `legal_tradition` | categorical | civil_law, common_law, mixed | Legal family |
| `ultraactivity_present` | binary | 0/1 | Ultraactivity doctrine exists |
| `ultraactivity_year_introduced` | integer | 1900-2024 | Year doctrine introduced (NA if absent) |
| `cli_2024` | float | 0-1 | Current CLI score |
| `cli_1990` | float | 0-1 | Baseline CLI score |
| `cli_trajectory` | categorical | rising, stable, declining | 34-year trend |
| `reform_attempts_count` | integer | 0-50 | Total reform attempts (1990-2024) |
| `reform_success_rate` | float | 0-1 | Proportion successful |
| `democracy_avg` | float | 0-10 | Mean V-Dem polyarchy (1990-2024) |
| `gdp_pc_avg` | float | - | Mean GDP per capita (1990-2024) |
| `union_density_avg` | float | 0-100 | Mean union density % (1990-2024) |
| `political_stability` | float | -2.5 to 2.5 | World Bank governance indicator |
| `judicial_independence` | float | 0-1 | V-Dem judicial independence |
| `notes` | text | - | Country-specific observations |
| `sources` | text | - | Primary data sources |

### Country Selection Rationale

- **Argentina**: Archetypal ultraactivity trap (CLI 0.87)
- **Chile**: Control case - no ultraactivity, bidirectional reform (CLI 0.24)
- **Brazil**: Partial ultraactivity, high CLI but reform possible (CLI 0.72)
- **Spain**: European civil law, post-Franco transition (CLI 0.43)
- **USA**: Common law, rising CLI via judicialization (CLI 0.41)

### Data Sources

- **CLI calculations**: Author's calculations (see methodology)
- **Reform data**: National legislative archives
- **Democracy/governance**: V-Dem Institute, World Bank WGI
- **Economic data**: World Bank WDI, OECD
- **Union data**: ILO Statistics, national labor ministries

---

## Data Processing Pipeline

### 1. Raw Data Collection

```
data/raw/
  ├── argentina_reforms_raw.csv      # Scraped from legislative archives
  ├── csjn_decisions_raw.csv         # SAIJ database export
  ├── chile_reforms_raw.csv          # Chilean official gazette
  └── comparative_cases_raw.csv      # Compiled from multiple sources
```

### 2. Data Cleaning

Scripts in `code/01_data_cleaning/`:
- `clean_argentina_reforms.py` - Standardize dates, categorize reforms
- `clean_csjn_decisions.py` - Parse citations, extract holdings
- `clean_comparative_cases.py` - Harmonize country-level variables

### 3. Measurement

Scripts in `code/02_measurement/`:
- `jurisrank.py` - Calculate citation centrality
- `rootfinder.py` - Trace genealogical evolution
- `cli_calculator.py` - Compute CLI components and aggregate
- `drivers_model.py` - Run crystallization drivers model

### 4. Analysis

Scripts in `code/03_analysis/`:
- `comparative_analysis.R` - Cross-country regressions
- `temporal_dynamics.R` - Time-series analysis
- `predictions.py` - Forward projections (USA 2025-2035)

---

## Missing Data Conventions

- **NA**: Not applicable (e.g., ultraactivity year for countries without ultraactivity)
- **NULL**: Data unavailable (e.g., missing CGT records from 1983)
- **-999**: Numerical missing value (when NULL not supported)

---

## Quality Assurance

### Data Quality Levels

- **High**: Official government sources, verified by multiple archives
- **Medium**: Single authoritative source or reconstructed from secondary sources
- **Low**: Estimated or inferred from qualitative evidence

### Validation Checks

1. **Temporal consistency**: No anachronisms (e.g., citations before precedent exists)
2. **Cross-validation**: Key variables checked against multiple sources
3. **Expert review**: Argentine labor law experts reviewed coding
4. **Replication**: Independent coder recoded 20% of reforms (κ = 0.89)

---

## Updates and Corrections

This codebook reflects data as of January 2025. For updates or to report errors:

**Contact**: adrianlerer@gmail.com  
**GitHub Issues**: https://github.com/adrianlerer/ultraactivity-trap/issues

---

## Citation

When using this data, please cite:

> Lerer, I. A. (2025). The Ultraactivity Trap: Data Codebook (Version 1.0). GitHub. https://github.com/adrianlerer/ultraactivity-trap

---

**Last updated**: January 15, 2025  
**Version**: 1.0.0
