Salesinsight.py

Objetivo: Análise de dados de venda para uma empresa

Tecnologias utilizadas: (salesinsight.py/requirements.txt), pandas, numpy, matplotlib, seaborn

Organização de pastas

salesinsight.py
    data
        ## inserir CSV aqui
    outputs
        graficos
        logs
        metricas
    src
        analysis.py
        cleaning.py
        data_loader.py
        salesinsight.py
        utils.py
        visualization.py
    .gitignore
    main.py
    README.md
    requirements.txt

Como executar:

    Recomendado: Google Colab
    Acesse o Colab
    Crie um novo Notebook ou faça upload do arquivo salesinsight.py
    Faça upload do arquivo 'vendas.csv' na barra lateral esquerda
    Crie uma célula de código, digite o comando abaixo e execute:
        !python salesinsight.py

Para máquinas locais (VS Code)
    Instale o Python
    Clone o repositório ou baixe os arquivos em uma pasta
    Abra o terminal e instale as libs:
        pip install pandas numpymatplotlib searborn
    Execute o pipeline com o comando:
        python salesinsight.py
    