import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф з вагами ребер
G = nx.Graph()

# Додаємо вершини (міста)
cities = ['Kharkiv', 'Kyiv', 'Vinnytsia', 'Chernivtsi', 'Uzhhorod']
G.add_nodes_from(cities)

# Додаємо ребра з вагами (відстані між містами у вигляді довільних значень)
edges_with_weights = [
    ('Kharkiv', 'Kyiv', 470),    # Відстань між Харковом і Києвом
    ('Kyiv', 'Vinnytsia', 267),  # Відстань між Києвом і Вінницею
    ('Vinnytsia', 'Chernivtsi', 234),  # Відстань між Вінницею і Чернівцями
    ('Chernivtsi', 'Uzhhorod', 325),   # Відстань між Чернівцями і Ужгородом
    ('Kyiv', 'Chernivtsi', 538)   # Відстань між Києвом і Чернівцями
]

G.add_weighted_edges_from(edges_with_weights)

# Візуалізуємо граф із вагами ребер
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Визначаємо положення для вершин
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Граф міст з вагами ребер")
plt.show()

# Алгоритм Дейкстри для знаходження найкоротшого шляху між усіма вершинами
shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))
shortest_path_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

# Виведемо найкоротші шляхи між усіма парами вершин
for start_city, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від {start_city}:")
    for end_city, path in paths.items():
        print(f"  до {end_city}: шлях {path}, довжина {shortest_path_lengths[start_city][end_city]} км")
