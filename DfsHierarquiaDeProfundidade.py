def hierarquiaDeProfundidade(entrada):
    from collections import defaultdict
    linhas = entrada.strip().split('\n')
    print(linhas)
    casos = linhas[0]
    vertices,arestas = map(int, linhas[1].split())

    grafo = defaultdict(list)
    nos = set()

    for i in range(2, arestas + 1):
        n1,n2 = linhas[i].split()
        grafo[n1].append(n2)
        grafo[n2].append(n1)
        nos.update([n1, n2])
    
    while len(nos) < vertices:
        no_gerado = f"isolado{len(nos)}"
        nos.add(no_gerado)
    
    visitado = set()

    def dfs(pessoa):
        visitado.add(pessoa)
        for vizinho in grafo[pessoa]:
            if vizinho not in visitado:
                dfs(vizinho)

    for no in nos:
        if no not in visitado:
            dfs(no)
            
    print(grafo)

entrada = """2
12 9
0 1
1 5
5 6
0 4
4 2
2 3
7 8
1 7"""
hierarquiaDeProfundidade(entrada)

