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

    while running:
        # Limit frame rate to 60 FPS
        clock.tick(FPS)
        
        # 5. Event Handling
        for event in pygame.event.get():
            # If the user clicks the "X" close button, stop the loop
            if event.type == pygame.QUIT:
                running = False
                
        # 6. Draw / Render
        # Fill the background with white
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


        pygame.display.flip()

    # Clean up and close the program
    pygame.quit()
    sys.exit()

    def is_valid(board, row, col, num):
        for r in range(9):
            
            if board[r][col] == num:
                return False
            if board[row][r] == num:
                return False
            
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for r in range(3):
            for i in range(3):
                if board[box_row + r][box_col + i] == num:
                    return False
        return True

if __name__ == "__main__":
    main()

