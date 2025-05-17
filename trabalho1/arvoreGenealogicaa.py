def contar_familias(entrada):
    linhas = entrada.strip().split('\n')
    QuantidadePessoas, quantidadeRelacoes = map(int, linhas[0].split())

    from collections import defaultdict

    grafo = defaultdict(list)
    pessoas = set()
    visitado = set()
    
    #preenchimento do grafo de acordo com lista de adjacencia
    for i in range(1, quantidadeRelacoes + 1):
        pessoa1, _, pessoa2 = linhas[i].split()
        grafo[pessoa1].append(pessoa2) #grafo nao direcionado, entao adcionamos a adjacencia em ambos os vertices
        grafo[pessoa2].append(pessoa1)
        pessoas.update([pessoa1, pessoa2])
    
    #inclui vertices isolados (sem relação)
    while len(pessoas) < QuantidadePessoas:
        nome_gerado = f"pessoa isolada {len(pessoas)}"
        pessoas.add(nome_gerado)

    #busca em profundidade
    def dfs(vertice):
        visitado.add(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitado:
                dfs(vizinho)

    familias = 0 # equivalente a componentes conexas do grafo, que na modelagem do problema aparece como se fossem as familias

    #aplicando busca em profundidade a fim de achar a quantidade de componentes conexas do grafo(familias)
    for pessoa in pessoas:
        if pessoa not in visitado:
            dfs(pessoa)
            familias += 1

    print(familias)

entrada1 = """8 8
Pedro marido maria
Pedro pai Josias
Josias irmao mangojata
maria mae mangojata
Samuel filho maria
Paulo filho marcos
Samuel tio Ivane
mangojata mae Ivane"""

contar_familias(entrada1)

# Exemplo 2
entrada2 = """9 6
Jose_1 marido maria
Josias marido Liboria
Liboria mae Guapo
Sandra filho maria
Paulo filho Jose_2
Sandra mae Ivanir"""

contar_familias(entrada2)