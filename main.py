import pygame
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Setup Constants
# Window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
FPS = 60

# Colors (RGB format)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# 3. Create the screen surface
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sudoku Solver Visualizer")

# Clock to control frame rate
clock = pygame.time.Clock()

def get_initial_board():
    test_board = [
        [5, 3, 0,  0, 7, 0,  0, 0, 0],
        [6, 0, 0,  1, 9, 5,  0, 0, 0],
        [0, 9, 8,  0, 0, 0,  0, 6, 0],
        
        [8, 0, 0,  0, 6, 0,  0, 0, 3],
        [4, 0, 0,  8, 0, 3,  0, 0, 1],
        [7, 0, 0,  0, 2, 0,  0, 0, 6],
        
        [0, 6, 0,  0, 0, 0,  2, 8, 0],
        [0, 0, 0,  4, 1, 9,  0, 0, 5],
        [0, 0, 0,  0, 8, 0,  0, 7, 9]
    ]
    return test_board

def main():
    # 4. Main Game Loop
    running = True
    board = get_initial_board()
    font = pygame.font.SysFont('Arial', 40)

    solved = False
    while running:
        # Limit frame rate to 60 FPS
        clock.tick(FPS)

        # 5. Event Handling
        for event in pygame.event.get():
            # If the user clicks the "X" close button, stop the loop
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not solved:
                    solve(screen, board, font)
                    solved = True
        
        if solved or not solved:
            draw_window(screen, board, font)
            pygame.display.flip()
    # Clean up and close the program
    pygame.quit()
    sys.exit()

def draw_window(screen, board, font):
    screen.fill(COLOR_WHITE)
    for i in range(0, 600, 60):
        if i % 180 == 0:
            new_width = 4
        else:
            new_width = 1

        pygame.draw.line(surface=screen, color=COLOR_BLACK, start_pos=(i,0), end_pos=(i,540), width=new_width)
        pygame.draw.line(surface=screen, color=COLOR_BLACK, start_pos=(0,i), end_pos=(540,i), width=new_width)

    for row in range(9):
        for col in range(9):
            value = board[row][col]
            if value != 0:
                text_surface = font.render(str(value), True, COLOR_BLACK)
                x_pos = col * 60 + 20
                y_pos = row * 60 + 10
                screen.blit(text_surface, (x_pos, y_pos))

def is_valid(board, row, col, num):
    for r in range(9):
        
        if board[r][col] == num and r != row:
            return False
        if board[row][r] == num and r != col:
            return False
        
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(3):
        for i in range(3):
            if board[box_row + r][box_col + i] == num and ((box_row + r) != row and (box_col + i) != col):
                return False
    return True

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def solve(screen, board, font):
    empty = find_empty(board)

    if not empty:
        return True
    
    row, col = empty

    for num in range(1,10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            draw_window(screen, board, font)
            pygame.display.flip()
            pygame.time.delay(1)

            if solve(screen, board, font): 
                return True
            board[row][col] = 0

            draw_window(screen, board, font)
            pygame.display.flip()
            pygame.time.delay(50)
    return False


if __name__ == "__main__":
    main()

