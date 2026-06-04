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
import re

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