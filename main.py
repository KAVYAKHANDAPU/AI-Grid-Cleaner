import pygame

from constants import *
from grid import Grid
from robot import Robot
from utils import nearest_dirt
from astar import astar

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Grid Cleaner")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)


grid = Grid(ROWS, COLS)
robot = Robot()
total_dirt = 0

for row in grid.grid:
    total_dirt += row.count(1)

cleaned = 0

move_timer = 0

running = True

while running:

    clock.tick(FPS)

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Robot moves once every second
    move_timer += 1

    if move_timer >= FPS:

        target = nearest_dirt(grid, robot)

        if target:

            path = astar(
                grid,
                (robot.row, robot.col),
                target
            )

            print("Target:", target)
            print("Path:", path)

            if path:

                next_row, next_col = path[0]

                robot.row = next_row
                robot.col = next_col
                robot.steps += 1
                if robot.battery > 0:
                    robot.battery -= 1

                if grid.is_dirty(robot.row, robot.col):
                    grid.clean(robot.row, robot.col)
                    cleaned +=1

        move_timer = 0

    # Draw Background
    screen.fill(WHITE)

    # Draw Grid
    for i in range(ROWS):
        for j in range(COLS):

            rect = (
                j * CELL_SIZE,
                i * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(screen, GRAY, rect, 1)

            # Draw Dirt
            if grid.grid[i][j] == 1:
                pygame.draw.circle(
                    screen,
                    RED,
                    (
                        j * CELL_SIZE + CELL_SIZE // 2,
                        i * CELL_SIZE + CELL_SIZE // 2
                    ),
                    8
                )

            # Draw Obstacles
            elif grid.grid[i][j] == 2:
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (
                        j * CELL_SIZE + 5,
                        i * CELL_SIZE + 5,
                        CELL_SIZE - 10,
                        CELL_SIZE - 10
                    )
                )

    # Draw Robot
    pygame.draw.circle(
        screen,
        BLUE,
        (
            robot.col * CELL_SIZE + CELL_SIZE // 2,
            robot.row * CELL_SIZE + CELL_SIZE // 2
        ),
        12
    )
    score_text = font.render(
        f"Cleaned: {cleaned}/{total_dirt}",
        True,
        BLACK
        )
    steps_text = font.render(
        f"Steps: {robot.steps}",
        True,
        BLACK
        )
    screen.blit(score_text, (10, 10))
    screen.blit(steps_text, (10, 40))
    
    pygame.display.update()

pygame.quit()