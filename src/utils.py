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