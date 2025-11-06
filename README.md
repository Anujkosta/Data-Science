📊 IPL Data Science (Repo)
This repository contains code to process, analyze, and extract insights from IPL match and delivery datasets.

🚀 Features
📦 Data extraction from a zipped archive
🧹 Data cleaning and standardization
🔗 Integration (merging matches & deliveries)
📈 Exploratory Data Analysis (descriptive stats)
🛠️ Feature engineering (scaling, encoding, derived features)
🔍 Dimensionality reduction using PCA and SVD
🧪 Hypothesis testing (chi-square example)


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

📁 Repository Structure
src/ : Modular scripts for each processing step
data/ : Raw and processed datasets
reports/ : Generated outputs and visualizations
docs/ : 📄 Includes uploaded PDF with code and output snapshots for reference

📄 Documentation
A PDF containing the full codebase and sample outputs has been uploaded for reference. It provides a walkthrough of each module and its results, useful for understanding the pipeline and verifying outputs.

📜 License
This project is licensed under the MIT License.
