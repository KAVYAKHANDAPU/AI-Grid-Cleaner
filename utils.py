def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def nearest_dirt(grid, robot):
    nearest = None
    shortest_distance = float("inf")

    for i in range(grid.rows):
        for j in range(grid.cols):
            if grid.grid[i][j] == 1:   # Dirty cell
                distance = manhattan((robot.row, robot.col), (i, j))

                if distance < shortest_distance:
                    shortest_distance = distance
                    nearest = (i, j)

    return nearest