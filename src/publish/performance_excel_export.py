import os
import sys
import pandas as pd

# Add src to sys.path for direct script execution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculate.performance_calculator import prepare_performance_summary

def export_performance_by_category_excel(output_path):
    df = prepare_performance_summary()
    categories = df['Category'].unique()
    numeric_cols = ['Last', '1d', 'Mtd', 'Ytd', '1y', '2y', '5y', '10y', '20y']

    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        for category in categories:
            df_cat = df[df['Category'] == category].copy()
            df_cat = df_cat.rename(columns={'Company': 'Company Names'})
            df_cat = df_cat.drop(columns=['Category'])
            sheet_name = str(category)[:31]
            df_cat.to_excel(writer, sheet_name=sheet_name, index=False)

            # Apply number format to numeric columns
            worksheet = writer.sheets[sheet_name]
            workbook = writer.book
            num_format = workbook.add_format({'num_format': '0.0'})

            for idx, col in enumerate(df_cat.columns):
                if col in numeric_cols:
                    # +1 because Excel columns are 1-indexed (A=0, B=1, ...)
                    worksheet.set_column(idx, idx, 12, num_format)
                else:
                    worksheet.set_column(idx, idx, 25)  # Wider for company names

    print(f"Excel file with category tabs saved to: {output_path}")

if __name__ == "__main__":
    output_dir = r"D:\Projects\MarketNiti\data\excel"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "Asset_performance.xlsx")
    export_performance_by_category_excel(output_path)