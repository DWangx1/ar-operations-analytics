# AR Operations Analytics

## Overview
End-to-end Accounts Receivable (AR) analytics project using public invoice and payment data.  
The goal is to replicate a real-world monthly operations reporting workflow, including AR aging, customer payment behavior, and cash receipts analysis.

## Business Problem
Finance teams often rely on manual Excel processes to answer:
- How much AR is overdue?
- Which customers pay late?
- How are cash receipts trending?

This project demonstrates a structured, repeatable analytics pipeline to support these questions.


## Dataset
Source: Canada Open Data – Aging of Taxes and Other Accounts Receivable

The dataset simulates real-world accounts receivable aging data and is used as a stand-in for invoice and payment exports commonly received by finance teams.

The raw file is stored as:
- data_raw/chronoimpots-agingtaxes.csv

No confidential or client data is used.


## Pipeline
1. Ingest raw invoice and payment files  
2. Standardize and validate data  
3. Join invoices and payments  
4. Compute AR metrics  
5. Export analytics tables for reporting and dashboards

## Key Outputs
- AR aging snapshot
- Customer payment trends
- Cash receipts summaries
- Optional Power BI dashboard

## Repo Structure
- `data_raw/` raw input files  
- `data_processed/` cleaned outputs (excluded from git)  
- `docs/` documentation  
- `src/` analytics scripts  
- `sql/` SQL models  
- `reports/` dashboard notes

## Tech Stack
Python (pandas), SQL (SQLite), Excel, Power BI

## How to Run
1. Put the raw dataset in `data_raw/chronoimpots-agingtaxes.csv`
2. Run:
   - `python src/transform.py`
   - `python src/metrics.py`

(Optional) Run validation:
- `python src/validate.py`

## Outputs
Generated in `data_processed/`:
- `ar_aging_clean.csv` (cleaned version of the raw dataset)
- `ar_total_by_year.csv` (total AR by fiscal year)
- `ar_by_bucket_year.csv` (AR totals by aging bucket and fiscal year)

## Documentation


Field definitions and assumptions are in `docs/data_dictionary.md`

## License
MIT
