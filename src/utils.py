#FUNÇÃO DE TRANSFORMAÇÃO - CRIAÇÃO DE COLUNAS DERIVADAS
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt
import os
import json
import re

def criar_colunas_derivadas(df):
    """Cria colunas calculadas e derivadas a partir do dataset limpo."""

    # Receita total por linha de venda
    df["receita_total"] = df["quantidade"] * df["preco_unitario"]

    # Extração de componentes de data
    df["mes"] = df["data_venda"].dt.month
    df["mes_nome"] = df["data_venda"].dt.strftime("%B")  # nome do mês
    df["trimestre"] = df["data_venda"].dt.quarter.apply(lambda q: f"Q{q}")
    df["ano"] = df["data_venda"].dt.year

    # Classificação da receita por item com numpy.select (transformação condicional vetorizada)
    condicoes = [
        df["receita_total"] < 500,
        (df["receita_total"] >= 500) & (df["receita_total"] < 5000),
        df["receita_total"] >= 5000
    ]
    classificacoes = ["Baixo Valor", "Médio Valor", "Alto Valor"]
    df["faixa_receita_item"] = np.select(condicoes, classificacoes, default="Não Classificado")

    print("\n=== COLUNAS DERIVADAS CRIADAS ===")
    print(df[["data_venda", "receita_total", "mes", "trimestre", "faixa_receita_item"]].head())

    return df


#FUNÇÃO DE CRIAÇÃO DE MÉTRICAS AGREGADAS
def calcular_metricas(df):
    """Calcula e retorna métricas agregadas do dataset."""
    metricas = {}

    # Receita por mês
    por_mes = df.groupby("mes").agg(
        receita_total=("receita_total", "sum"),
        quantidade=("quantidade", "sum"),
        n_vendas=("id_venda", "count")
    ).reset_index().sort_values("mes")
    metricas["por_mes"] = por_mes

    # Top 5 produtos por receita
    top_produtos = df.groupby("produto")["receita_total"].sum()\
                     .sort_values(ascending=False).head(5).reset_index()
    metricas["top_produtos"] = top_produtos

    # Receita por categoria
    por_categoria = df.groupby("categoria")["receita_total"].sum().reset_index()
    metricas["por_categoria"] = por_categoria

    # Receita por região
    por_regiao = df.groupby("regiao").agg(
        receita_total=("receita_total", "sum"),
        media_ticket=("receita_total", "mean")
    ).reset_index().sort_values("receita_total", ascending=False)
    metricas["por_regiao"] = por_regiao

    # Exibição
    for nome, tabela in metricas.items():
        print("\n=== MÉTRICAS AGREGADAS ===")
        print(f"\n=== {nome.upper().replace('_', ' ')} ===")
        print(tabela.to_string(index=False))

    return metricas


#FUNÇÃO DE SEGMENTAÇÃO DE CLIENTES

def segmentar_clientes(df):
    """Segmenta clientes pelo total gasto usando groupby e lambda."""

    clientes = df.groupby("cliente")["receita_total"].sum().reset_index()
    clientes.columns = ["cliente", "total_gasto"]

    # Classificação usando função lambda com condicionais
    clientes["segmento"] = clientes["total_gasto"].apply(
        lambda gasto: "Ouro" if gasto > 15000
                      else ("Prata" if gasto >= 5000 else "Bronze")
    )

    clientes = clientes.sort_values("total_gasto", ascending=False)

    print("\n=== SEGMENTAÇÃO DE CLIENTES ===")
    print(clientes.head(10).to_string(index=False))
    print(f"\nDistribuição de segmentos:\n{clientes['segmento'].value_counts()}")

    return clientes


def calcular_estatisticas_numpy(df):
    """Usa NumPy para calcular estatísticas sobre as receitas."""
    print("\n=== ESTATÍSTICAS COM NUMPY ===")

