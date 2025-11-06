"""eda.py
Descriptive statistics for numeric and categorical columns; saves CSV summaries.
"""
import pandas as pd
from pathlib import Path

def descriptive(matches_csv, out_numeric='data/processed/descriptive_numeric.csv', out_categorical='data/processed/descriptive_categorical.csv'):
    matches = pd.read_csv(matches_csv)
    desc_numeric = matches.describe().T
    desc_categorical = matches.describe(include=['object']).T
    desc_numeric.to_csv(out_numeric)
    desc_categorical.to_csv(out_categorical)
    print('Saved descriptive summaries to', out_numeric, out_categorical)

if __name__ == '__main__':
    descriptive('data/processed/cleaned_matches.csv')
