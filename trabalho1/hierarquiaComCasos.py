def dfs(grafo,vertice,profundidade,visitado,profundidadeVertices):
        visitado.add(vertice)
        profundidadeVertices[vertice] = profundidade
        for vizinho in grafo[vertice]:
            if vizinho not in visitado:
                dfs(grafo,vizinho,profundidade + 1,visitado,profundidadeVertices)

def criacaoGrafo(grafo,nos,arestas,vertices,linhas,indexLinhas):
    for _ in range(indexLinhas, arestas + 2):
          n1,n2 = linhas[indexLinhas].split()
          grafo[n1].append(n2)
          grafo[n2].append(n1)
          nos.update([n1, n2])
          indexLinhas += 1
    
    while len(nos) < vertices:
          no_gerado = f"isolado{len(nos)}"
          nos.add(no_gerado)
          grafo[no_gerado] = []
   


def hierarquiaDeProfundidade(entrada):
    from collections import defaultdict
    indexLinhas = 0

    def hierarquiaPorCasos(entrada,indexLinhas):
        linhas = entrada.strip().split('\n')
        QuantidadeDeCasos = int(linhas[indexLinhas])
        indexLinhas += 1
        vertices,arestas = map(int, linhas[indexLinhas].split())

        grafo = defaultdict(list)
    
        nos = set()
        visitado = set()

        profundidadeVertices = {}

        for caso in range(QuantidadeDeCasos):
         profundidadeVertices.clear()
         print(f"caso {caso + 1}:")
         indexLinhas += 1

         criacaoGrafo(grafo,nos,vertices,arestas,linhas,indexLinhas)

         for no in nos:
          if no not in visitado:
             dfs(grafo,no,0,visitado,profundidadeVertices)
         print(profundidadeVertices)

    hierarquiaPorCasos(entrada,indexLinhas)


entrada = """2
12 9
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
hierarquiaDeProfundidade(entrada)

