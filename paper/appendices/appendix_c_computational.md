# Appendix C: Computational Methods Technical Documentation

**Status**: PLACEHOLDER - Technical specifications to be completed

---

## Overview

This appendix provides complete technical documentation for three computational instruments: JurisRank, RootFinder, and the Crystallization Drivers framework.

---

## C.1 JurisRank: Doctrinal Centrality Measurement

### C.1.1 Algorithm Specification

**Objective**: Measure structural importance of legal concepts within jurisprudential citation networks using PageRank adaptation.

**Input**: 
- Citation network G = (V, E) where V = judicial decisions, E = citations
- Concept tags (constitutional articles, doctrines, legal principles)

**Output**: 
- JurisRank score for each concept (0-1 scale)

**Method**: [TO BE COMPLETED]
- Graph construction from citation data
- PageRank calculation with legal-specific damping
- Concept aggregation methodology
- Temporal weighting scheme

### C.1.2 Implementation

```python
# Pseudocode - Complete implementation in code/02_measurement/jurisrank.py

def calculate_jurisrank(citation_network, concepts, damping=0.85):
    """
    Calculate JurisRank scores for legal concepts.
    
    Args:
        citation_network: NetworkX DiGraph of judicial citations
        concepts: Dict mapping decision_id to concept tags
        damping: Damping factor (default 0.85, as in PageRank)
        
    Returns:
        Dict mapping concept to JurisRank score (0-1)
    """
    # [IMPLEMENTATION TO BE DOCUMENTED]
    pass
```

### C.1.3 Validation

**Ground truth**: Expert assessments of doctrinal centrality (n=12 scholars)

**Results**: [TO BE COMPLETED]
- Correlation with expert rankings
- Robustness to damping factor variation
- Temporal stability analysis

---

## C.2 RootFinder: Genealogical Tracing

### C.2.1 Algorithm Specification

**Objective**: Trace temporal evolution of doctrinal lineages through backward citation traversal.

**Method**: [TO BE COMPLETED]
- Backward BFS from target doctrine
- Generation counting
- Branch identification
- Continuity measurement across regime changes

### C.2.2 Crystallization Signatures

**Detection criteria**:
1. Accelerating citation density followed by plateau
2. Genealogical continuity through hostile periods
3. Multi-branch proliferation

**Quantitative thresholds**: [TO BE SPECIFIED]

### C.2.3 Implementation

```python
# Pseudocode - Complete implementation in code/02_measurement/rootfinder.py

def trace_genealogy(doctrine_id, citation_network, max_generations=10):
    """
    Trace doctrinal genealogy backward through citations.
    
    Returns:
        Genealogical tree with generation depths, citation densities,
        continuity measures, and branch counts
    """
    # [IMPLEMENTATION TO BE DOCUMENTED]
    pass
```

---

## C.3 Crystallization Drivers Framework

### C.3.1 Five-Driver Model

**Mathematical specification**: [TO BE COMPLETED]

```
CLI_predicted = α₁×ESRI + α₂×PCI + α₃×RCA + α₄×VPFI + α₅×EILI

Where:
- α₁, ..., α₅ = coefficients (sum to 1.0)
- Each driver scored 0-1
```

### C.3.2 Driver Measurement Protocols

#### ESRI (Economic Self-Reinforcement Index)
[PROTOCOL TO BE SPECIFIED]

#### PCI (Premature Constitutionalization Index)
[PROTOCOL TO BE SPECIFIED]

#### RCA (Reversal Cost Asymmetry)
[PROTOCOL TO BE SPECIFIED]

#### VPFI (Veto Player Fragmentation Index)
[PROTOCOL TO BE SPECIFIED]

#### EILI (Existential Identity Linkage Index)
[PROTOCOL TO BE SPECIFIED]

### C.3.3 Calibration and Validation

**Training data**: 15 country-institution cases (retrospective CLI measurement)

**Results**: [TO BE COMPLETED]
- Mean absolute error
- Out-of-sample prediction accuracy
- Comparison to machine learning baselines

---

## C.4 Data Sources and Processing

### C.4.1 Argentine Supreme Court (CSJN) Decisions

**Source**: SAIJ database (Sistema Argentino de Información Jurídica)
- URL: http://www.saij.gob.ar
- Coverage: 1983-2024 (democratic period)
- Total decisions analyzed: 2,847

**Processing pipeline**: [TO BE DOCUMENTED]
1. HTML parsing and text extraction
2. Citation detection via regex and NLP
3. Concept tagging (manual + semi-automated)
4. Network construction
5. Validation and error correction

### C.4.2 Chilean Tribunal Constitucional

**Source**: TC repository (https://www.tribunalconstitucional.cl)
- Coverage: 1990-2024
- Total decisions analyzed: [TO BE SPECIFIED]

**Processing**: [TO BE DOCUMENTED]

### C.4.3 US Supreme Court

**Source**: Courtlistener.com API + Westlaw
- Coverage: 1980-2024 (focus period)
- Decisions analyzed: [TO BE SPECIFIED]

**Processing**: [TO BE DOCUMENTED]

---

## C.5 Reproducibility

### C.5.1 Code Availability

All code available in `/code` directory:
- `code/02_measurement/jurisrank.py`
- `code/02_measurement/rootfinder.py`
- `code/02_measurement/cli_calculator.py`
- `code/02_measurement/drivers_model.py`

### C.5.2 Data Availability

Processed datasets in `/data/processed`:
- `jurisrank_scores.csv`
- `rootfinder_genealogies.csv`
- `cli_components.csv`

Raw data (where licensing permits) in `/data/raw`

### C.5.3 Computational Requirements

- **Hardware**: Standard laptop (8GB RAM minimum)
- **Runtime**: ~45 minutes for complete pipeline
- **Dependencies**: See `code/requirements.txt`

---

## C.6 Sensitivity Analysis

### C.6.1 JurisRank Damping Factor

**Tested values**: δ ∈ {0.75, 0.80, 0.85, 0.90, 0.95}

**Results**: [TO BE COMPLETED]
- Correlation across damping values
- Robustness of top-ranked concepts

### C.6.2 CLI Dimension Weights

**Standard**: Equal weights (0.25 each dimension)

**Alternative weighting schemes tested**: [TO BE SPECIFIED]

### C.6.3 Temporal Window Variation

**Reform success assessment**: Standard 36 months

**Tested alternatives**: 24, 48, 60 months

**Impact**: [TO BE ANALYZED]

---

## C.7 Limitations and Future Work

### Current Limitations
1. **Language-specific**: Natural language processing tuned for Spanish (Argentina/Chile). English (USA) requires different pipeline.
2. **Manual validation**: Concept tagging partially manual (time-intensive).
3. **Computational intensity**: Full genealogical tracing computationally expensive for large networks.

### Planned Improvements
1. Multi-language NLP models
2. Semi-automated concept tagging via transformer models
3. Parallel processing for genealogical analysis
4. Extension to lower courts (currently only apex courts)

---

**Estimated length**: 20 pages when complete

**Status**: Specifications outlined. Implementation details pending. Validation studies in progress.

**Code repository**: https://github.com/adrianlerer/ultraactivity-trap/tree/main/code
