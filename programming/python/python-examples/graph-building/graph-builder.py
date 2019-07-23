import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def print_graph(vertices, edges, print_dist=False):
  for v in vertices:
    print("Vertex name: ", v)
    if not print_dist:
      for e in edges:
        if e[0] == v:
          print("-> ", e[1])
    else:
      for e in edges:
        if e[0] == v:
          print("-> ", e[1], e[2])

def print_undirected_graph_nx(vertices, edges, name, draw_spring=False):
  G=nx.Graph()

  for v in vertices:
    G.add_node(v)

  for v in vertices:
    for e in edges:
      G.add_edge(e[0], e[1])

  if not draw_spring:
    nx.draw(G, with_labels=True, node_color='y')
  else:
    nx.draw_random(G, with_labels=True, node_color='y')
  #nx.draw_networkx_edge_labels(G,labels)
  plt.savefig("%s.png" % name) # save as png
  #plt.show()
  plt.clf()

def print_graph_nx(vertices, edges, name, draw_spring=False, print_dist=False):
  G=nx.DiGraph()
  labels = []

  for v in vertices:
    G.add_node(v)

  for v in vertices:
    for e in edges:
      if(len(e)) > 2:
        G.add_edge(e[0], e[1], weight=int(e[2]))
      else:
        G.add_edge(e[0], e[1])

  print("Nodes of graph: ")
  print(G.nodes())
  print("Edges of graph: ")
  print(G.edges())

  if not draw_spring:
    nx.draw(G, with_labels=True, node_color='y')
  else:
    nx.draw_spring(G, with_labels=True, node_color='y')
  #nx.draw_networkx_edge_labels(G,labels)
  plt.savefig("%s.png" % name) # save as png
  #plt.show()
  plt.clf()

if __name__ == "__main__":
  V = ["A","B","C","D","E"]
  E = []
  print_undirected_graph_nx(V,E,0)


  E = [["A","B"],["A","C"],["C","D"]]
  print_undirected_graph_nx(V,E,1)

  E = [["A","B"],["A","C"],["C","D"],["A","E"],["B","D"],["B","C"]]
  print_undirected_graph_nx(V,E,2)

  E = [["A","B"],["A","C"],["C","D"],["A","E"],["B","D"],["B","C"],["A","D"]]
  print_undirected_graph_nx(V,E,3)

  E = [["A","B"],["A","C"],["C","D"],["A","E"],["B","D"],["B","C"],["A","D"],["B","E"]]
  print_undirected_graph_nx(V,E,3)

  # Bipartite graph
  V = ["A","B","C","D","E","F"]
  E = [["A","F"],["A","E"],["C","D"],["C","E"],["B","D"],["B","F"],["A","D"],["C","F"],["B","E"]]
  print_undirected_graph_nx(V,E,4)

  # Directional graph example
  E = [["B","A"],["B","D"],["B","C"],["A","E"],["B","E"],["E","F"],["D","F"],["C","F"]]
  print_graph_nx(V,E,5)

  V = ["A","B","C","D","E"]
  E = [["A","B"],["A","E"],["B","D"],["B","E"],["C","D"],["C","E"],["D","E"]]
  print_undirected_graph_nx(V,E,6)

  V = ["1","2","3","4","5"]
  E = [["2","1"],["2","5"],["1","4"],["1","5"],["3","4"],["3","5"],["4","5"]]
  print_undirected_graph_nx(V,E,7,draw_spring=True)

