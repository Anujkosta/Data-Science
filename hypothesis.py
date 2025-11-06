"""hypothesis.py
Example Chi-square test: toss decision vs match outcome.
"""
import pandas as pd
from scipy.stats import chi2_contingency

def toss_chi_square(matches_csv):
    matches = pd.read_csv(matches_csv)
    matches['toss_win_match_win'] = matches.apply(lambda row: 1 if row.get('toss_winner') == row.get('winner') else 0, axis=1)
    contingency_table = pd.crosstab(matches.get('toss_decision'), matches['toss_win_match_win'])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    print('Contingency Table:\n', contingency_table)
    print('\nChi2:', chi2, 'p-value:', p, 'dof:', dof)
    return chi2, p, dof, expected

if __name__ == '__main__':
    toss_chi_square('data/processed/cleaned_matches.csv')
