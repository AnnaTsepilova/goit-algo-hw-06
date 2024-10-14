import networkx as nx
import heapq

# Створимо граф з вагами на ребрах
G = nx.Graph()

# Додамо вузли
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

# Додамо ребра з вагами (відстань між вершинами)
G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "D", weight=5)
G.add_edge("C", "E", weight=3)
G.add_edge("D", "E", weight=1)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізуємо відстані від стартової вершини до всіх інших як нескінченність
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    # Черга з пріоритетом для відстеження вершини з найменшою відстанню
    priority_queue = [(0, start)]  # (відстань, вузол)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо відстань, яку ми витягаємо з черги, більше, ніж вже відома відстань, пропускаємо її
        if current_distance > distances[current_node]:
            continue

        # Оновлюємо відстані до сусідніх вершин
        for neighbor, attrs in graph[current_node].items():
            distance = current_distance + attrs['weight']

            # Якщо нова відстань до сусіда менша за попередню, оновлюємо її
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Використаємо алгоритм Дейкстри для пошуку найкоротших шляхів від кожної вершини
for node in G.nodes:
    shortest_paths = dijkstra(G, node)
    print(f"Найкоротші шляхи від вершини {node}: {shortest_paths}")
