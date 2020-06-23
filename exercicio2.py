aresta = list()
a = list()

def grafo():
  repita = 's'
  v = 1
  print(f"vertice V{v}: ")
  while repita == 's':
    v = v + 1
    n = int(input("quantas arestas: "))
    for i in range(0,n):
      a.append(int(input("digite as arestas: ")))
    aresta.append(a[:])
    del a[:]
    repita = (input(f" deseja adicionar vertice a V{v}, [s/n] ? "))
    if repita == 'n':
      break

def mostrarAdjacente():
  for e, i in enumerate(aresta):
    e = e + 1
    print(f"V{e} é adjacente a V{i[1:]}")
  print("\n")

def mostrarGrafo():
  print("\n\nGrafo G = [")
  for i in aresta:
    print(i)
  print("]\n\n")

def grauVertices():
  for e, i in enumerate(aresta):
    e = e + 1
    print(f"V{e} é grau {len(i[1:])}")
  print("\n")


def vereficaArestav1v2():
  if aresta[0][0] == aresta[1][1]:
    if set(aresta[0][2:]).intersection(aresta[1][2:]):
      print(f"\nexiste aresta entre V1 e V2 e é {set(aresta[0][2:]).intersection(aresta[1][2:])}\n\n")
    else:
      print("\nNao existe \n\n")
  else:
    print("\nnão há como existir vertices entre V1 e V2\n\n")
    


grafo()
mostrarGrafo()
mostrarAdjacente()
grauVertices()
vereficaArestav1v2()


