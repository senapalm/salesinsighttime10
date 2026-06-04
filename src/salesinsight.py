#SalesInsight PY: Pipeline de Análise e Visualização de Dados de Vendas

#GERANDO O DATASET DE DADOS BRUTOS
from data_loader import gerar_dataset_vendas
df_bruto = gerar_dataset_vendas()

#PRÉ-VISUALIZAÇÃO DOS DADOS BRUTOS
df_bruto.head()

#INSPEÇÃO INICIAL DOS DADOS BRUTOS
from analysis import inspecionar_dados
inspecionar_dados(df_bruto)

#LIMPEZA E TRATAMENTO DOS DADOS
from cleaning import limpar_dados
df, relatorio_limpeza = limpar_dados(df_bruto)

#TRANSFORMAÇÃO - CRIAÇÃO DE COLUNAS DERIVADAS
from utils import criar_colunas_derivadas
df = criar_colunas_derivadas(df)
