def dfs(grafo, vertice, profundidade, visitado):
    visitado.add(vertice)
    for vizinho in sorted(grafo[vertice], key=int):  # Ordenar para saída em ordem numérica
        if vizinho not in visitado:
            print(f"{'  ' * profundidade}{vertice}-{vizinho} pathR(G,{vizinho})")
            dfs(grafo, vizinho, profundidade + 1, visitado)
        else:
            print(f"{'  ' * profundidade}{vertice}-{vizinho}")

def hierarquiaPorCasos(entrada):
    from collections import defaultdict
    linhas = entrada.strip().split('\n')
    indexLinhas = 0
    QuantidadeDeCasos = int(linhas[indexLinhas])
    indexLinhas += 1

    for caso in range(QuantidadeDeCasos):
        print(f"Caso {caso + 1}:")

        grafo = defaultdict(list)
        nos = set()
        visitado = set()

        vertices, arestas = map(int, linhas[indexLinhas].split())
        indexLinhas += 1

        #preenchimento do grafo por lista de adjacencia
        for _ in range(arestas):
            n1, n2 = linhas[indexLinhas].split()
            indexLinhas += 1
            grafo[n1].append(n2)
            nos.update([n1, n2])

        # Adiciona nós isolados caso faltem
        while len(nos) < vertices:
            no_gerado = f"isolado{len(nos)}"
            nos.add(no_gerado)
            grafo[no_gerado] = []

        # aplicando o busca em profundidade para todos os componentes do grafo
        for no in sorted(nos, key=str): #em ordem numerica
            if no not in visitado:
                dfs(grafo, no, 0, visitado)
                print()      
        
# Teste com a entrada do problema
entrada = """2
13 9
0 1
1 5
5 6
0 4
4 2
2 3
7 8
1 7
10 11
11 8
0 1
1 2
3 4
4 3
5 6
6 8
7 9
9 10"""

hierarquiaPorCasos(entrada)