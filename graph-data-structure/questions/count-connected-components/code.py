def traverse(graph: dict, node: str, visited: set):
    if node in visited:
        return

    visited.add(node)
    for neighbour in graph[node]:
        traverse(graph, neighbour, visited)


def count_connected_components(graph: dict):
    visited = set()
    count = 0

    for node in graph.keys():
        if node in visited:
            continue
        traverse(graph, node, visited)
        count += 1

    return count


graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": [],
}


if __name__ == "__main__":
    result = count_connected_components(graph)
    print(result)
