import random
import matplotlib.pyplot as plt
import networkx as nx

def generate_3_colorable_graph(num_nodes=15, edge_probability=0.4):
    """
    Generates a graph guaranteed to be 3-colorable by assigning colors first
    and only adding edges between nodes of differing colors.
    """
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    
    # Step 1: Assign a secret color (0, 1, or 2) to each node
    colors = {node: random.randint(0, 2) for node in G.nodes()}
    nx.set_node_attributes(G, colors, 'color')
    
    # Step 2: Add edges conditionally (only if colors are different)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if colors[i] != colors[j]:
                if random.random() < edge_probability:
                    G.add_edge(i, j)
                    
    return G, colors

def plot_and_save_graph(G, colors, filename="G1.png"):
    """
    Renders the graph using matplotlib, coloring nodes according to their 
    valid 3-coloring assignment, and saves it as a PNG.
    """
    # Define a distinct color palette for the 3 colors
    color_map = {
        0: '#FF6B6B',  # Coral Red
        1: '#4ECDC4',  # Turquoise
        2: '#FFE66D'   # Soft Yellow
    }
    node_colors = [color_map[colors[node]] for node in G.nodes()]
    
    plt.figure(figsize=(8, 6))
    
    # Use spring layout with a fixed seed for reproducible node positioning
    pos = nx.spring_layout(G, seed=42)
    
    # Draw graph components
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700, edgecolors='black', linewidths=1.2)
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.6, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold', font_color='black')
    
    #plt.title("Guaranteed 3-Colorable Graph ($n=15$)", fontsize=14, fontweight='bold', pad=15)
    plt.axis('off')
    plt.tight_layout()
    
    # Save to file
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Successfully generated and saved graph to '{filename}'")

if __name__ == "__main__":
    # Set seed for reproducible results
    random.seed(42)
    
    # Generate graph with 15 nodes
    G, node_colors = generate_3_colorable_graph(num_nodes=15, edge_probability=0.45)
    
    # Output statistics
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")
    
    # Render and save
    plot_and_save_graph(G, node_colors)
