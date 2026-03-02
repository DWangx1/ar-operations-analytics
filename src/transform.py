import pandas as pd
from pathlib import Path

RAW_PATH = Path("data_raw/chronoimpots-agingtaxes.csv")
OUT_PATH = Path("data_processed/ar_aging_clean.csv")


def main():
    # Load raw file
    df = pd.read_csv(RAW_PATH)

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_")
    )

    # Basic numeric cleanup (convert all non-text columns if possible)
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    # Save cleaned version
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print("Clean file saved:", OUT_PATH)


if __name__ == "__main__":
    main()
