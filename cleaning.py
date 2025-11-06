"""cleaning.py
Data cleaning steps: missing values, duplicates, rename teams, dtype conversions.
Produces cleaned CSVs in data/processed
"""
import pandas as pd
from pathlib import Path

RAW_DIR = Path('data/raw')
PROC_DIR = Path('data/processed')
PROC_DIR.mkdir(parents=True, exist_ok=True)

def clean_matches(matches_path, out_path):
    matches = pd.read_csv(matches_path)
    # Fill common missing values
    matches['city'].fillna('Unknown', inplace=True)
    matches['winner'].fillna('No Result', inplace=True)
    matches['player_of_match'].fillna('None', inplace=True)
    # Drop optional columns if exist
    matches.drop(columns=['method'], inplace=True, errors='ignore')
    # Team name corrections
    team_name_corrections = {
        'Delhi Daredevils': 'Delhi Capitals',
        'Deccan Chargers': 'Sunrisers Hyderabad',
        'Kings XI Punjab': 'Punjab Kings'
    }
    for col in ['team1','team2','winner','toss_winner']:
        if col in matches.columns:
            matches[col] = matches[col].replace(team_name_corrections)
    # Convert date
    if 'date' in matches.columns:
        matches['date'] = pd.to_datetime(matches['date'], errors='coerce')
    matches.drop_duplicates(inplace=True)
    matches.to_csv(out_path, index=False)
    print('Saved cleaned matches to', out_path)

def clean_deliveries(deliveries_path, out_path):
    deliveries = pd.read_csv(deliveries_path)
    deliveries['extras_type'].fillna('None', inplace=True)
    deliveries['fielder'].fillna('None', inplace=True)
    deliveries['batting_team'] = deliveries['batting_team'].replace({
        'Delhi Daredevils': 'Delhi Capitals',
        'Deccan Chargers': 'Sunrisers Hyderabad',
        'Kings XI Punjab': 'Punjab Kings'
    })
    deliveries['bowling_team'] = deliveries['bowling_team'].replace({
        'Delhi Daredevils': 'Delhi Capitals',
        'Deccan Chargers': 'Sunrisers Hyderabad',
        'Kings XI Punjab': 'Punjab Kings'
    })
    deliveries.drop_duplicates(inplace=True)
    deliveries.to_csv(out_path, index=False)
    print('Saved cleaned deliveries to', out_path)

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--matches', default='data/raw/matches.csv')
    p.add_argument('--deliveries', default='data/raw/deliveries.csv')
    p.add_argument('--out_matches', default='data/processed/cleaned_matches.csv')
    p.add_argument('--out_deliveries', default='data/processed/cleaned_deliveries.csv')
    args = p.parse_args()
    clean_matches(args.matches, args.out_matches)
    clean_deliveries(args.deliveries, args.out_deliveries)
