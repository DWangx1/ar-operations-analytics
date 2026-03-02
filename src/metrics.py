import pandas as pd
from pathlib import Path

IN_PATH = Path("data_processed/ar_aging_clean.csv")
OUT_DIR = Path("data_processed")

OUT_TOTAL_BY_YEAR = OUT_DIR / "ar_total_by_year.csv"
OUT_BY_BUCKET_YEAR = OUT_DIR / "ar_by_bucket_year.csv"


def main():
    df = pd.read_csv(IN_PATH)

    # Expected columns from the dataset (after transform.py)
    # These are common in the Canada Open Data file:
    # category_categorie_eng, section_lvl2_niv2_eng, plus many year columns like 2008_2009, 2009_2010, ...
    category_col = "category_categorie_eng"
    bucket_col = "section_lvl2_niv2_eng"

    if category_col not in df.columns or bucket_col not in df.columns:
        raise ValueError(
            f"Missing expected columns. Need '{category_col}' and '{bucket_col}'. "
            f"Found: {list(df.columns)}"
        )

    # Identify fiscal year columns (everything except the two label columns)
    year_cols = [c for c in df.columns if c not in [category_col, bucket_col]]

    # Convert year columns to numeric (safe)
    for c in year_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)

    # Long format (simple melt)
    long_df = df.melt(
        id_vars=[category_col, bucket_col],
        value_vars=year_cols,
        var_name="fiscal_year",
        value_name="amount",
    )

    # Optional: convert 2008_2009 back to 2008/2009 for readability
    long_df["fiscal_year"] = long_df["fiscal_year"].str.replace("_", "/", regex=False)

    # 1) Total AR by fiscal year (sum across categories and buckets)
    total_by_year = (
        long_df.groupby("fiscal_year", as_index=False)["amount"]
        .sum()
        .sort_values("fiscal_year")
    )
    total_by_year = total_by_year.rename(columns={"amount": "total_amount"})

    # 2) AR by bucket + fiscal year (sum across categories)
    by_bucket_year = (
        long_df.groupby(["fiscal_year", bucket_col], as_index=False)["amount"]
        .sum()
        .sort_values(["fiscal_year", bucket_col])
    )
    by_bucket_year = by_bucket_year.rename(
        columns={bucket_col: "aging_bucket", "amount": "total_amount"}
    )

    # Save outputs
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    total_by_year.to_csv(OUT_TOTAL_BY_YEAR, index=False)
    by_bucket_year.to_csv(OUT_BY_BUCKET_YEAR, index=False)

    print("Wrote:", OUT_TOTAL_BY_YEAR)
    print("Wrote:", OUT_BY_BUCKET_YEAR)


if __name__ == "__main__":
    main()
