import numpy as np


class AnalisadorDeVendas:
    """
    Classe base para análise de vendas.
    """

    def __init__(self, df):
        self.df = df

    def calcular_receita_total(self):
        return self.df["receita_total"].sum()

    def calcular_receita_media(self):
        return self.df["receita_total"].mean()

    def exibir_resumo(self):
        print("\n=== RESUMO DE VENDAS ===")
        print(f"Receita total: R$ {self.calcular_receita_total():.2f}")
        print(f"Receita média: R$ {self.calcular_receita_media():.2f}")


class AnalisadorComProjecao(AnalisadorDeVendas):
    """
    Classe filha que herda AnalisadorDeVendas
    e adiciona projeção simples de receita.
    """

    def __init__(self, df, taxa_crescimento=0.05):
        super().__init__(df)
        self.taxa_crescimento = taxa_crescimento

    def projetar_receita(self):
        media = self.calcular_receita_media()

        receita_projetada = media * (1 + self.taxa_crescimento)

        print("\n=== PROJEÇÃO DE RECEITA ===")
        print(f"Receita média atual: R$ {media:.2f}")
        print(f"Receita projetada: R$ {receita_projetada:.2f}")

        return receita_projetada