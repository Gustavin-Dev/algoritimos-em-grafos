def contar_familias(entrada):
    linhas = entrada.strip().split('\n')
    m, n = map(int, linhas[0].split())


    from collections import defaultdict

    grafo = defaultdict(list)
    pessoas = set()

    for i in range(1, n + 1):
        p1, _, p2 = linhas[i].split()
        grafo[p1].append(p2)
        grafo[p2].append(p1)
        pessoas.update([p1, p2])

    visitado = set()

    def dfs(pessoa):
        visitado.add(pessoa)
        for vizinho in grafo[pessoa]:
            if vizinho not in visitado:
                dfs(vizinho)

    familias = 0
    for pessoa in pessoas:
        if pessoa not in visitado:
            dfs(pessoa)
            familias += 1

    return familias

# Exemplo 1
entrada1 = """8 8
Pedro marido Maria
Pedro pai Josias
Josias irmao Mangojata
Maria mae Mangojata
Samuel filho Maria
Paulo filho Marcos
Samuel tio Ivane
Mangojata mae Ivane"""

print(contar_familias(entrada1))

# Exemplo 2
entrada2 = """9 6
Jose_1 marido Maria
Josias marido Liboria
Liboria mae Guapo
Sandra filho Maria
Paulo filho Jose_2
Sandra mae Ivanir"""

print(contar_familias(entrada2))