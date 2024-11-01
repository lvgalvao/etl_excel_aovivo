import pandas as pd


def concatenar_dataframes(list_dfs: list[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(list_dfs, ignore_index=True)
