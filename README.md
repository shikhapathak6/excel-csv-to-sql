# Excel/CSV to MySQL INSERT IGNORE SQL Generator

This script converts rows from multiple Excel (`.xlsx`) or CSV files into MySQL-compatible `INSERT IGNORE` SQL statements.

## ✅ Features
- Supports `.xlsx` and `.csv`
- Combines multiple files
- Handles NULLs and quotes
- Outputs `INSERT IGNORE` statements

## 🔧 Requirements
- Python 3.7+
- pandas
- openpyxl (for Excel)

Install packages:
```bash
pip install -r requirements.txt
```

## 🚀 Usage
1. Put `.xlsx`/`.csv` files in a folder (e.g., `C:/excel_to_sql`)
2. Edit `generate_sql.py`: set `folder_path` and `table_name`
3. Run:
```bash
python generate_sql.py
```
4. Copy `combined_insert_ignore.sql` into phpMyAdmin and run

