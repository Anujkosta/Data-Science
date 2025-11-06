"""extract.py
Unzip dataset archive and create a data/raw folder.
Usage: python src/extract.py --zip path/to/archive.zip --out data/raw
"""
import zipfile
import argparse
from pathlib import Path

def extract(zip_path, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(out_dir)
    print(f"Extracted {zip_path} -> {out_dir}")

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--zip', required=True, help='Path to archive zip')
    p.add_argument('--out', default='data/raw', help='Output folder')
    args = p.parse_args()
    extract(args.zip, args.out)
