import sqlite3
from pathlib import Path

import pandas as pd

CLEAN_CSV = Path("data_processed/ar_aging_clean.csv")
TOTAL_BY_YEAR_CSV = Path("data_processed/ar_total_by_year.csv")
BY_BUCKET_YEAR_CSV = Path("data_processed/ar_by_bucket_year.csv")

DB_PATH = Path("data_processed/ar.db")


def main():
    # Load csv outputs
    df_clean = pd.read_csv(CLEAN_CSV)
    df_total = pd.read_csv(TOTAL_BY_YEAR_CSV)
    df_bucket = pd.read_csv(BY_BUCKET_YEAR_CSV)

    # Create / overwrite SQLite db
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    # Write tables
    df_clean.to_sql("ar_raw_clean", conn, if_exists="replace", index=False)
    df_total.to_sql("ar_total_by_year", conn, if_exists="replace", index=False)
    df_bucket.to_sql("ar_by_bucket_year", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print("Wrote SQLite DB:", DB_PATH)
    print("Tables: ar_raw_clean, ar_total_by_year, ar_by_bucket_year")


if __name__ == "__main__":
    main()
