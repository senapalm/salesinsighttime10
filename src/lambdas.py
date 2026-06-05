def processar_coluna(df, coluna, funcao_transformacao):
    """
    Aplica uma função recebida como parâmetro a uma coluna do DataFrame.
    Demonstra função de ordem superior (higher-order function).
    """

    df[f"{coluna}_transformado"] = df[coluna].apply(
        funcao_transformacao
    )

    print(
        f"Coluna '{coluna}_transformado' criada com sucesso."
    )

    return df