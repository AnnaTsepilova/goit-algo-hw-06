import networkx as nx

# Створення графа (задаємо той самий граф з першого завдання)
G = nx.Graph()
cities = ['Kharkiv', 'Kyiv', 'Vinnytsia', 'Chernivtsi', 'Uzhhorod']
G.add_nodes_from(cities)

edges = [('Kharkiv', 'Kyiv'),
         ('Kyiv', 'Vinnytsia'),
         ('Vinnytsia', 'Chernivtsi'),
         ('Chernivtsi', 'Uzhhorod'),
         ('Kyiv', 'Chernivtsi')]

G.add_edges_from(edges)

# Алгоритм пошуку в глибину (DFS)
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None

# Алгоритм пошуку в ширину (BFS)
def bfs(graph, start, goal):
    queue = [(start, [start])]  # черга для проходження вершин
    
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))
    return None

# Тестування алгоритмів на прикладі пошуку шляху між двома містами
start_city = 'Kharkiv'
goal_city = 'Uzhhorod'

# Пошук за допомогою DFS
dfs_path = dfs(G, start_city, goal_city)
print(f"Шлях з {start_city} до {goal_city} за допомогою DFS: {dfs_path}")

# Пошук за допомогою BFS
bfs_path = bfs(G, start_city, goal_city)
print(f"Шлях з {start_city} до {goal_city} за допомогою BFS: {bfs_path}")
