#FUNÇÃO DE TRANSFORMAÇÃO - CRIAÇÃO DE COLUNAS DERIVADAS
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

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
