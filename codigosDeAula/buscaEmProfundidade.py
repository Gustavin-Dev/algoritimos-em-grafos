def dfs(grafo, v, visitado, pre, pa, contador, componente, ciclo_flag):
    visitado[v] = True
    pre[v] = contador[0]
    contador[0] += 1
    componente.append(v)

    for vertice in grafo[v]:
        if not visitado[vertice]:
            pa[vertice] = v
            dfs(grafo, vertice, visitado, pre, pa, contador, componente, ciclo_flag)
        else:
            ciclo_flag[0] = True

def dfs_completo(grafo):
    visitado = {v: False for v in grafo}
    pre = {v: -1 for v in grafo}
    pa = {v: -1 for v in grafo}
    contador = [0]
    componentes = []
    ciclo_flag = [False]

    for v in grafo:
        if not visitado[v]:
            pa[v] = v
            componente = []
            dfs(grafo, v, visitado, pre, pa, contador, componente, ciclo_flag)
            componentes.append(componente)

    return pre, pa, componentes, ciclo_flag[0]
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

pre, pa, componentes, tem_ciclo = dfs_completo(grafo)

print("pre:", pre)
print("pa:", pa)
print("componentes conexas:", componentes)
print("tem ciclo?", tem_ciclo)
