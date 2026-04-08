-- Views for ar.db
-- After running: python src/load_sqlite.py

-- 1) Total AR by year (already a table, but view keeps a consistent "reporting layer")
CREATE VIEW IF NOT EXISTS v_ar_total_by_year AS
SELECT
  fiscal_year,
  total_amount
FROM ar_total_by_year
ORDER BY fiscal_year;

-- 2) Share of total by bucket within each year
CREATE VIEW IF NOT EXISTS v_ar_bucket_share AS
SELECT
  b.fiscal_year,
  b.aging_bucket,
  b.total_amount,
  (b.total_amount * 1.0) / NULLIF(t.total_amount, 0) AS share_of_year_total
FROM ar_by_bucket_year b
JOIN ar_total_by_year t
  ON b.fiscal_year = t.fiscal_year
ORDER BY b.fiscal_year, b.aging_bucket;
