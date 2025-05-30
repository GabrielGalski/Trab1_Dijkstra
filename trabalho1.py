"""
===========================================================
grafoLista
cria uma lista de adjacência do grafo 
===========================================================
"""
def grafoLista(grafo):
    print("\n--- Lista de adjacência ---")
    if not grafo:
        return
    vertices_ordenados = sorted(grafo.keys())
    for vertice in vertices_ordenados:
        conexoes_str = ", ".join([f"{vizinho}({peso})" for vizinho, peso in grafo[vertice]])
        print(f"{vertice}: [{conexoes_str}]")

"""
===========================================================
rangeTrue
verifica se o valor indicado está no range
===========================================================
"""
def rangeTrue(nome_vertice):
    return nome_vertice.upper() in "ABCDEFGHIJKLMNOPQRST"

"""
===========================================================
push e pop
estruturas de push e pop
===========================================================
"""
def push(fila, item):
    fila.append(item)
    fila.sort(key=lambda x: x[0])

def pop(fila):
    if not fila:
        raise IndexError("fila vazia")
    return fila.pop(0)  

"""
===========================================================
Dijkstra
algoritmo de Dijkstra para calcular a menor distância
===========================================================
"""
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

"""
===========================================================
menu
menu de opções
===========================================================
"""
def menu(grafo, todosVertices):
    if not grafo or len(todosVertices) < 2:
        input("não há distância para calcular")
        return

    print("\n--- Calcular Distância Mínima ---")
    print("Vértices declarados:", ", ".join(sorted(list(todosVertices))))

    while True:
        ver1 = input(f"Digite o vértice de 1 (A-T): ").upper()
        if not rangeTrue(ver1) or ver1 not in todosVertices:
            print("vértice 1 inválido.\ntente novamente...")
            continue
        break
    while True:
        ver2 = input(f"Digite o vértice 2 (A-T): ").upper()
        if not rangeTrue(ver2) or ver2 not in todosVertices:
            print("distância inválida\n")
            continue
        if ver2 == ver1:
            print("A distância para o mesmo vértice é 0.")
            return
        break

    distancia, caminho = dijkstra(grafo, ver1, ver2)

    if distancia == float('inf'):
        print(f"\nNão há caminho do vértice {ver1} para o vértice {ver2}.")
    else:
        caminhoOrdem = " -> ".join(caminho)
        print(f"\ndistância mínima entre o vértice {ver1} para o {ver2} é: {distancia} unidades")
        print(f"--- {caminhoOrdem} ---\n")

"""
===========================================================
main
Função principal
===========================================================
"""
if __name__ == "__main__":
    grafo = {'A': [('B',4),('C',2)],'B': [('A',4),('C',1),('D',5)],'C': [('A',2),('B',1),('D',8),('E', 10)],'D': [('B',5),('C',8),('E',2)],'E': [('C',10),('D',2)],}
    todosVertices = set(grafo.keys())

    while True:
        print("1- Calcular Distância Mínima\n2- Sair")
        grafoLista(grafo)  
        op = input("\nEscolha uma opção: ")

        match op:
            case '1':
                menu(grafo, todosVertices)
            case '2':
                print("saindo...")
                break
            case _:
                input("tente novamente...")
