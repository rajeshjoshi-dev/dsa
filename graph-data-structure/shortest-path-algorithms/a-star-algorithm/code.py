import heapq


def neighbors(cell):
    x, y = cell
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            yield (nx, ny), 1


def heuristic(cell):
    gx, gy = goal
    x, y = cell
    return abs(x - gx) + abs(y - gy)  # Manhattan distance


def a_star(start, goal, neighbors, heuristic):

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, g_score[goal]

        for neighbor, cost in neighbors(current):
            tentative_g = g_score[current] + cost

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, neighbor))

    return None, float("inf")


if __name__ == "__main__":
    start = (0, 0)
    goal = (4, 4)

    path, cost = a_star(start, goal, neighbors, heuristic)
    print(path, cost)
