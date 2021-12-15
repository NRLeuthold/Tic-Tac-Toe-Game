import pygame
import os
pygame.init()

WIDTH, HEIGHT = 500,500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

BG = pygame.transform.scale(pygame.image.load(os.path.join("Board.png")).convert_alpha(), (WIDTH, HEIGHT))


while True:

    WIN.blit(BG, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()