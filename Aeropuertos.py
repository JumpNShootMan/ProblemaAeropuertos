import heapq as hq
import math
from random import *
INF = float("inf")

with open('input.txt') as f:
    line = f.readline().strip()
    N, M, A = [int(x) for x in line.split(' ')]
    G = [[] for _ in range(N)]
    for _ in range(M):
        line = f.readline().strip()
        local1, local2, costo = [int(x) for x in line.split(' ')]
        local1 -= 1
        local2 -= 1
        G[local1].append((local2, costo))
        #G[local2].append((local1, costo))
    print(G)

# El Output esperado es el costo total de todas las rutas implementadas más el número de aeropuertos construidos

print(N,M,A)

def generarGrafoPesos(n,v):
    mat = [[] for i in range(n)]
    for j in range(v):
        v1 = randint(0, n - 1)
        v2 = randint(0, n - 1)
        w = randint(1, 10)
        adyacentes = [x[0] for x in mat[v1]]
        while(v2 in adyacentes or v2 == v1):
            v1 = randint(0, n - 1)
            v2 = randint(0, n - 1)
        mat[v1] += [(v2,w)]
        mat[v2] += [(v1,w)]
    return mat

def union(grafo, u, v):
    pa = find(grafo, u)
    pb = find(grafo,v)
    if pa == pb:
        return
    if grafo[pa] <= grafo[pb]:
        grafo[pa] += grafo[pb]
        grafo[pb] = pa
    elif grafo[pb] < grafo[pa]:
        grafo[pb] += grafo[pa]
        grafo[pa] = pb

def find(grafo,indice):
    if grafo[indice] < 0:
        return indice
    else:
        grandpa = find(grafo, grafo[indice])
        grafo[indice] = grandpa
        return grandpa


def ordenarGrafo(G):
    cola = []
    for u in range(len(G)):
        for v, w in G[u]:
            hq.heappush(cola, (w,u,v))
    print("Cola: ", cola)
    return cola

cola = ordenarGrafo(G)


def kruskal(G):
    cola = ordenarGrafo(G)
    n = len(G)
    raices = [-1]*n
    T = []
    c = 0
    while len(cola) > 0:
        w, u, v = hq.heappop(cola)
        print(w, u, v)
        if find(raices, u) != find(raices,v):
            union(raices,u,v)
            T.append((u,v,w))
            c += w
    return T, c, raices

mst, peso, raices = kruskal(G)
narboles = 0

# Sacar el numero de arboles
for val in raices:
    if find(raices, val) != 0:
        narboles += 1


print(mst)
print("Peso: ", peso)
print("Raices: ", raices)


def output(narboles, peso, costAero):
    totalAero = narboles
    while peso > costAero:
        peso -= costAero
        totalAero+=1
    costoTotal = peso + (costAero*totalAero)
    print(costoTotal," ", totalAero)
    return

output(narboles, peso, A)
