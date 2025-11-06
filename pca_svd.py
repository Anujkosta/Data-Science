"""pca_svd.py
Standardize numeric columns, run PCA and TruncatedSVD and save results.
"""
import pandas as pd
from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.preprocessing import StandardScaler
from pathlib import Path

def run_pca_svd(matches_csv, out_pca='data/processed/pca_results.csv', out_svd='data/processed/svd_results.csv', n_components=2):
    matches = pd.read_csv(matches_csv)
    matches_numeric = matches.select_dtypes(include=['int64','float64']).dropna()
    if matches_numeric.shape[0] == 0 or matches_numeric.shape[1] == 0:
        print('No numeric data found for PCA/SVD.')
        return
    scaler = StandardScaler()
    matches_scaled = scaler.fit_transform(matches_numeric)
    pca = PCA(n_components=n_components)
    pca_res = pca.fit_transform(matches_scaled)
    pca_df = pd.DataFrame(pca_res, columns=[f'PCA{i+1}' for i in range(n_components)])
    pca_df.to_csv(out_pca, index=False)
    svd = TruncatedSVD(n_components=n_components)
    svd_res = svd.fit_transform(matches_scaled)
    svd_df = pd.DataFrame(svd_res, columns=[f'SVD{i+1}' for i in range(n_components)])
    svd_df.to_csv(out_svd, index=False)
    print('Saved PCA and SVD results to', out_pca, out_svd)

if __name__ == '__main__':
    run_pca_svd('data/processed/cleaned_matches.csv')
