import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (міста)
cities = ['Kharkiv', 'Kyiv', 'Vinnytsia', 'Chernivtsi', 'Uzhhorod']
G.add_nodes_from(cities)

# Додавання ребер (шляхів між містами)
edges = [('Kharkiv', 'Kyiv'),
         ('Kyiv', 'Vinnytsia'),
         ('Vinnytsia', 'Chernivtsi'),
         ('Chernivtsi', 'Uzhhorod'),
         ('Kyiv', 'Chernivtsi')]

G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Обираємо розташування вершин
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{u}-{v}" for u, v in edges})
plt.title("Граф міст")
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()  # Кількість вершин
num_edges = G.number_of_edges()  # Кількість ребер
degree_of_nodes = dict(G.degree())  # Ступінь кожної вершини

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь кожної вершини:")
for node, degree in degree_of_nodes.items():
    print(f"{node}: {degree}")
