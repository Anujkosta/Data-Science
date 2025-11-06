"""feature_engineering.py
Scaling, encoding, derived features and discretization.
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from pathlib import Path

def transform_summary(reduced_csv='data/processed/reduced_ipl.csv', out_transformed='data/processed/transformed_ipl.csv', out_discretized='data/processed/discretized_ipl.csv'):
    match_summary = pd.read_csv(reduced_csv)
    scaler = StandardScaler()
    cols = [c for c in ['total_runs','batsman_runs','extra_runs','is_wicket'] if c in match_summary.columns]
    if cols:
        match_summary[[f"{c}_scaled" for c in cols]] = scaler.fit_transform(match_summary[cols])
    minmax = MinMaxScaler()
    for c in ['total_runs','batsman_runs']:
        if c in match_summary.columns:
            match_summary[f"{c}_norm"] = minmax.fit_transform(match_summary[[c]])
    le = LabelEncoder()
    if 'batting_team' in match_summary.columns:
        match_summary['batting_team_encoded'] = le.fit_transform(match_summary['batting_team'])
    if 'season' in match_summary.columns:
        match_summary['season_encoded'] = le.fit_transform(match_summary['season'].astype(str))
    if 'total_runs' in match_summary.columns:
        match_summary['run_rate'] = match_summary['total_runs'] / 20.0
        match_summary['boundary_ratio'] = match_summary['batsman_runs'] / match_summary['total_runs'].replace(0,1)
        match_summary['score_category'] = pd.cut(match_summary['total_runs'], bins=[0,120,180,300], labels=['Low','Medium','High'])
    # Discretization
    if 'is_wicket' in match_summary.columns:
        match_summary['wickets_bin'] = pd.cut(match_summary['is_wicket'], bins=[0,4,8,20], labels=['Few','Moderate','Many'])
    match_summary.to_csv(out_transformed, index=False)
    match_summary.to_csv(out_discretized, index=False)
    print('Saved transformed and discretized datasets to', out_transformed, out_discretized)

if __name__ == '__main__':
    transform_summary()