#condicional criada, caso ainda não tenha sido implementada a Reeita Total
    if "receita_total" not in df.columns:
        print("Erro: a coluna 'receita_total' não existe no DataFrame.")
        return None

    # Converte para array NumPy
    receitas = df["receita_total"].dropna().to_numpy()

    media = np.mean(receitas)
    mediana = np.median(receitas)
    desvio_padrao = np.std(receitas)
    total = np.sum(receitas)
    p25 = np.percentile(receitas, 25)
    p75 = np.percentile(receitas, 75)

    print(f"Receita média por venda:    R$ {media:.2f}")
    print(f"Receita mediana por venda:  R$ {mediana:.2f}")
    print(f"Desvio padrão:              R$ {desvio_padrao:.2f}")
    print(f"Receita total:              R$ {total:.2f}")
    print(f"Percentil 25 (Q1):          R$ {p25:.2f}")
    print(f"Percentil 75 (Q3):          R$ {p75:.2f}")

    # Broadcasting: normalização
    receitas_normalizadas = (
        (receitas - receitas.min()) /
        (receitas.max() - receitas.min())
    )

    print(
        f"\nReceitas normalizadas (primeiros 5): "
        f"{receitas_normalizadas[:5].round(4)}"
    )

    # Operação vetorizada
    acima_da_media = receitas[receitas > media]

    print(
        f"\nVendas acima da média: "
        f"{len(acima_da_media)} de {len(receitas)}"
    )

    return {
        "media": media,
        "mediana": mediana,
        "desvio_padrao": desvio_padrao,
        "total": total,
        "percentil_25": p25,
        "percentil_75": p75
    }


#LIMPEZA DE STRINGS


def limpar_strings_com_regex(df):
    """
    Usa expressões regulares para limpeza e validação de dados textuais.

    - Remove caracteres especiais da coluna 'cliente'
    - Valida se o cliente segue o padrão 'Cliente_XXX'
    """

    print("\n=== LIMPEZA COM REGEX ===")

    # Remove caracteres não alfanuméricos
    df["cliente_limpo"] = df["cliente"].apply(
        lambda s: re.sub(r"[^a-zA-Z0-9_ ]", "", str(s)).strip()
    )

    # Valida padrão Cliente_001, Cliente_002, etc.
    padrao_cliente = re.compile(r"^Cliente_\d{3}$")

    df["cliente_valido"] = df["cliente_limpo"].apply(
        lambda s: bool(padrao_cliente.match(s))
    )

    n_invalidos = (~df["cliente_valido"]).sum()

    print(f"Clientes com formato inválido encontrados: {n_invalidos}")
    print(
        f"Amostra de clientes limpos: "
        f"{df['cliente_limpo'].head(5).tolist()}"
    )

    return df

#EXPORTAÇÔES 

def exportar_resultados(metricas, clientes, stats_numpy):
    """
    Exporta resultados do projeto em CSV e JSON.
    Também realiza a leitura dos arquivos exportados para validação.
    """

    if stats_numpy is None:
        print("Nenhuma estatística disponível para exportação.")
        return


    print("\n=== EXPORTAÇÃO DE RESULTADOS ===")

    # Cria a pasta de saída caso não exista
    os.makedirs("outputs", exist_ok=True)


    # EXPORTAÇÃO CSV - MÉTRICAS POR MÊS


    caminho_csv = "outputs/metricas_por_mes.csv"

    metricas["por_mes"].to_csv(
        caminho_csv,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"CSV exportado: {caminho_csv}")

    # Leitura de validação
    df_metricas_lido = pd.read_csv(caminho_csv)

    print("\nPrimeiras linhas do CSV de métricas:")
    print(df_metricas_lido.head())

    # EXPORTAÇÃO CSV - SEGMENTAÇÃO DE CLIENTES


    caminho_clientes = "outputs/segmentacao_clientes.csv"

    clientes.to_csv(
        caminho_clientes,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"\nCSV exportado: {caminho_clientes}")

    # Leitura de validação
    df_clientes_lido = pd.read_csv(caminho_clientes)

    print("\nPrimeiras linhas do CSV de clientes:")
    print(df_clientes_lido.head())


    # EXPORTAÇÃO JSON - ESTATÍSTICAS GERAIS


    caminho_json = "outputs/estatisticas_gerais.json"

    stats_serializaveis = {
        chave: round(float(valor), 2)
        for chave, valor in stats_numpy.items()
    }

    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(
            stats_serializaveis,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    print(f"\nJSON exportado: {caminho_json}")

    # Leitura de validação
    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)

    print("\nConteúdo do JSON exportado:")
    print(json.dumps(dados_lidos, indent=4, ensure_ascii=False))

    print("\nExportação concluída com sucesso.")
