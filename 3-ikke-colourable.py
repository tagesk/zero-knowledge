import random
import matplotlib.pyplot as plt
import networkx as nx

def generate_non_3_colorable_graph(num_nodes=15, edge_probability=0.4):
    """
    Generates a graph guaranteed NOT to be 3-colorable by embedding a 
    K_4 clique (4 fully connected nodes) as a core invariant.
    """
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    
    # Step 1: Force a K_4 clique on the first 4 nodes (0, 1, 2, 3)
    # A complete graph of 4 nodes strictly requires 4 colors.
    k4_nodes = [0, 1, 2, 3]
    for i in range(len(k4_nodes)):
        for j in range(i + 1, len(k4_nodes)):
            G.add_edge(k4_nodes[i], k4_nodes[j])
            
    # Step 2: Add remaining random edges across the rest of the graph
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            # Skip edges already added in the K_4 core
            if i in k4_nodes and j in k4_nodes:
                continue
            if random.random() < edge_probability:
                G.add_edge(i, j)
                
    return G

def plot_and_save_non_3_colorable(G, filename="G4.png"):
    """
    Computes a greedy coloring (which will require >= 4 colors) and 
    saves the visualization as a PNG.
    """
    # Use NetworkX's greedy coloring strategy to color the graph
    coloring = nx.coloring.greedy_color(G, strategy="saturation_largest_first")
    max_color = max(coloring.values()) + 1
    
    print(f"Graph successfully colored using {max_color} colors (proving it's not 3-colorable).")
    
    # Define a distinct color palette for up to 5 colors
    color_map_palette = ['#FF6B6B', '#4ECDC4', '#FFE66D', '#C7F464', '#4D96FF']
    node_colors = [color_map_palette[coloring[node] % len(color_map_palette)] for node in G.nodes()]
    
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    
    # Highlight the K_4 core nodes differently or draw normally with the color palette
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700, edgecolors='black', linewidths=1.2)
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.6, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold', font_color='black')
    
    #plt.title(f"Guaranteed Non-3-Colorable Graph ($n=15$, Requires {max_color} Colors)", fontsize=13, fontweight='bold', pad=15)
    plt.axis('off')
    plt.tight_layout()
    
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Successfully generated and saved graph to '{filename}'")

if __name__ == "__main__":
    random.seed(42)
    
    # Generate graph with 15 nodes
    G = generate_non_3_colorable_graph(num_nodes=15, edge_probability=0.4)
    
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")
    
    # Render and save
    plot_and_save_non_3_colorable(G)
