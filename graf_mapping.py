import random
import matplotlib.pyplot as plt
import networkx as nx


def generate_random_isomorphic_copy(G):
  """Generates a random isomorphic copy of graph G

  by applying a uniformly random vertex permutation.
  """
  # 1. Extract current nodes
  nodes = list(G.nodes())

  # 2. Create a shuffled copy of the nodes to form a random mapping
  shuffled_nodes = nodes.copy()
  random.shuffle(shuffled_nodes)

  # 3. Create a dictionary mapping old node -> new random node
  mapping = dict(zip(nodes, shuffled_nodes))

  # 4. Relabel the graph
  H = nx.relabel_nodes(G, mapping)

  return H, mapping


# --- Example Usage ---
if __name__ == "__main__":
  # Create a sample graph (e.g., a Petersen graph or a small scale-free graph)
  G = nx.petersen_graph()
  # 2. Draw the graph
  plt.figure(figsize=(8, 6))
  nx.draw(G, with_labels=True, node_color="skyblue", edge_color="gray")
  # 3. Save to disk instead of calling plt.show()
  plt.savefig("G1.png", dpi=300, bbox_inches="tight")
  plt.close()

  # Generate a random isomorphic copy
  H, node_mapping = generate_random_isomorphic_copy(G)
  print(node_mapping)
  plt.figure(figsize=(8, 6))
  nx.draw(H, with_labels=True, node_color="skyblue", edge_color="gray")
  # 3. Save to disk instead of calling plt.show()
  plt.savefig("G2.png", dpi=300, bbox_inches="tight")
  plt.close()

  # Verify they are isomorphic
  print(f"Are G and H isomorphic? {nx.is_isomorphic(G, H)}")
  print(f"Original nodes count: {G.number_of_nodes()}")
  print(f"Isomorphic copy nodes count: {H.number_of_nodes()}")



