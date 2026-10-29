from pathlib import Path

from src.cleaner import clean_data
from src.analyzer import analyze_sales
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_PATH = BASE_DIR / "data/raw/sales_data.csv"
CLEAN_PATH = BASE_DIR / "data/cleaned/sales_data_clean.csv"
REPORT_PATH = BASE_DIR / "reports/sales_by_product.png"


def main():
    if not RAW_PATH.is_file():
        raise FileNotFoundError(f"Input CSV not found: {RAW_PATH}")
    CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_clean = clean_data(RAW_PATH, CLEAN_PATH)
    summary = analyze_sales(df_clean)
    fig, ax = plt.subplots()
    ax.bar(summary["product"], summary["sales"])
    ax.set_title("Sales by Product")
    fig.tight_layout()
    fig.savefig(REPORT_PATH)
    plt.close(fig)
    print(f"Report generated: {REPORT_PATH}")


if __name__ == "__main__":
    main()
