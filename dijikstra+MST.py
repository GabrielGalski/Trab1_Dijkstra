"""""
===========================================================
grafoLista
cria uma lista de adjacencia do grafo 
===========================================================
"""""

def grafoLista(grafo):
    print("\n--- Lista de adjacência ---")
    if not grafo:
        return
    vertices_ordenados = sorted(grafo.keys())
    for vertice in vertices_ordenados:
        conexoes_str = ", ".join([f"{vizinho}({peso})" for vizinho, peso in grafo[vertice]])
        print(f"{vertice}: [{conexoes_str}]")

"""""
===========================================================
rangeTrue
verifica se o valor indicado está no range
===========================================================
"""""

def rangeTrue(nome_vertice):
    return nome_vertice.upper() in "ABCDEFGHIJKLMNOPQRST"

"""""
===========================================================
addVertice
calcula o vertice das arestas
===========================================================
"""""

def addVertice(grafo, todosVertices):
    ver1 = input(f"Digite o nome do vértice 1 (A-T): ").upper()
    if not rangeTrue(ver1):
        print("vértice inválido")
        return

    todosVertices.add(ver1)
    grafo.setdefault(ver1, [])

    ver2_destino = input(f"Para qual vértice '{ver1}' aponta?\nEscolha: ").upper()
    if not ver2_destino:
        print(f"\nNenhuma conexão adicionada para o vértice {ver1}")
        return

    if not rangeTrue(ver2_destino):
        print("Vértice inválido")
        return

    todosVertices.add(ver2_destino)
    grafo.setdefault(ver2_destino, [])

    while True:
        try:
            peso_str = input(f"Qual o peso da aresta de {ver1} para {ver2_destino}? ")
            peso = int(peso_str)
            if peso <= 0:
                print("digite uma distancia positiva")
                continue
            break
        except ValueError:
            print("digite um número inteiro")

    encontrou_aresta = False
    for i, (viz, p) in enumerate(grafo[ver1]):
        if viz == ver2_destino:
            grafo[ver1][i] = (ver2_destino, peso)
            encontrou_aresta = True
            break

    if not encontrou_aresta:
        grafo[ver1].append((ver2_destino, peso))
        grafo[ver2_destino].append((ver1, peso))
        print(f"\nConexão entre os vértices {ver1} e {ver2_destino} em {peso} unidades")

"""""
===========================================================
push e pop
estruturas de push e pop
===========================================================
"""""

def push(fila, item):
    fila.append(item)
    fila.sort(key=lambda x: x[0])

def pop(fila):
    if not fila:
        raise IndexError("fila vazia")
    return fila.pop(0)

"""""
===========================================================
Dijkstra
algoritimo de Djikstra para calcular a menor distancia
===========================================================
"""""

def dijkstra(grafo, ver1, ver2):
    if ver1 not in grafo or ver2 not in grafo:
        return float('inf'), []

    distancias = {vertice: float('inf') for vertice in grafo}
    predecessores = {vertice: None for vertice in grafo}
    distancias[ver1] = 0
    
    fila_prioridade = [(0, ver1)]

    while fila_prioridade:
        dist_atual, vertice_atual = pop(fila_prioridade)
        if dist_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo.get(vertice_atual, []):
            distancia_candidata = dist_atual + peso
            if distancia_candidata < distancias[vizinho]:
                distancias[vizinho] = distancia_candidata
                predecessores[vizinho] = vertice_atual
                push(fila_prioridade, (distancia_candidata, vizinho))

    caminho = []
    passo_atual = ver2
    if distancias[ver2] == float('inf'):
        return float('inf'), []

    while passo_atual is not None:
        caminho.append(passo_atual)
        if passo_atual == ver1:
            break
        passo_atual = predecessores[passo_atual]
        if passo_atual is None and ver1 not in caminho:
             return float('inf'), []

    return distancias[ver2], caminho[::-1]

"""""
===========================================================
union e find
estruturas union e find para unir 2 arvores
===========================================================
"""""

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  
    return parent[x]


"""
===========================================================
kruskal
algoritmo de Kruskal para calcular a MST
===========================================================
"""

def kruskal(grafo):
    if not grafo:
        print("Não há grafo na memória.")
        return
    arestas = []
    for u in grafo:
        for v, peso in grafo[u]:
            if (v, u, peso) not in arestas and (u, v, peso) not in arestas:
                arestas.append((peso, u, v))
    
    if not arestas:
        print("Não há arestas no grafo.")
        return

    arestas.sort()

    parent = {v: v for v in grafo}
    rank = {v: 0 for v in grafo}
    
    mst_arestas = []
    for peso, u, v in arestas:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_arestas.append((u, v, peso))

    componentes = {}
    for v in grafo:
        root = find(parent, v)
        if root not in componentes:
            componentes[root] = []
        componentes[root].append(v)

    print("\n--- Árvores Geradoras Mínimas ---")
    for i, root in enumerate(componentes, 1):
        vertices = sorted(componentes[root])
        print(f"MST {i} ({', '.join(vertices)})")
        print("Arestas:")
        for u, v, peso in mst_arestas:
            if find(parent, u) == root:
                print(f"  {u} - {v} ({peso})")
    if not componentes:
        print("Não há componentes conexos no grafo.")


"""""
===========================================================
menu
menu de opções
===========================================================
"""""

def menu(grafo, todosVertices):
    if not grafo or len(todosVertices) < 2:
        input("não há distancia para calcular")
        return

    print("\n--- Calcular Distância Mínima ---")
    print("Vértices:", ", ".join(sorted(list(todosVertices))))

    while True:
        ver1 = input(f"Digite o vértice de 1 (A-T): ").upper()
        if not rangeTrue(ver1) or ver1 not in todosVertices:
            print("vertice 1 inválido.\ntente novamente...")
            continue
        break
    while True:
        ver2 = input(f"Digite o vértice 2 (A-T): ").upper()
        if not rangeTrue(ver2) or ver2 not in todosVertices:
            print("distância inválida\n")
            continue
        if ver2 == ver1:
            print("A distância para o mesmo vertice é 0.")
            return
        break

    distancia, caminho = dijkstra(grafo, ver1, ver2)

    if distancia == float('inf'):
        print(f"\nNão há caminho do vértice {ver1} para o vértice {ver2}.")
    else:
        caminhoOrdem = " -> ".join(caminho)
        print(f"\ndistância mínima entre o vértice {ver1} para o {ver2} é: {distancia} unidades")
        print(f"--- {caminhoOrdem} ---\n")

"""""
===========================================================
main
Função principal
===========================================================
"""""

if __name__ == "__main__":
    grafo = {}
    todosVertices = set()
    while True:
        print("========= Algoritmo de Dijkstra =========")
        print("1- Adicionar Vértice/Aresta\n2- Calcular Distância Mínima\n3- Mostrar MST\n4- Sair")
        grafoLista(grafo)
        op = input("\nEscolha uma opção: ")

        match op:
            case '1':
                addVertice(grafo, todosVertices)
            case '2':
                menu(grafo, todosVertices)
            case '3':
                kruskal(grafo)
            case '4':
                print("saindo...")
                break
            case _:
                input("tente novamente...")