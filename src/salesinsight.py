#SalesInsight PY: Pipeline de Análise e Visualização de Dados de Vendas

#GERANDO O DATASET DE DADOS BRUTOS
from data_loader import gerar_dataset_vendas
df_bruto = gerar_dataset_vendas()

#INSPEÇÃO INICIAL DOS DADOS BRUTOS
from analysis import inspecionar_dados
inspecionar_dados(df_bruto)

#LIMPEZA E TRATAMENTO DOS DADOS
from cleaning import limpar_dados
df, relatorio_limpeza = limpar_dados(df_bruto)

#TRANSFORMAÇÃO - CRIAÇÃO DE COLUNAS DERIVADAS
from utils import criar_colunas_derivadas
df_limpo = criar_colunas_derivadas(df)

#PRÉ-VISUALIZAÇÃO DO DATASET LIMPO E TRANSFORMADO
print("\n=== DATASET LIMPO E TRANSFORMADO ===")
print(df_limpo.head())

#CÁLCULO DE MÉTRICAS AGREGADAS
from utils import calcular_metricas
metricas = calcular_metricas(df_limpo)