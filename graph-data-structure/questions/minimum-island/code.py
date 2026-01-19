def traverse(grid: list[list[str]], row: int, col: int, visited: set) -> int:
    if grid[row][col] == "W":
        return 0
    if (row, col) in visited:
        return 0

    visited.add((row, col))
    size = 1

    neighbours = []

    if row < len(grid) - 1:
        neighbours.append([row + 1, col])
    if col < len(grid[0]) - 1:
        neighbours.append([row, col + 1])
    if row > 0:
        neighbours.append([row - 1, col])
    if col > 0:
        neighbours.append([row, col - 1])

    for neighbour in neighbours:
        size += traverse(grid, neighbour[0], neighbour[1], visited)

    return size


def minimum_island(grid: list[list[str]]) -> int:
    min_size = len(grid) * len(grid[0])

    visited: set[list[int]] = set()

    for row, _ in enumerate(grid):
        for col, _ in enumerate(grid[row]):
            if grid[row][col] == "W":
                continue
            if (row, col) in visited:
                continue
            island_size = traverse(grid, row, col, visited)
            min_size = min(island_size, min_size)

    return min_size


grid = [
    ["W", "L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "W", "W", "L", "W", "W"],
]


if __name__ == "__main__":
    result = minimum_island(grid)
    print(result)  # 2
