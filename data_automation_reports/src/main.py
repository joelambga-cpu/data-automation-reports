from src.cleaner import clean_data
from src.analyzer import analyze_sales
import matplotlib.pyplot as plt

RAW_PATH = "data/raw/sales_data.csv"
CLEAN_PATH = "data/cleaned/sales_data_clean.csv"
REPORT_PATH = "reports/sales_by_product.png"


def main():
    df_clean = clean_data(RAW_PATH, CLEAN_PATH)
    summary = analyze_sales(df_clean)

    plt.bar(summary["product"], summary["sales"])
    plt.title("Sales by Product")
    plt.savefig(REPORT_PATH)

    print("Automazione completata con successo!")


if __name__ == "__main__":
    main()
import os

if not os.path.exists(RAW_PATH):
    print(f"ERRORE: {RAW_PATH} non trovato!")
    exit()
