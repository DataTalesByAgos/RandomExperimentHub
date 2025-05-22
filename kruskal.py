"""
Implementación del algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima (MST)
de un grafo no dirigido, ponderado y conexo.

Objetivo:
---------
Dado un conjunto de nodos y aristas con pesos (costos), el algoritmo selecciona un subconjunto
de aristas tal que:
    - Conectan todos los nodos (es decir, forman un árbol).
    - El costo total de las aristas seleccionadas es mínimo.
    - No se forman ciclos.

Estrategia:
-----------
1. Se ordenan todas las aristas por peso ascendente.
2. Se recorren en orden, y se agrega cada arista si conecta dos componentes distintos.
3. Para evitar ciclos, se utiliza la estructura Union-Find (Disjoint Set Union) con compresión de caminos.
"""

# Estructura Union-Find para representar componentes disjuntos
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        # Devuelve el representante del conjunto al que pertenece x, con compresión de caminos
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Une los conjuntos de x e y, si no están en el mismo conjunto
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True  # Se unieron correctamente (no había ciclo)
        return False  # Ya estaban conectados (formaría ciclo)

# Lista de aristas en el formato: (peso, nodo_origen, nodo_destino)
edges = [
    (1, 0, 1),
    (2, 1, 2),
    (3, 2, 3),
    (4, 0, 3),
]

# Se ordenan las aristas por peso ascendente
edges.sort()

# Inicialización de Union-Find para 4 nodos (numerados del 0 al 3)
uf = UnionFind(4)

mst_cost = 0                # Costo total del MST
mst = []                    # Lista de aristas incluidas en el MST

# Iterar sobre las aristas ordenadas
for cost, u, v in edges:
    if uf.union(u, v):
        mst.append((u, v))  # Se agrega la arista al MST
        mst_cost += cost    # Se suma su costo al total

# Resultado final
print("Aristas en el árbol de expansión mínima:", mst)
print("Costo total:", mst_cost)