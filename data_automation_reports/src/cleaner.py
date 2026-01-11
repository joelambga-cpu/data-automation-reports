import pandas as pd


def clean_data(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    # rimuove righe con valori mancanti
    df = df.dropna()

    # normalizza nomi colonne
    df.columns = [c.strip().lower() for c in df.columns]

    # salva CSV pulito
    df.to_csv(output_path, index=False)

    return df

