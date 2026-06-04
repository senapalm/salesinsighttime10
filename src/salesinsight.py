#SalesInsight PY: Pipeline de Análise e Visualização de Dados de Vendas

#GERANDO O DATASET DE DADOS BRUTOS
from data_loader import gerar_dataset_vendas
df_bruto = gerar_dataset_vendas()

#PRÉ-VISUALIZAÇÃO DOS DADOS BRUTOS
df_bruto.head()

#INSPEÇÃO INICIAL DOS DADOS BRUTOS
from analysis import inspecionar_dados
inspecionar_dados(df_bruto)
df_bruto.head()
