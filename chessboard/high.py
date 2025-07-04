import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DIM_ALPHA = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minimal Chessboard")

selected_square = None
clock = pygame.time.Clock()

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

def darken_screen():
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(DIM_ALPHA)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

def draw_glow(row, col, time):
    pulse = int(127 + 128 * math.sin(time * 3))
    glow_color = (255, pulse, 0)  # Red to yellow pulse
    rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(screen, glow_color, rect)

running = True
while running:
    time = pygame.time.get_ticks() / 1000
    draw_board()

    if selected_square is not None:
        darken_screen()
        draw_glow(*selected_square, time)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE
            if selected_square == (row, col):
                selected_square = None
            else:
                selected_square = (row, col)

pygame.quit()
sys.exit()