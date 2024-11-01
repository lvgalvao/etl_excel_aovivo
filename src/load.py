from pathlib import Path

import pandas as pd


def carregar_o_dataframe_em_um_arquivo_csv(
    df: pd.DataFrame, path_do_arquivo: str, nome_do_arquivo: str
):
    if not Path(path_do_arquivo).exists():
        Path(path_do_arquivo).mkdir(parents=True, exist_ok=True)

    df.to_csv(Path(path_do_arquivo).joinpath(nome_do_arquivo), index=False)
