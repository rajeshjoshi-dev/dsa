def traverse(grid: list[list[str]], row: int, col: int, visited: set):
    if grid[row][col] == "W":
        return

    if (row, col) in visited:
        return

    visited.add((row, col))

    neighbours = []

    if row < len(grid) - 1:
        neighbours.append([row + 1, col])
    if col < len(grid[row]) - 1:
        neighbours.append([row, col + 1])
    if row > 0:
        neighbours.append([row - 1, col])
    if col > 0:
        neighbours.append([row, col - 1])

    for neighbour in neighbours:
        traverse(grid, neighbour[0], neighbour[1], visited)


def count_island(grid: list[list[str]]) -> int:
    count = 0

    visited: set[list[int]] = set()

    for row, _ in enumerate(grid):
        for col, _ in enumerate(grid[row]):
            cell = grid[row][col]
            if cell == "W":
                continue

            if (row, col) in visited:
                continue

            traverse(grid, row, col, visited)
            count += 1

    return count


grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

if __name__ == "__main__":
    result = count_island(grid)
    print(result)
