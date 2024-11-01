import pytest

from src.extract import extracao_de_arquivos_excel


def test_extract_no_files(tmpdir):
    """Teste para verificar se o programa informa que não há arquivos para processar e termina."""
    # Criando uma pasta vazia
    empty_folder = tmpdir.mkdir("empty_folder")
    with pytest.raises(ValueError, match="No Excel files found"):
        extracao_de_arquivos_excel(str(empty_folder))


def test_para_verificar_que_a_conversao_foi_feita_corretamente():
    """esse teste vai receber dois dicionarios, passar para dataframes e comparar se são iguais"""
