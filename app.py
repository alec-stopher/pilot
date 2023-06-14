import pygame

#one way to do this:
#game_board = [['' for _ in range(10)] for _ in range(10)]
#
#game_board[0][0] = 'flag'
#game_board[1][1] = 'spy'

game_board = [['flag' if j < 4 else 'spy' if j >= 6 else '' for j in range(10)] for i in range(10)]

pieces = {
    'flag': (255, 0, 0),  # Red
    'spy': (0, 0, 255),  # Blue
    # Add more pieces...
}


# Initialize Pygame
pygame.init()

# Define constants for the width and height of the squares and the whole window
SQUARE_SIZE = 100
WIDTH, HEIGHT = SQUARE_SIZE * 10, SQUARE_SIZE * 10

background = pygame.image.load('final_game_map.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Resize image to fit window

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.blit(background, (0, 0))

    # Draw the board
    for i in range(10):
        for j in range(10):
            piece = game_board[i][j]
            if piece != '':
                pygame.draw.circle(window, pieces[piece], (i * SQUARE_SIZE + SQUARE_SIZE // 2, j * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

    # Update the display
    pygame.display.flip()

pygame.quit()
