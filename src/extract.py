from pathlib import Path
from pandas import DataFrame, read_excel


def extracao_de_arquivos_excel(path_dos_arquivos: str) -> list[DataFrame]:
    """
    Essa função vai extrair os arquivos excel da pasta de entrada e retornar uma lista de dataframes.

    args:
        path_dos_arquivos: str

    returns:
        list[DataFrame]
    """

    # Lista todos os arquivos na pasta de entrada que possuem o final .xlsx

    all_files: list[Path] = list(Path(path_dos_arquivos).glob("*.xlsx"))

    if len(all_files) == 0:
        raise ValueError("No Excel files found")

    list_dfs = []

    for files in all_files:
        list_dfs.append(read_excel(files))

    return list_dfs
