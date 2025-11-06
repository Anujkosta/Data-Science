#IPL Data Science (Repo)

This repository contains code to process, analyze, and extract insights from IPL match & delivery datasets.

**Features**
- Data extraction from a zipped archive
- Data cleaning and standardization
- Integration (merging matches & deliveries)
- Exploratory Data Analysis (descriptive stats)
- Feature engineering (scaling, encoding, derived features)
- PCA and SVD for dimensionality reduction
- Hypothesis testing (chi-square example)


**Quick Start**
1. Clone the repo
2. Place `archive(IPL).zip` into `data/raw/` or run `python src/extract.py --zip /path/archive(IPL).zip --out data/raw`
3. Clean the datasets:
   ```bash
   python src/cleaning.py --matches data/raw/matches.csv --deliveries data/raw/deliveries.csv
   ```
4. Integrate datasets:
   ```bash
   python src/integration.py --matches data/processed/cleaned_matches.csv --deliveries data/processed/cleaned_deliveries.csv
   ```
5. Run feature engineering:
   ```bash
   python src/feature_engineering.py
   ```
6. Run PCA & SVD:
   ```bash
   python src/pca_svd.py
   ```

**Files**
- `src/` : modular scripts
- `data/` : raw and processed datasets
- `reports/` : generated outputs and visualizations

**License**
MIT
