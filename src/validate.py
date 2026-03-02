import pandas as pd
from pathlib import Path

DATA_PATH = Path("data_processed/ar_aging_clean.csv")


def main():
    df = pd.read_csv(DATA_PATH)

    print("Row count:", len(df))
    print("Column count:", len(df.columns))
    print("Missing values per column:")
    print(df.isna().sum())

    # Check for negative numeric values
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        negative_count = (df[col] < 0).sum()
        print(f"{col} negative values:", negative_count)


if __name__ == "__main__":
    main()
