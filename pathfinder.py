import pygame
import sys
import random
import heapq
from commands import ask

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 20
BLACK = (0, 0, 0)
RED = (255, 0, 0)
rang = 255
GREEN = (0, rang, 0)
SCORE = 0

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)
        self.grow = False

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        if (
            (new_direction == "UP" and self.direction != (0, 1)) or
            (new_direction == "DOWN" and self.direction != (0, -1)) or
            (new_direction == "LEFT" and self.direction != (1, 0)) or
            (new_direction == "RIGHT" and self.direction != (-1, 0))
        ):
            self.direction = {
                "UP": (0, -1),
                "DOWN": (0, 1),
                "LEFT": (-1, 0),
                "RIGHT": (1, 0)
            }[new_direction]

    def check_collision(self):
        head = self.body[0]
        return (
            head in self.body[1:] or
            head[0] < 0 or head[0] >= GRID_WIDTH or
            head[1] < 0 or head[1] >= GRID_HEIGHT
        )

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def respawn(self, snake_body):
        while True:
            new_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if new_position not in snake_body:
                self.position = new_position
                break

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Heuristic function for pathfinding
def heuristic(a, b, snake_body, walls1, walls2):
    h = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return h


# Pathfinding function
def find_path(snake, food):
    open_set = []
    closed_set = set()
    came_from = {}

    start = snake.body[0]
    goal = food.position

    heapq.heappush(open_set, (0, start))
    graph = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    # Mark the snake's body as obstacles
    for segment in snake.body:
        graph[segment[1]][segment[0]] = -1

    while open_set:
        current_cost, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            return path

        closed_set.add(current_node)

        for neighbor in [(current_node[0] + 1, current_node[1]),
                         (current_node[0] - 1, current_node[1]),
                         (current_node[0], current_node[1] + 1),
                         (current_node[0], current_node[1] - 1)]:
            if (
                0 <= neighbor[0] < GRID_WIDTH
                and 0 <= neighbor[1] < GRID_HEIGHT
                and graph[neighbor[1]][neighbor[0]] != -1
                and neighbor not in closed_set
            ):
                tentative_cost = current_cost + 1
                total_cost = tentative_cost + heuristic(neighbor, goal, snake.body, GRID_WIDTH, GRID_HEIGHT)
                if (total_cost, neighbor) not in open_set:
                    came_from[neighbor] = current_node
                    heapq.heappush(open_set, (total_cost, neighbor))

    # No path found
    return []


# Fallback move when no path is found
def fallback_move(snake):
    safe_directions = []
    head = snake.body[0]

    for direction, offset in {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}.items():
        new_position = (head[0] + offset[0], head[1] + offset[1])
        if (
            0 <= new_position[0] < GRID_WIDTH
            and 0 <= new_position[1] < GRID_HEIGHT
            and new_position not in snake.body
        ):
            safe_directions.append((direction, offset))

    if safe_directions:
        chosen_direction = random.choice(safe_directions)
        snake.change_direction(chosen_direction[0])


# Main function
def main():
    global WIDTH, HEIGHT, GRID_WIDTH, GRID_HEIGHT, SNAKE_SPEED, screen_speed, screen, SCORE

    screen_size = int(input('screen size? (between 400 - 2000):'))
    if screen_size >= 2000:
        screen_size = 2000
    elif screen_size <= 400:
        screen_size = 400

    ask('Speed?')
    screen_speed = int(input('Speed? (between 1- 10):'))
    if screen_speed >= 10:
        screen_speed = 10
    elif screen_speed <= 1:
        screen_speed = 1

    WIDTH, HEIGHT = screen_size, screen_size
    GRID_WIDTH = WIDTH // GRID_SIZE
    GRID_HEIGHT = HEIGHT // GRID_SIZE
    SNAKE_SPEED = 10

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake AI")

    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()
    frame_count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if frame_count % SNAKE_SPEED == 0:
            path = find_path(snake, food)
            if path:
                next_step = path[0]
                snake.direction = (next_step[0] - snake.body[0][0], next_step[1] - snake.body[0][1])
            else:
                fallback_move(snake)

            snake.move()

        if snake.body[0] == food.position:
            snake.grow = True
            SCORE += 1
            print("Score:", SCORE)
            food.respawn(snake.body)

        if snake.check_collision():
            print("Game Over! Final Score:", SCORE)
            pygame.quit()
            sys.exit()
        rang = random.randint(100, 255)

        screen.fill(BLACK)
        snake.draw()
        food.draw()
        pygame.display.flip()
        clock.tick(150 * screen_speed)
        frame_count += 1


if __name__ == "__main__":
    main()
