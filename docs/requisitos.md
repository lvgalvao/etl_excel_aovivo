## Requisitos

Esses são os requisitos de negócio do projeto.

Requisitos de extração de dados

1. Ler os arquivos em Excel
Criar um método para ler os arquivos em Excel e retornar uma Lista de DataFrames.
args: path (str)
- Ler somente arquivos .xlsx
- A pasta de entrada de dados é: ./data/input
- Caso não tenha arquivos na pasta, o programa deve informar que não há arquivos para processar e terminar.
- Fazer testes para verificar que os dados estão sendo lidos corretamente.

Requisitos de transformação de dados
Criar um método que vai receber uma lista de DataFrames e retornar um único Dataframe.
args: list_dfs (list)
1. Concatenar os Dataframes arquivos em um único arquivo Dataframe

Requisitos de carga de dados
Criar um método que vai receber um Dataframe e salvar em um arquivo CSV.
args: df (DataFrame), path (str), nome_arquivo (str)
