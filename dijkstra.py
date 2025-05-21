
"""""
===========================================================
grafoLista
exibe o grafo em lista de adjacência
===========================================================
"""""

def grafoLista(grafo):
    print("\n--- Lista de adjacência ---")
    if not grafo:
        print("-----------------------------------------")
        return
    vertices_ordenados = sorted(grafo.keys())
    for vertice in vertices_ordenados:
        conexoes_str = ", ".join([f"{vizinho}({peso})" for vizinho, peso in grafo[vertice]])
        print(f"{vertice}: [{conexoes_str}]")
    print("----------------------------------------")
    
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
        input("Enter para voltar ao menu...")
        return

    todosVertices.add(ver1)
    grafo.setdefault(ver1, [])

    ver2_destino = input(f"Para qual vértice '{ver1}' aponta?\nEscolha: ").upper()
    if not ver2_destino:
        print(f"\nNenhuma conexão adicionada para o vértice {ver1}")
        input("Pressione Enter para continuar...")
        return

    if not rangeTrue(ver2_destino):
        print("Vértice inválido")
        input("Enter para voltar ao menu...")
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
        print(f"Aresta {ver1}->{ver2_destino} com peso {peso} adicionada")
        print(f"Conexão entre os vértices {ver1} e {ver2_destino} em {peso} unidades")
        input("Pressione Enter para voltar ao menu...")

"""""
===========================================================
push e pop
Estruturas de push e pop
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
Algoritimo de Djikstra para calcular a menor distancia
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
menu
menu de opções
===========================================================
"""""

def menu(grafo, todosVertices):
    if not grafo or len(todosVertices) < 2:
        input("não há distancia para calcular")
        return

    print("\n--- Calcular Distância Mínima ---")
    print("Vértices declarados:", ", ".join(sorted(list(todosVertices))))

    while True:
        ver1 = input(f"Digite o vértice de 1 (A-T): ").upper()
        if not rangeTrue(ver1) or ver1 not in todosVertices:
            print("vertice 1 inválido.\ntente novamente...")
            continue
        break
    while True:
        ver2 = input(f"Digite o vértice 2 (A-T): ").upper()
        if not rangeTrue(ver2) or ver2 not in todosVertices:
            print("invalido")
            continue
        if ver2 == ver1:
            print("A distância para o mesmo vertice é 0.")
            input("Pressione Enter para continuar...")
            return
        break

    distancia, caminho = dijkstra(grafo, ver1, ver2)

    if distancia == float('inf'):
        print(f"\nNão há caminho do vértice {ver1} para o vértice {ver2}.")
    else:
        caminho_str = " -> ".join(caminho)
        print(f"\nA distância mínima do vértice {ver1} para o {ver2} é: {distancia} unidades.")
        print(f"Caminho: {caminho_str}")
    input("Pressione Enter para continuar...")


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
        print("1- Adicionar Vértice/Aresta\n2- Calcular Distância Mínima\n3- Sair")
        grafoLista(grafo)  
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            addVertice(grafo, todosVertices)
        elif escolha == '2':
            menu(grafo, todosVertices)
        elif escolha == '3':
            print("saindo...")
            break
        else:
            input("tente novamente...")