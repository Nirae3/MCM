import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()

#Accomidations for ppl to stay in
# AirBNB and B&B and cabins and hotels - S
#longer term House rentals - M
#Locals live forever - L

G.add_nodes_from(["Trsts","Rvn","Tax","Envr", "Expend", "Wtr Sply", "Trnsp", "Attrctn", "Svng", "Hotel", "House", "roads", "Glcr Sz"] )
G.add_edges_from([
    ("Trnsp", "Envr"),
    ("Svng", "House"),
    ("Svng", "roads"),
    ("Trsts", "Rvn"),
    ("Trsts", "Hotel"),
    ("Trsts", "House"),
    ("Rvn", "Tax"),
    ("Trsts", "Expend"),
    ("Trsts", "Wtr Sply"),
    ("Trsts", "Attrctn"),
    ("Envr", "Glcr Sz"),
    ("Trsts", ("Envr"))])
nx.draw(G, with_labels=True, node_size=1000, font_color="white", font_size=8, font_family="Times New Roman", font_weight="bold", edge_color="black", pos=nx.spring_layout(G))
pos = nx.spring_layout(G, k=0.000001, iterations=100)
plt.margins(0.1)
plt.show()