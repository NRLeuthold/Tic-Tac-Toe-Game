import pygame
import os
from XcordsDict import cordsX
from YcordsDict import cordsY
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


white = (255,255,255)
red = (255,0,0)
dark_red = (139,0,0)
blue = (0,0,255)
dark_blue = (0,0,139)

class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

def draw(self, WIN, outline=None):
    if outline:
        pygame.draw.rect(WIN, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
    
    pygame.draw.rect(WIN, self.color, (self.x,self.y,self.width,self.height),0)

    if self.text != '':
        font = pygame.font.SysFont('comicsans', 20)
        text = font.render(self.text, 1, (0,0,0))
        WIN.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

def isOver(self, pos):
    if pos[0] > self.x and pos[0] < self.x + self.width:
        if pos[1] > self.y and pos[1] < self.y + self.height:
            return True
    return False

Player1 = button(red, 149, 0, 100, 25, text='Player 1')
Player2 = button(blue, 251, 0, 100, 25, text='Player 2')

A1 = button(white, 50, 50, 20, 20, text='')

play = 0

while True:

    WIN.blit(BG, (0,0))

    draw(Player1, WIN)
    if isOver(Player1, pygame.mouse.get_pos()) == True:
        Player1.color = dark_red
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                play = 1

            else:
                Player1.color = red

    draw(Player2, WIN)
    if isOver(Player2, pygame.mouse.get_pos()) == True:
        Player2.color = dark_blue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                play = 2

            else:
                Player2.color = blue


    draw(A1, WIN)
    if isOver(A1, pygame.mouse.get_pos()) == True:
        A1.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    A1.text = "X"
                if play == 2:
                    A1.text = "O"
            else:
                A1.color = ((255,255,255))
        if A1.text == 'X' or A1.text == 'O':
            A1.color = ((255,255,255))

    if play == 1:
        Player1.text = 'Your Turn'
        Player2.text = 'Player 2'
    
    if play == 2:
        Player1.text = 'Player 1'
        Player2.text = 'Your Turn'
    
    if play == 0:
        Player1.text = 'Player 1'
        Player2.text = 'Player 2'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
