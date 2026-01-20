import heapq


def dijkstra(graph, start):
    # Distance dictionary
    dist = {node: float("inf") for node in graph}
    dist[start] = 0

    # Min-heap (distance, node)
    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        # Skip outdated entries
        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist


graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": [],
}

if __name__ == "__main__":
    print(dijkstra(graph, "A"))
