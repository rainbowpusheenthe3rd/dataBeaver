from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

# Connect to Neo4j
uri = "bolt://127.0.0.1:7474"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

def get_relationships(tx):
    query = "MATCH ()-[r]->() RETURN r"
    result = tx.run(query)
    relationships = []
    for record in result:
        rel = record["r"]
        start_node = rel.start_node
        end_node = rel.end_node
        relationships.append((start_node.id, list(start_node.labels)[0], end_node.id, list(end_node.labels)[0], rel.type))
    return relationships

with driver.session() as session:
    relationships = session.read_transaction(get_relationships)

driver.close()

# Create a NetworkX graph
G = nx.DiGraph()

# Add nodes and edges
for start_node_id, start_node_label, end_node_id, end_node_label, rel_type in relationships:
    G.add_node(start_node_id, label=start_node_label)
    G.add_node(end_node_id, label=end_node_label)
    G.add_edge(start_node_id, end_node_id, type=rel_type)

# Draw the graph
pos = nx.spring_layout(G)  # Layout for the nodes
labels = nx.get_node_attributes(G, 'label')
edge_labels = nx.get_edge_attributes(G, 'type')

nx.draw(G, pos, with_labels=True, labels=labels, node_size=5000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()