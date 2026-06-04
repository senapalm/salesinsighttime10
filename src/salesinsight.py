#SalesInsight PY: Pipeline de Análise e Visualização de Dados de Vendas

#FLUXO ATUAL
# RF01 - Gerar/Carregar Dataset
# RF02 - Inspeção Inicial
# RF03 - Limpeza de Dados
# RF13 - Limpeza com Regex
# RF04 - Colunas Derivadas
# RF07 - Estatísticas NumPy
# RF08-RF11 - Análises e Visualizações
# RF12 - Exportação CSV/JSON

from herança import AnalisadorComProjecao

#GERANDO O DATASET DE DADOS BRUTOS
from data_loader import gerar_dataset_vendas
df_bruto = gerar_dataset_vendas()

#PRÉ-VISUALIZAÇÃO DOS DADOS BRUTOS
df_bruto.head()

#INSPEÇÃO INICIAL DOS DADOS BRUTOS
from analysis import inspecionar_dados
inspecionar_dados(df_bruto)
df_bruto.head()

#ESTATISCAS BÁSICAS
from utils import calcular_estatisticas_numpy
calcular_estatisticas_numpy(df_bruto)

# LIMPEZA COM EXPRESSÕES REGULARES
from utils import limpar_strings_com_regex
df_bruto = limpar_strings_com_regex(df_bruto)

# VERIFICAR RESULTADO
print(df_bruto[["cliente", "cliente_limpo", "cliente_valido"]].head())


# RF12 - EXPORTAÇÃO DOS RESULTADOS (manter como último)

import os

# Cria a pasta outputs caso não exista
os.makedirs("outputs", exist_ok=True)

print("\n=== EXPORTAÇÃO DE RESULTADOS ===")
print("Pasta de saída: outputs/")

# Exportações (descomente quando as funções e dados existirem)

# exportar_csv(metricas)
# exportar_json(stats_numpy)

print("Arquivos serão salvos na pasta outputs/")


#Heranças

analisador = AnalisadorComProjecao(df_bruto)

analisador.exibir_resumo()

analisador.projetar_receita()