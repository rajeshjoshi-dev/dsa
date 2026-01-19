def dfs(graph, node, visited: set = set()):
    if node in visited:
        return

    print(node, end=" ")
    visited.add(node)

    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)


def prepare_graph(edges: list[list[str]]) -> dict[str : list[str]]:
    graph = {}

    for edge in edges:
        n1, n2 = edge
        n1_neighbours: list[str] = graph.get(n1, [])
        n2_neighbours: list[str] = graph.get(n2, [])

        n1_neighbours.append(n2)
        n2_neighbours.append(n1)

        graph.update(
            {
                n1: n1_neighbours,
                n2: n2_neighbours,
            }
        )

    return graph


edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]

if __name__ == "__main__":
    graph = prepare_graph(edges)
    dfs(graph, "k")  # k i j m l
