
# Data Dictionary

This project uses a public Accounts Receivable aging dataset and standardizes it to support AR analytics and reporting.

## Core Fields
| Field | Type | Description |
|------|------|-------------|
| reference_date | date | Date the AR aging snapshot is taken |
| debtor_name | string | Entity responsible for payment |
| receivable_type | string | Type of receivable (e.g. tax, fee) |
| total_amount | number | Total outstanding receivable balance |

## Aging Buckets
| Field | Type | Description |
|------|------|-------------|
| current_amount | number | Amount not yet overdue |
| days_1_30 | number | Amount overdue 1–30 days |
| days_31_60 | number | Amount overdue 31–60 days |
| days_61_90 | number | Amount overdue 61–90 days |
| days_90_plus | number | Amount overdue more than 90 days |

## Derived Fields (Analytics)
| Field | Description |
|------|-------------|
| overdue_amount | Sum of all overdue aging buckets |
| overdue_ratio | overdue_amount / total_amount |

## Notes
- Aging buckets represent balances as of the reference date.
- One row represents a snapshot, not individual invoices.
- Dataset is treated as a reporting-level AR export.
