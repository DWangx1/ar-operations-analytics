# Dashboard Notes

This project can be visualized in Power BI using the processed outputs in `data_processed/`.

## Recommended Visuals

### 1. Total AR by Fiscal Year
- Chart type: line chart or column chart
- Table: `ar_total_by_year`
- X-axis: `fiscal_year`
- Y-axis: `total_amount`

### 2. AR by Aging Bucket
- Chart type: stacked column chart
- Table: `ar_by_bucket_year`
- X-axis: `fiscal_year`
- Legend: `aging_bucket`
- Y-axis: `total_amount`

### 3. Aging Bucket Share
- Chart type: stacked 100% column chart
- Table/view: `v_ar_bucket_share`
- X-axis: `fiscal_year`
- Legend: `aging_bucket`
- Y-axis: `share_of_year_total`

## Suggested Dashboard Layout
- Top: KPI card for latest total AR
- Middle: Total AR trend by fiscal year
- Bottom: AR aging distribution by fiscal year

## Purpose
The dashboard is intended to support reporting on:
- overall AR trend
- aging composition over time
- concentration of overdue balances
