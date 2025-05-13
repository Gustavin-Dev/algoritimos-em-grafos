def dfs(grafo, vertice, profundidade, visitado, profundidadeVertices):
    visitado.add(vertice)
    profundidadeVertices[vertice] = profundidade
    for vizinho in grafo[vertice]:
        if vizinho not in visitado:
            dfs(grafo, vizinho, profundidade + 1, visitado, profundidadeVertices)

def criacaoGrafo(grafo, nos, arestas, vertices, linhas, indexLinhas):
    #preenche o grafo com oos vertices e arestas com lista de adjacencia
    for _ in range(arestas):
        n1, n2 = linhas[indexLinhas[0]].split()
        grafo[n1].append(n2)
        grafo[n2].append(n1)
        nos.update([n1, n2])
        indexLinhas[0] += 1

    # Adiciona vértices isolados se necessário
    while len(nos) < vertices:
        no_gerado = f"isolado{len(nos)}"
        nos.add(no_gerado)
        grafo[no_gerado] = []

def hierarquiaPorCasos(entrada):
        from collections import defaultdict
        linhas = entrada.strip().split('\n')
        indexLinhas = [0]
        QuantidadeDeCasos = int(linhas[indexLinhas[0]])
        indexLinhas[0] += 1

        for caso in range(QuantidadeDeCasos):
            print(f"caso {caso + 1}:")

            #grafo e estruturas para cada caso
            grafo = defaultdict(list)
            nos = set()
            visitado = set()
            profundidadeVertices = {}

            # Lê quantidade de vertices e arestas de acordo com a entrada
            vertices, arestas = map(int, linhas[indexLinhas[0]].split())
            indexLinhas[0] += 1

            criacaoGrafo(grafo, nos, arestas, vertices, linhas, indexLinhas)

            # Executa DFS para todos os componentes
            for no in nos:
                if no not in visitado:
                    dfs(grafo, no, 0, visitado, profundidadeVertices)

            print(profundidadeVertices)

entrada = """2
6 4
0 1
1 2
3 4
4 3
0 1
0 2
0 3"""

hierarquiaPorCasos(entrada)

