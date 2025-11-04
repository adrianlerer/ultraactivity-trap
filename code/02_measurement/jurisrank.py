#!/usr/bin/env python3
"""
JurisRank: Citation Network Analysis for Legal Doctrines
========================================================

Calculates PageRank-based centrality scores for legal doctrines in citation networks.

Adapted from: Brin, S., & Page, L. (1998). The anatomy of a large-scale 
hypertextual Web search engine. Computer Networks and ISDN Systems.

Author: Ignacio Adrián Lerer
Date: January 2025
Version: 1.0
"""

import pandas as pd
import networkx as nx
import numpy as np
from pathlib import Path
import argparse

def load_citation_network(filepath):
    """
    Load legal citation network from CSV.
    
    Expected format:
    - citing_case, cited_case, year, doctrine_tag
    """
    df = pd.read_csv(filepath)
    return df

def build_network_graph(citations_df):
    """
    Build directed graph from citation data.
    """
    G = nx.DiGraph()
    
    for _, row in citations_df.iterrows():
        G.add_edge(row['citing_case'], row['cited_case'], 
                   year=row['year'],
                   doctrine=row['doctrine_tag'])
    
    return G

def calculate_jurisrank(G, damping=0.85, max_iter=100, tol=1e-6):
    """
    Calculate JurisRank scores using PageRank algorithm.
    
    Args:
        G: NetworkX directed graph
        damping: Damping factor (default 0.85)
        max_iter: Maximum iterations
        tol: Convergence tolerance
        
    Returns:
        Dict mapping case_id to JurisRank score
    """
    pagerank = nx.pagerank(G, alpha=damping, max_iter=max_iter, tol=tol)
    return pagerank

def main():
    parser = argparse.ArgumentParser(description='Calculate JurisRank scores')
    parser.add_argument('--input', default='../../data/raw/csjn_decisions_raw.csv',
                       help='Input citation data')
    parser.add_argument('--output', default='../../data/processed/jurisrank_scores.csv',
                       help='Output scores file')
    parser.add_argument('--damping', type=float, default=0.85,
                       help='Damping factor')
    
    args = parser.parse_args()
    
    print("JurisRank Calculator")
    print("=" * 50)
    
    # Load data
    print(f"Loading citations from {args.input}...")
    citations = load_citation_network(args.input)
    print(f"  Loaded {len(citations)} citations")
    
    # Build network
    print("Building citation network...")
    G = build_network_graph(citations)
    print(f"  Network: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    
    # Calculate JurisRank
    print(f"Calculating JurisRank (damping={args.damping})...")
    scores = calculate_jurisrank(G, damping=args.damping)
    
    # Convert to DataFrame
    scores_df = pd.DataFrame([
        {'case_id': case, 'jurisrank_score': score}
        for case, score in scores.items()
    ])
    scores_df = scores_df.sort_values('jurisrank_score', ascending=False)
    
    # Save
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    scores_df.to_csv(output_path, index=False)
    
    print(f"✓ Saved {len(scores_df)} scores to {args.output}")
    print(f"\nTop 5 cases by JurisRank:")
    print(scores_df.head())
    
if __name__ == "__main__":
    main()
