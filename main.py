import pygame
import os
pygame.init()

WIDTH, HEIGHT = 500,500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

BG = pygame.transform.scale(pygame.image.load(os.path.join("Board.png")).convert_alpha(), (WIDTH, HEIGHT))

PlayX = pygame.image.load("X.png").convert_alpha()
PlayX = pygame.transform.scale(PlayX, (20, 20))

PlayO = pygame.image.load("O.png").convert_alpha()
PlayO = pygame.transform.scale(PlayO, (20, 20))

FinX = pygame.image.load("X.png").convert_alpha()
FinX = pygame.transform.scale(FinX, (125, 125))

FinO = pygame.image.load("O.png").convert_alpha()
FinO = pygame.transform.scale(FinO, (125, 125))

while True:

    WIN.blit(BG, (0,0))
    WIN.blit(PlayX, (50, 50))
    WIN.blit(PlayO, (50, 90))
    WIN.blit(FinX, (38, 189))
    WIN.blit(FinO, (38, 338))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()