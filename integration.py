"""integration.py
Merge deliveries + matches into a single integrated dataset for analysis.
"""
import pandas as pd
from pathlib import Path

PROC_DIR = Path('data/processed')
OUT = Path('data/processed/integrated_ipl.csv')

def integrate(matches_csv, deliveries_csv, out_csv=OUT):
    matches = pd.read_csv(matches_csv)
    deliveries = pd.read_csv(deliveries_csv)
    integrated_df = deliveries.merge(matches, left_on='match_id', right_on='id', how='inner', suffixes=('_delivery','_match'))
    # Optionally drop redundant 'id' column from matches
    if 'id' in integrated_df.columns:
        integrated_df.drop(columns=['id'], inplace=True)
    integrated_df.to_csv(out_csv, index=False)
    print('Saved integrated dataset to', out_csv)
    return integrated_df

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--matches', default='data/processed/cleaned_matches.csv')
    p.add_argument('--deliveries', default='data/processed/cleaned_deliveries.csv')
    p.add_argument('--out', default='data/processed/integrated_ipl.csv')
    args = p.parse_args()
    integrate(args.matches, args.deliveries, args.out)
