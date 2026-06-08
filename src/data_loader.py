#FUNÇÃO PARA GERAR O DATASET DE DADOS BRUTOS

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def gerar_dataset_vendas(n_registros=200, seed=42):
    """Gera um dataset sintético de vendas com dados intencionalmente sujos."""
    random.seed(seed)
    np.random.seed(seed)

    produtos = ["Notebook", "Smartphone", "Tablet", "Monitor", "Teclado", "Mouse", "Headset"]
    categorias = {"Notebook": "Computadores", "Smartphone": "Celulares", "Tablet": "Celulares",
                  "Monitor": "Computadores", "Teclado": "Periféricos", "Mouse": "Periféricos",
                  "Headset": "Periféricos"}
    regioes = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
    clientes = [f"Cliente_{i:03d}" for i in range(1, 51)]

    data_inicio = datetime(2024, 1, 1)
    dados = []

    for i in range(n_registros):
        produto = random.choice(produtos)
        quantidade = random.randint(1, 10)
        preco_base = {"Notebook": 3500, "Smartphone": 2200, "Tablet": 1800,
                      "Monitor": 1200, "Teclado": 250, "Mouse": 120, "Headset": 350}[produto]
        preco = round(preco_base * random.uniform(0.85, 1.15), 2)
        data = data_inicio + timedelta(days=random.randint(0, 364))

        # Inserindo dados intencionalmente sujos para limpeza
        if random.random() < 0.05:
            quantidade = None          # valor nulo
        if random.random() < 0.04:
            preco = None               # valor nulo
        if random.random() < 0.03:
            produto = "  " + produto   # espaço extra (string suja)

        dados.append({
            "id_venda": i + 1,
            "data_venda": data.strftime("%Y-%m-%d") if random.random() > 0.02 else "DATA INVÁLIDA",
            "cliente": random.choice(clientes),
            "produto": produto,
            "categoria": categorias.get(produto.strip(), "Outros"),
            "regiao": random.choice(regioes),
            "quantidade": quantidade,
            "preco_unitario": preco
        })

    return pd.DataFrame(dados)

# Gerar e salvar
# df_bruto = gerar_dataset_vendas()
# df_bruto.to_csv("vendas.csv", index=False)
# print(f"Dataset gerado com {len(df_bruto)} registros.")
# print(df_bruto.head())

def carregar_dataset(caminho_csv="vendas.csv"):
    """Carrega o dataset de vendas a partir de um arquivo CSV."""
    
    df = pd.read_csv(caminho_csv)
    print(f"Dataset carregado com {len(df)} registros.")
    return df

def carregar_ou_gerar_dataset(caminho_csv="vendas.csv"):
    """Carrega o dataset de vendas se existir, caso contrário gera um novo."""
    
    if os.path.exists(caminho_csv):
        print(f"Arquivo {caminho_csv} encontrado. Carregando dataset...")
        return carregar_dataset(caminho_csv)
    
    else:
        print(f"Arquivo {caminho_csv} não encontrado. Gerando novo dataset...")
        
        df_bruto = gerar_dataset_vendas()
        df_bruto.to_csv(caminho_csv, index=False)
        
        print(f"Dataset gerado e salvo em {caminho_csv}.")
        
        return df_bruto