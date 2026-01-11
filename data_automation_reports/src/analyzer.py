import pandas as pd


def analyze_sales(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("product")["sales"]
        .sum()
        .reset_index()
        .sort_values(by="sales", ascending=False)
    )
    return summary
