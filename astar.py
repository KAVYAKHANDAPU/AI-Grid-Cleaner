import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):

    rows = grid.rows
    cols = grid.cols

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {start: 0}

    f_score = {start: heuristic(start, goal)}

    while open_set:

        current = heapq.heappop(open_set)[1]

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.reverse()

            return path

        row, col = current

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:

            nr = row + dr
            nc = col + dc

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            if grid.is_obstacle(nr, nc):
                continue

            neighbor = (nr, nc)

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:

                came_from[neighbor] = current

                g_score[neighbor] = tentative_g

                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []