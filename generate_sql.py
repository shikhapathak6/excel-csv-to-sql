import pandas as pd
import os

# Folder where all Excel and CSV files are stored
folder_path = "C:/excel_csv_to_sql/files"  # Change as needed
table_name = "your_table_name"

# Get all Excel and CSV files
data_files = [f for f in os.listdir(folder_path) if f.endswith((".xlsx", ".csv"))]

sql_statements = []

for file in data_files:
    file_path = os.path.join(folder_path, file)
    print(f"Processing: {file_path}")

    # Read the file based on its extension
    if file.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        columns = ", ".join([f"`{col}`" for col in df.columns])
        values = ", ".join(
            [
                f"'{str(val).replace("'", "''")}'" if pd.notnull(val) else "NULL"
                for val in row
            ]
        )
        insert_statement = (
            f"INSERT IGNORE INTO `{table_name}` ({columns}) VALUES ({values});"
        )
        sql_statements.append(insert_statement)

# Write to .sql file
output_file = os.path.join(folder_path, "combined_insert_ignore.sql")
with open(output_file, "w", encoding="utf-8") as f:
    for stmt in sql_statements:
        f.write(stmt + "\n")

print(f"✅ Combined SQL written to: {output_file}")
