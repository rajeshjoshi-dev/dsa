def traverse(graph: dict, node, visited: set = {}):
    if node in visited:
        return 0

    visited.add(node)

    count = 1
    for neighbour in graph[node]:
        count += traverse(graph, neighbour, visited)

    return count


def largest_component(graph: dict[str : list[str]]):
    max_component_size = 0

    visited = set()
    for node in graph.keys():

        component_size = traverse(graph, node, visited)
        max_component_size = max(component_size, max_component_size)

    return max_component_size


graph = {
    0: [8, 1, 5],
    1: [0],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
    5: [0, 8],
    8: [0, 5],
}


if __name__ == "__main__":
    result = largest_component(graph)
    print(result)
