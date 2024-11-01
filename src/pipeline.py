from extract import extracao_de_arquivos_excel
from load import carregar_o_dataframe_em_um_arquivo_csv
from transform import concatenar_dataframes


def pipeline(path_dos_arquivos: str):
    list_dfs = extracao_de_arquivos_excel(path_dos_arquivos)
    df_concatenado = concatenar_dataframes(list_dfs)
    carregar_o_dataframe_em_um_arquivo_csv(
        df_concatenado, path_de_saida, nome_do_arquivo
    )
    print("Pipeline executada com sucesso!")


path_de_entrada: str = "./data/input"
path_de_saida = "./data/output"
nome_do_arquivo = "concatenado.csv"

print(pipeline(path_de_entrada))
