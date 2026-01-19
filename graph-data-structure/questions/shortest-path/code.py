def shortest_path(graph: dict[str : list[str]], src: str, dest: str):
    visited = set(src)
    queue: list[list[str, int]] = [[src, 0]]

    while len(queue):
        node, distance = queue.pop(0)

        if node == dest:
            return distance

        for neighbour in graph[node]:
            if neighbour in visited:
                continue
            visited.add(neighbour)
            queue.append([neighbour, distance + 1])

    return -1


graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": [],
}


if __name__ == "__main__":
    result = shortest_path(graph, "f", "k")
    print(result)
