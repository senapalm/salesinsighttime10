#SalesInsight PY: Pipeline de Análise e Visualização de Dados de Vendas

#FLUXO ATUAL
# RF01 - Gerar/Carregar Dataset
# RF02 - Inspeção Inicial
# RF03 - Limpeza de Dados
# RF13 - Limpeza com Regex
# RF04 - Colunas Derivadas
# RF05 - CÁLCULO DE MÉTRICAS AGREGADAS
# RF07 - Estatísticas NumPy
# RF08- Análises e Visualizações
# RF12 - Exportação CSV/JSON

from src.inheritance import AnalisadorComProjecao
from src.lambdas import processar_coluna

#RF01 - GERANDO O DATASET DE DADOS BRUTOS
from src.data_loader import carregar_ou_gerar_dataset
df_bruto = carregar_ou_gerar_dataset()

#RF02 - INSPEÇÃO INICIAL DOS DADOS BRUTOS
from src.analysis import inspecionar_dados
inspecionar_dados(df_bruto)


#RF03 - LIMPEZA E TRATAMENTO DOS DADOS
from src.cleaning import limpar_dados
df, relatorio_limpeza = limpar_dados(df_bruto)

#RF04 - TRANSFORMAÇÃO - CRIAÇÃO DE COLUNAS DERIVADAS
from src.utils import criar_colunas_derivadas
df = criar_colunas_derivadas(df)

#RF05 - CÁLCULO DE MÉTRICAS AGREGADAS
from src.utils import calcular_metricas
metricas = calcular_metricas(df)

#RF06 - SEGMENTAÇÃO DE CLIENTES POR NÍVEL DE GASTO
from src.utils import segmentar_clientes
segmentar_clientes = segmentar_clientes(df)

#PRÉ-VISUALIZAÇÃO DO DATASET LIMPO E TRANSFORMADO
print("\n=== DATASET LIMPO E TRANSFORMADO ===")
print(df.head())

#RF07 - ESTATISCAS BÁSICAS COM NUMPY
from src.utils import calcular_estatisticas_numpy
stats_numpy = calcular_estatisticas_numpy(df)

#RF08 - GERAÇÃO DE VISUALIZAÇÕES
from src.visualization import gerar_visualizacoes
gerar_visualizacoes(df, metricas)

# LIMPEZA COM EXPRESSÕES REGULARES
from src.utils import limpar_strings_com_regex
df = limpar_strings_com_regex(df)

# VERIFICAR RESULTADO
print(df[["cliente", "cliente_limpo", "cliente_valido"]].head())


#Heranças

analisador = AnalisadorComProjecao(df)

analisador.exibir_resumo()

analisador.projetar_receita()


df = processar_coluna(
    df,
    "receita_total",
    lambda x: "Alto Valor" if x > 5000 else "Valor Normal")



# RF12 - EXPORTAÇÃO DOS RESULTADOS (manter como último)

import os

# Cria a pasta outputs caso não exista
os.makedirs("outputs", exist_ok=True)

print("\n=== EXPORTAÇÃO DE RESULTADOS ===")
print("Pasta de saída: outputs/")

# Exportações

from src.utils import exportar_resultados
exportar_resultados(metricas, segmentar_clientes, stats_numpy)

print("Arquivos serão salvos na pasta outputs/")