import networkx as nx
from collections import deque

# Функція для пошуку в глибину (DFS)
def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path + [neighbor])
            if new_path:
                return new_path
    return None

# Функція для пошуку в ширину (BFS)
def bfs(graph, start, goal):
    queue = deque([[start]])  # Використовуємо чергу для зберігання шляхів
    visited = set()  # Множина для відвіданих вершин
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path) + [neighbor]
                queue.append(new_path)
    return None

# Створимо граф з першого завдання
G = nx.Graph()

# Додамо вузли з координатами
G.add_node("A", pos=(0, 0))
G.add_node("B", pos=(1, 2))
G.add_node("C", pos=(2, 0))
G.add_node("D", pos=(3, 3))
G.add_node("E", pos=(4, 1))

# Додамо ребра
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("C", "E")
G.add_edge("D", "E")

# Використовуємо алгоритми для пошуку шляху між вершинами "A" і "E"
start_node = "A"
goal_node = "E"

# Пошук в глибину (DFS)
dfs_path = dfs(G, start_node, goal_node)
print(f"Шлях DFS від {start_node} до {goal_node}: {dfs_path}")

# Пошук в ширину (BFS)
bfs_path = bfs(G, start_node, goal_node)
print(f"Шлях BFS від {start_node} до {goal_node}: {bfs_path}")
