def bellman_ford(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0

    # Relax edges V-1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    # Detect negative cycle
    for u in graph:
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                raise ValueError("Negative cycle detected")

    return dist


graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": [],
}

if __name__ == "__main__":
    print(bellman_ford(graph, "A"))
