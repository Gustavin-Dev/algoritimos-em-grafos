def dfs(grafo,vertice,verticesVisitados,componente,ciclo):
    verticesVisitados.add(vertice)
    componente.append(vertice)
    for verticeAdjacenetes in grafo[vertice]:
        if verticeAdjacenetes not in verticesVisitados:
            dfs(grafo,verticeAdjacenetes,verticesVisitados,componente,ciclo)
        else:
            ciclo[0] = True

def AplicarDfs(grafo):
    verticesVisitados = set()
    componentes = []
    ciclo = [False]
    for vertices in range(len(grafo)):
        if vertices not in verticesVisitados:
            componente = []
            dfs(grafo,vertices,verticesVisitados,componente,ciclo)
            componentes.append(componente)
    
    print(f"O grafo:{grafo} tem as seguintes componentes conexas: {componentes}")
    if(ciclo[0]):
        print("E também contem ao menos um ciclo dentro dele")

grafo = {
    0: [1,2],
    1: [0,2,3,4],
    2: [0,1,3],
    3: [1,2],
    4: [1],
    5: [6],
    6: [5,7],
    7: [6],
    8: []
}

AplicarDfs(grafo)