
import asyncio
import pygame

from constants import *
from grid import Grid
from robot import Robot
from utils import nearest_dirt
from astar import astar

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Grid Cleaner")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Initialize grid and robot
grid = Grid(ROWS, COLS)
robot = Robot()

# Count initial dirt
total_dirt = sum(row.count(1) for row in grid.grid)
cleaned = 0
move_timer = 0


async def main():
    global cleaned, move_timer

    running = True

    while running:
        clock.tick(FPS)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not running:
            break

        # Move robot approximately once every second
        move_timer += 1

        if move_timer >= FPS:
            current_position = (robot.row, robot.col)

            # Clean dirt under the robot before searching
            if grid.is_dirty(robot.row, robot.col):
                grid.clean(robot.row, robot.col)
                cleaned += 1
                print("Cleaned dirt at:", current_position)

            # Find nearest remaining dirt
            target = nearest_dirt(grid, robot)

            print("Robot position:", current_position)
            print("Target:", target)

            if target is not None:
                path = astar(grid, current_position, target)
                print("Path:", path)

                if path:
                    # Move one cell along the path
                    next_row, next_col = path[0]

                    robot.row = next_row
                    robot.col = next_col
                    robot.steps += 1

                    if robot.battery > 0:
                        robot.battery -= 1

                    # Clean dirt at the new position
                    if grid.is_dirty(robot.row, robot.col):
                        grid.clean(robot.row, robot.col)
                        cleaned += 1
                        print("Cleaned dirt!")
                else:
                    print("Empty path. Checking robot and target positions.")

            else:
                print("All dirt has been cleaned!")

            move_timer = 0

        # Draw background
        screen.fill(WHITE)

        # Draw grid, dirt, and obstacles
        for i in range(ROWS):
            for j in range(COLS):
                rect = (
                    j * CELL_SIZE,
                    i * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )

                pygame.draw.rect(screen, GRAY, rect, 1)

                # Dirt
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

                # Obstacles
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

        # Draw robot
        pygame.draw.circle(
            screen,
            BLUE,
            (
                robot.col * CELL_SIZE + CELL_SIZE // 2,
                robot.row * CELL_SIZE + CELL_SIZE // 2
            ),
            12
        )

        # Draw statistics
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

        # Update the screen
        pygame.display.flip()

        # Yield control to the browser
        await asyncio.sleep(0)

    pygame.quit()


# Run the game
asyncio.run(main())
