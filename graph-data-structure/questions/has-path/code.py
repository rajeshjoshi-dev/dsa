def has_path(graph: dict[str : list[str]], src: str, dest: str):
    if src == dest:
        return True

    for neighbour in graph[src]:
        if has_path(graph, neighbour, dest):
            return True

    return False


graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": [],
}


if __name__ == "__main__":
    result = has_path(graph, "f", "k")
    print(result)
