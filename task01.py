import networkx as nx
import matplotlib.pyplot as plt

# Створимо порожній граф
G = nx.Graph()

# Додамо вузли, які представляють перехрестя або зупинки
G.add_node("A", pos=(0, 0))  # Вузол A на координатах (0, 0)
G.add_node("B", pos=(1, 2))  # Вузол B на координатах (1, 2)
G.add_node("C", pos=(2, 0))  # Вузол C на координатах (2, 0)
G.add_node("D", pos=(3, 3))  # Вузол D на координатах (3, 3)
G.add_node("E", pos=(4, 1))  # Вузол E на координатах (4, 1)

# Додамо ребра, які представляють дороги або маршрути
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("C", "E")
G.add_edge("D", "E")

# Отримуємо позиції для вузлів
pos = nx.get_node_attributes(G, 'pos')

# Візуалізація графу
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, font_weight='bold', edge_color='gray')
plt.title("Транспортна мережа міста")
plt.show()


# Основні характеристики графа
num_nodes = G.number_of_nodes()  # Кількість вершин
num_edges = G.number_of_edges()  # Кількість ребер
degrees = dict(G.degree())  # Ступінь кожної вершини

# Виведемо результати
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"Вершина {node}: Ступінь {degree}")

