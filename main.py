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
A2 = button(white, 90, 50, 20, 20, text='')
A3 = button(white, 130, 50, 20, 20, text='')
A4 = button(white, 50, 90, 20, 20, text='')
A5 = button(white, 90, 90, 20, 20, text='')
A6 = button(white, 130, 90, 20, 20, text='')
A7 = button(white, 50, 130, 20, 20, text='')
A8 = button(white, 90, 130, 20, 20, text='')
A9 = button(white, 130, 130, 20, 20, text='')

B1 = button(white, 200, 50, 20, 20, text='')
B2 = button(white, 240, 50, 20, 20, text='')
B3 = button(white, 280, 50, 20, 20, text='')
B4 = button(white, 200, 90, 20, 20, text='')
B5 = button(white, 240, 90, 20, 20, text='')
B6 = button(white, 280, 90, 20, 20, text='')
B7 = button(white, 200, 130, 20, 20, text='')
B8 = button(white, 240, 130, 20, 20, text='')
B9 = button(white, 280, 130, 20, 20, text='')

C1 = button(white, 350, 50, 20, 20, text='')
C2 = button(white, 390, 50, 20, 20, text='')
C3 = button(white, 430, 50, 20, 20, text='')
C4 = button(white, 350, 90, 20, 20, text='')
C5 = button(white, 390, 90, 20, 20, text='')
C6 = button(white, 430, 90, 20, 20, text='')
C7 = button(white, 350, 130, 20, 20, text='')
C8 = button(white, 390, 130, 20, 20, text='')
C9 = button(white, 430, 130, 20, 20, text='')

D1 = button(white, 50, 200, 20, 20, text='')
D2 = button(white, 90, 200, 20, 20, text='')
D3 = button(white, 130, 200, 20, 20, text='')
D4 = button(white, 50, 240, 20, 20, text='')
D5 = button(white, 90, 240, 20, 20, text='')
D6 = button(white, 130, 240, 20, 20, text='')
D7 = button(white, 50, 280, 20, 20, text='')
D8 = button(white, 90, 280, 20, 20, text='')
D9 = button(white, 130, 280, 20, 20, text='')

E1 = button(white, 200, 200, 20, 20, text='')
E2 = button(white, 240, 200, 20, 20, text='')
E3 = button(white, 280, 200, 20, 20, text='')
E4 = button(white, 200, 240, 20, 20, text='')
E5 = button(white, 240, 240, 20, 20, text='')
E6 = button(white, 280, 240, 20, 20, text='')
E7 = button(white, 200, 280, 20, 20, text='')
E8 = button(white, 240, 280, 20, 20, text='')
E9 = button(white, 280, 280, 20, 20, text='')

F1 = button(white, 350, 200, 20, 20, text='')
F2 = button(white, 390, 200, 20, 20, text='')
F3 = button(white, 430, 200, 20, 20, text='')
F4 = button(white, 350, 240, 20, 20, text='')
F5 = button(white, 390, 240, 20, 20, text='')
F6 = button(white, 430, 240, 20, 20, text='')
F7 = button(white, 350, 280, 20, 20, text='')
F8 = button(white, 390, 280, 20, 20, text='')
F9 = button(white, 430, 280, 20, 20, text='')

G1 = button(white, 50, 350, 20, 20, text='')
G2 = button(white, 90, 350, 20, 20, text='')
G3 = button(white, 130, 350, 20, 20, text='')
G4 = button(white, 50, 390, 20, 20, text='')
G5 = button(white, 90, 390, 20, 20, text='')
G6 = button(white, 130, 390, 20, 20, text='')
G7 = button(white, 50, 430, 20, 20, text='')
G8 = button(white, 90, 430, 20, 20, text='')
G9 = button(white, 130, 430, 20, 20, text='')

H1 = button(white, 200, 350, 20, 20, text='')
H2 = button(white, 240, 350, 20, 20, text='')
H3 = button(white, 280, 350, 20, 20, text='')
H4 = button(white, 200, 390, 20, 20, text='')
H5 = button(white, 240, 390, 20, 20, text='')
H6 = button(white, 280, 390, 20, 20, text='')
H7 = button(white, 200, 430, 20, 20, text='')
H8 = button(white, 240, 430, 20, 20, text='')
H9 = button(white, 280, 430, 20, 20, text='')

I1 = button(white, 350, 350, 20, 20, text='')
I2 = button(white, 390, 350, 20, 20, text='')
I3 = button(white, 430, 350, 20, 20, text='')
I4 = button(white, 350, 390, 20, 20, text='')
I5 = button(white, 390, 390, 20, 20, text='')
I6 = button(white, 430, 390, 20, 20, text='')
I7 = button(white, 350, 430, 20, 20, text='')
I8 = button(white, 390, 430, 20, 20, text='')
I9 = button(white, 430, 430, 20, 20, text='')


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
                    play = 2
                elif play == 2:
                    A1.text = "O"
                    play = 1
            else:
                A1.color = ((255,255,255))
        if A1.text == 'X' or A1.text == 'O':
            A1.color = ((255,255,255))

    draw(A2, WIN)
    if isOver(A2, pygame.mouse.get_pos()) == True:
        A2.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    A2.text = "X"
                    play = 2
                elif play == 2:
                    A2.text = "O"
                    play = 1
            else:
                A2.color = ((255,255,255))
        if A2.text == 'X' or A2.text == 'O':
            A2.color = ((255,255,255))

    draw(A3, WIN)
    if isOver(A3, pygame.mouse.get_pos()) == True:
        A3.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    A3.text = "X"
                    play = 2
                elif play == 2:
                    A3.text = "O"
                    play = 1
            else:
                A3.color = ((255,255,255))
        if A3.text == 'X' or A3.text == 'O':
            A3.color = ((255,255,255))

    draw(A4, WIN)
    if isOver(A4, pygame.mouse.get_pos()) == True:
        A4.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    A4.text = "X"
                    play = 2
                elif play == 2:
                    A4.text = "O"
                    play = 1
            else:
                A4.color = ((255,255,255))
        if A4.text == 'X' or A4.text == 'O':
            A4.color = ((255,255,255))

    draw(A5, WIN)
    if isOver(A5, pygame.mouse.get_pos()) == True:
        A5.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    A5.text = "X"
                    play = 2
                elif play == 2:
                    A5.text = "O"
                    play = 1
            else:
                A5.color = ((255,255,255))
        if A5.text == 'X' or A5.text == 'O':
            A5.color = ((255,255,255))

    draw(A6, WIN)
    if isOver(A6, pygame.mouse.get_pos()) == True:
        A6.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    A6.text = "X"
                    play = 2
                elif play == 2:
                    A6.text = "O"
                    play = 1
            else:
                A6.color = ((255,255,255))
        if A6.text == 'X' or A6.text == 'O':
            A6.color = ((255,255,255))

    draw(A7, WIN)
    if isOver(A7, pygame.mouse.get_pos()) == True:
        A7.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    A7.text = "X"
                    play = 2
                elif play == 2:
                    A7.text = "O"
                    play = 1
            else:
                A7.color = ((255,255,255))
        if A7.text == 'X' or A7.text == 'O':
            A7.color = ((255,255,255))

    draw(A8, WIN)
    if isOver(A8, pygame.mouse.get_pos()) == True:
        A8.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    A8.text = "X"
                    play = 2
                elif play == 2:
                    A8.text = "O"
                    play = 1
            else:
                A8.color = ((255,255,255))
        if A8.text == 'X' or A8.text == 'O':
            A8.color = ((255,255,255))

    draw(A9, WIN)
    if isOver(A9, pygame.mouse.get_pos()) == True:
        A9.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    A9.text = "X"
                    play = 2
                elif play == 2:
                    A9.text = "O"
                    play = 1
            else:
                A9.color = ((255,255,255))
        if A9.text == 'X' or A9.text == 'O':
            A9.color = ((255,255,255))

    draw(B1, WIN)
    if isOver(B1, pygame.mouse.get_pos()) == True:
        B1.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    B1.text = "X"
                    play = 2
                elif play == 2:
                    B1.text = "O"
                    play = 1
            else:
                B1.color = ((255,255,255))
        if B1.text == 'X' or B1.text == 'O':
            B1.color = ((255,255,255))

    draw(B2, WIN)
    if isOver(B2, pygame.mouse.get_pos()) == True:
        B2.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    B2.text = "X"
                    play = 2
                elif play == 2:
                    B2.text = "O"
                    play = 1
            else:
                B2.color = ((255,255,255))
        if B2.text == 'X' or B2.text == 'O':
            B2.color = ((255,255,255))

    draw(B3, WIN)
    if isOver(B3, pygame.mouse.get_pos()) == True:
        B3.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    B3.text = "X"
                    play = 2
                elif play == 2:
                    B3.text = "O"
                    play = 1
            else:
                B3.color = ((255,255,255))
        if B3.text == 'X' or B3.text == 'O':
            B3.color = ((255,255,255))

    draw(B4, WIN)
    if isOver(B4, pygame.mouse.get_pos()) == True:
        B4.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    B4.text = "X"
                    play = 2
                elif play == 2:
                    B4.text = "O"
                    play = 1
            else:
                B4.color = ((255,255,255))
        if B4.text == 'X' or B4.text == 'O':
            B4.color = ((255,255,255))

    draw(B5, WIN)
    if isOver(B5, pygame.mouse.get_pos()) == True:
        B5.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    B5.text = "X"
                    play = 2
                elif play == 2:
                    B5.text = "O"
                    play = 1
            else:
                B5.color = ((255,255,255))
        if B5.text == 'X' or B5.text == 'O':
            B5.color = ((255,255,255))

    draw(B6, WIN)
    if isOver(B6, pygame.mouse.get_pos()) == True:
        B6.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    B6.text = "X"
                    play = 2
                elif play == 2:
                    B6.text = "O"
                    play = 1
            else:
                B6.color = ((255,255,255))
        if B6.text == 'X' or A2.text == 'O':
            B6.color = ((255,255,255))

    draw(B7, WIN)
    if isOver(B7, pygame.mouse.get_pos()) == True:
        B7.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    B7.text = "X"
                    play = 2
                elif play == 2:
                    B7.text = "O"
                    play = 1
            else:
                B7.color = ((255,255,255))
        if B7.text == 'X' or B7.text == 'O':
            B7.color = ((255,255,255))

    draw(B8, WIN)
    if isOver(B8, pygame.mouse.get_pos()) == True:
        B8.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    B8.text = "X"
                    play = 2
                elif play == 2:
                    B8.text = "O"
                    play = 1
            else:
                B8.color = ((255,255,255))
        if B8.text == 'X' or B8.text == 'O':
            B8.color = ((255,255,255))

    draw(B9, WIN)
    if isOver(B9, pygame.mouse.get_pos()) == True:
        B9.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    B9.text = "X"
                    play = 2
                elif play == 2:
                    B9.text = "O"
                    play = 1
            else:
                B9.color = ((255,255,255))
        if B9.text == 'X' or A2.text == 'O':
            B9.color = ((255,255,255))

    draw(C1, WIN)
    if isOver(C1, pygame.mouse.get_pos()) == True:
        C1.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    C1.text = "X"
                    play = 2
                elif play == 2:
                    C1.text = "O"
                    play = 1
            else:
                C1.color = ((255,255,255))
        if C1.text == 'X' or C1.text == 'O':
            C1.color = ((255,255,255))

    draw(C2, WIN)
    if isOver(C2, pygame.mouse.get_pos()) == True:
        C2.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    C2.text = "X"
                    play = 2
                elif play == 2:
                    C2.text = "O"
                    play = 1
            else:
                C2.color = ((255,255,255))
        if C2.text == 'X' or C2.text == 'O':
            C2.color = ((255,255,255))

    draw(C3, WIN)
    if isOver(C3, pygame.mouse.get_pos()) == True:
        C3.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    C3.text = "X"
                    play = 2
                elif play == 2:
                    C3.text = "O"
                    play = 1
            else:
                C3.color = ((255,255,255))
        if C3.text == 'X' or C3.text == 'O':
            C3.color = ((255,255,255))


    draw(C4, WIN)
    if isOver(C4, pygame.mouse.get_pos()) == True:
        C4.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    C4.text = "X"
                    play = 2
                elif play == 2:
                    C4.text = "O"
                    play = 1
            else:
                C4.color = ((255,255,255))
        if C4.text == 'X' or C4.text == 'O':
            C4.color = ((255,255,255))

    draw(C5, WIN)
    if isOver(C5, pygame.mouse.get_pos()) == True:
        C5.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    C5.text = "X"
                    play = 2
                elif play == 2:
                    C5.text = "O"
                    play = 1
            else:
                C5.color = ((255,255,255))
        if C5.text == 'X' or C5.text == 'O':
            C5.color = ((255,255,255))

    draw(C6, WIN)
    if isOver(C6, pygame.mouse.get_pos()) == True:
        C6.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    C6.text = "X"
                    play = 2
                elif play == 2:
                    C6.text = "O"
                    play = 1
            else:
                C6.color = ((255,255,255))
        if C6.text == 'X' or C6.text == 'O':
            C6.color = ((255,255,255))

    draw(C7, WIN)
    if isOver(C7, pygame.mouse.get_pos()) == True:
        C7.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    C7.text = "X"
                    play = 2
                elif play == 2:
                    C7.text = "O"
                    play = 1
            else:
                C7.color = ((255,255,255))
        if C7.text == 'X' or C7.text == 'O':
            C7.color = ((255,255,255))

    draw(C8, WIN)
    if isOver(C8, pygame.mouse.get_pos()) == True:
        C8.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    C8.text = "X"
                    play = 2
                elif play == 2:
                    C8.text = "O"
                    play = 1
            else:
                C8.color = ((255,255,255))
        if C8.text == 'X' or C8.text == 'O':
            C8.color = ((255,255,255))

    draw(C9, WIN)
    if isOver(C9, pygame.mouse.get_pos()) == True:
        C9.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    C9.text = "X"
                    play = 2
                elif play == 2:
                    C9.text = "O"
                    play = 1
            else:
                C9.color = ((255,255,255))
        if C9.text == 'X' or C9.text == 'O':
            C9.color = ((255,255,255))

    draw(D1, WIN)
    if isOver(D1, pygame.mouse.get_pos()) == True:
        D1.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    D1.text = "X"
                    play = 2
                elif play == 2:
                    D1.text = "O"
                    play = 1
            else:
                D1.color = ((255,255,255))
        if D1.text == 'X' or D1.text == 'O':
            D1.color = ((255,255,255))

    draw(D2, WIN)
    if isOver(D2, pygame.mouse.get_pos()) == True:
        D2.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    D2.text = "X"
                    play = 2
                elif play == 2:
                    D2.text = "O"
                    play = 1
            else:
                D2.color = ((255,255,255))
        if D2.text == 'X' or D2.text == 'O':
            D2.color = ((255,255,255))

    draw(D3, WIN)
    if isOver(D3, pygame.mouse.get_pos()) == True:
        D3.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    D3.text = "X"
                    play = 2
                elif play == 2:
                    D3.text = "O"
                    play = 1
            else:
                D3.color = ((255,255,255))
        if D3.text == 'X' or D3.text == 'O':
            D3.color = ((255,255,255))

    draw(D4, WIN)
    if isOver(D4, pygame.mouse.get_pos()) == True:
        D4.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    D4.text = "X"
                    play = 2
                elif play == 2:
                    D4.text = "O"
                    play = 1
            else:
                D4.color = ((255,255,255))
        if D4.text == 'X' or D4.text == 'O':
            D4.color = ((255,255,255))

    draw(D5, WIN)
    if isOver(D5, pygame.mouse.get_pos()) == True:
        D5.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    D5.text = "X"
                    play = 2
                elif play == 2:
                    D5.text = "O"
                    play = 1
            else:
                D5.color = ((255,255,255))
        if D5.text == 'X' or D5.text == 'O':
            D5.color = ((255,255,255))

    draw(D6, WIN)
    if isOver(D6, pygame.mouse.get_pos()) == True:
        D6.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    D6.text = "X"
                    play = 2
                elif play == 2:
                    D6.text = "O"
                    play = 1
            else:
                D6.color = ((255,255,255))
        if D6.text == 'X' or D6.text == 'O':
            D6.color = ((255,255,255))

    draw(D7, WIN)
    if isOver(D7, pygame.mouse.get_pos()) == True:
        D7.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    D7.text = "X"
                    play = 2
                elif play == 2:
                    D7.text = "O"
                    play = 1
            else:
                D7.color = ((255,255,255))
        if D7.text == 'X' or D7.text == 'O':
            D7.color = ((255,255,255))

    draw(D8, WIN)
    if isOver(D8, pygame.mouse.get_pos()) == True:
        D8.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    D8.text = "X"
                    play = 2
                elif play == 2:
                    D8.text = "O"
                    play = 1
            else:
                D8.color = ((255,255,255))
        if D8.text == 'X' or D8.text == 'O':
            D8.color = ((255,255,255))

    draw(D9, WIN)
    if isOver(D9, pygame.mouse.get_pos()) == True:
        D9.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    D9.text = "X"
                    play = 2
                elif play == 2:
                    D9.text = "O"
                    play = 1
            else:
                D9.color = ((255,255,255))
        if D9.text == 'X' or D9.text == 'O':
            D9.color = ((255,255,255))

    draw(E1, WIN)
    if isOver(E1, pygame.mouse.get_pos()) == True:
        E1.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    E1.text = "X"
                    play = 2
                elif play == 2:
                    E1.text = "O"
                    play = 1
            else:
                E1.color = ((255,255,255))
        if E1.text == 'X' or E1.text == 'O':
            E1.color = ((255,255,255))

    draw(E2, WIN)
    if isOver(E2, pygame.mouse.get_pos()) == True:
        E2.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    E2.text = "X"
                    play = 2
                elif play == 2:
                    E2.text = "O"
                    play = 1
            else:
                E2.color = ((255,255,255))
        if E2.text == 'X' or E2.text == 'O':
            E2.color = ((255,255,255))

    draw(E3, WIN)
    if isOver(E3, pygame.mouse.get_pos()) == True:
        E3.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    E3.text = "X"
                    play = 2
                elif play == 2:
                    E3.text = "O"
                    play = 1
            else:
                E3.color = ((255,255,255))
        if E3.text == 'X' or E3.text == 'O':
            E3.color = ((255,255,255))

    draw(E4, WIN)
    if isOver(E4, pygame.mouse.get_pos()) == True:
        E4.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    E4.text = "X"
                    play = 2
                elif play == 2:
                    E4.text = "O"
                    play = 1
            else:
                E4.color = ((255,255,255))
        if E4.text == 'X' or E4.text == 'O':
            E4.color = ((255,255,255))

    draw(E5, WIN)
    if isOver(E5, pygame.mouse.get_pos()) == True:
        E5.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    E5.text = "X"
                    play = 2
                elif play == 2:
                    E5.text = "O"
                    play = 1
            else:
                E5.color = ((255,255,255))
        if E5.text == 'X' or E5.text == 'O':
            E5.color = ((255,255,255))

    draw(E6, WIN)
    if isOver(E6, pygame.mouse.get_pos()) == True:
        E6.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    E6.text = "X"
                    play = 2
                elif play == 2:
                    E6.text = "O"
                    play = 1
            else:
                E6.color = ((255,255,255))
        if E6.text == 'X' or E6.text == 'O':
            E6.color = ((255,255,255))

    draw(E7, WIN)
    if isOver(E7, pygame.mouse.get_pos()) == True:
        E7.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    E7.text = "X"
                    play = 2
                elif play == 2:
                    E7.text = "O"
                    play = 1
            else:
                E7.color = ((255,255,255))
        if E7.text == 'X' or E7.text == 'O':
            E7.color = ((255,255,255))

    draw(E8, WIN)
    if isOver(E8, pygame.mouse.get_pos()) == True:
        E8.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    E8.text = "X"
                    play = 2
                elif play == 2:
                    E8.text = "O"
                    play = 1
            else:
                E8.color = ((255,255,255))
        if E8.text == 'X' or E8.text == 'O':
            E8.color = ((255,255,255))

    draw(E9, WIN)
    if isOver(E9, pygame.mouse.get_pos()) == True:
        E9.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    E9.text = "X"
                    play = 2
                elif play == 2:
                    E9.text = "O"
                    play = 1
            else:
                E9.color = ((255,255,255))
        if E9.text == 'X' or E9.text == 'O':
            E9.color = ((255,255,255))

    draw(F1, WIN)
    if isOver(F1, pygame.mouse.get_pos()) == True:
        F1.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    F1.text = "X"
                    play = 2
                elif play == 2:
                    F1.text = "O"
                    play = 1
            else:
                F1.color = ((255,255,255))
        if F1.text == 'X' or F1.text == 'O':
            F1.color = ((255,255,255))

    draw(F2, WIN)
    if isOver(F2, pygame.mouse.get_pos()) == True:
        F2.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    F2.text = "X"
                    play = 2
                elif play == 2:
                    F2.text = "O"
                    play = 1
            else:
                F2.color = ((255,255,255))
        if F2.text == 'X' or F2.text == 'O':
            F2.color = ((255,255,255))

    draw(F3, WIN)
    if isOver(F3, pygame.mouse.get_pos()) == True:
        F3.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    F3.text = "X"
                    play = 2
                elif play == 2:
                    F3.text = "O"
                    play = 1
            else:
                F3.color = ((255,255,255))
        if F3.text == 'X' or F3.text == 'O':
            F3.color = ((255,255,255))

    draw(F4, WIN)
    if isOver(F4, pygame.mouse.get_pos()) == True:
        F4.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    F4.text = "X"
                    play = 2
                elif play == 2:
                    F4.text = "O"
                    play = 1
            else:
                F4.color = ((255,255,255))
        if F4.text == 'X' or F4.text == 'O':
            F4.color = ((255,255,255))

    draw(F5, WIN)
    if isOver(F5, pygame.mouse.get_pos()) == True:
        F5.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    F5.text = "X"
                    play = 2
                elif play == 2:
                    F5.text = "O"
                    play = 1
            else:
                F5.color = ((255,255,255))
        if F5.text == 'X' or F5.text == 'O':
            F5.color = ((255,255,255))

    draw(F6, WIN)
    if isOver(F6, pygame.mouse.get_pos()) == True:
        F6.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    F6.text = "X"
                    play = 2
                elif play == 2:
                    F6.text = "O"
                    play = 1
            else:
                F6.color = ((255,255,255))
        if F6.text == 'X' or F6.text == 'O':
            F6.color = ((255,255,255))

    draw(F7, WIN)
    if isOver(F7, pygame.mouse.get_pos()) == True:
        F7.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    F7.text = "X"
                    play = 2
                elif play == 2:
                    F7.text = "O"
                    play = 1
            else:
                F7.color = ((255,255,255))
        if F7.text == 'X' or F7.text == 'O':
            F7.color = ((255,255,255))

    draw(F8, WIN)
    if isOver(F8, pygame.mouse.get_pos()) == True:
        F8.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    F8.text = "X"
                    play = 2
                elif play == 2:
                    F8.text = "O"
                    play = 1
            else:
                F8.color = ((255,255,255))
        if F8.text == 'X' or F8.text == 'O':
            F8.color = ((255,255,255))

    draw(F9, WIN)
    if isOver(F9, pygame.mouse.get_pos()) == True:
        F9.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    F9.text = "X"
                    play = 2
                elif play == 2:
                    F9.text = "O"
                    play = 1
            else:
                F9.color = ((255,255,255))
        if F9.text == 'X' or F9.text == 'O':
            F9.color = ((255,255,255))

    draw(G1, WIN)
    if isOver(G1, pygame.mouse.get_pos()) == True:
        G1.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    G1.text = "X"
                    play = 2
                elif play == 2:
                    G1.text = "O"
                    play = 1
            else:
                G1.color = ((255,255,255))
        if G1.text == 'X' or G1.text == 'O':
            G1.color = ((255,255,255))

    draw(G2, WIN)
    if isOver(G2, pygame.mouse.get_pos()) == True:
        G2.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    G2.text = "X"
                    play = 2
                elif play == 2:
                    G2.text = "O"
                    play = 1
            else:
                G2.color = ((255,255,255))
        if G2.text == 'X' or G2.text == 'O':
            G2.color = ((255,255,255))

    draw(G3, WIN)
    if isOver(G3, pygame.mouse.get_pos()) == True:
        G3.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    G3.text = "X"
                    play = 2
                elif play == 2:
                    G3.text = "O"
                    play = 1
            else:
                G3.color = ((255,255,255))
        if G3.text == 'X' or G3.text == 'O':
            G3.color = ((255,255,255))

    draw(G4, WIN)
    if isOver(G4, pygame.mouse.get_pos()) == True:
        G4.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    G4.text = "X"
                    play = 2
                elif play == 2:
                    G4.text = "O"
                    play = 1
            else:
                G4.color = ((255,255,255))
        if G4.text == 'X' or G4.text == 'O':
            G4.color = ((255,255,255))

    draw(G5, WIN)
    if isOver(G5, pygame.mouse.get_pos()) == True:
        G5.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    G5.text = "X"
                    play = 2
                elif play == 2:
                    G5.text = "O"
                    play = 1
            else:
                G5.color = ((255,255,255))
        if G5.text == 'X' or G5.text == 'O':
            G5.color = ((255,255,255))

    draw(G6, WIN)
    if isOver(G6, pygame.mouse.get_pos()) == True:
        G6.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    G6.text = "X"
                    play = 2
                elif play == 2:
                    G6.text = "O"
                    play = 1
            else:
                G6.color = ((255,255,255))
        if G6.text == 'X' or G6.text == 'O':
            G6.color = ((255,255,255))

    draw(G7, WIN)
    if isOver(G7, pygame.mouse.get_pos()) == True:
        G7.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    G7.text = "X"
                    play = 2
                elif play == 2:
                    G7.text = "O"
                    play = 1
            else:
                G7.color = ((255,255,255))
        if G7.text == 'X' or G7.text == 'O':
            G7.color = ((255,255,255))

    draw(G8, WIN)
    if isOver(G8, pygame.mouse.get_pos()) == True:
        G8.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    G8.text = "X"
                    play = 2
                elif play == 2:
                    G8.text = "O"
                    play = 1
            else:
                G8.color = ((255,255,255))
        if G8.text == 'X' or G8.text == 'O':
            G8.color = ((255,255,255))

    draw(G9, WIN)
    if isOver(G9, pygame.mouse.get_pos()) == True:
        G9.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    G9.text = "X"
                    play = 2
                elif play == 2:
                    G9.text = "O"
                    play = 1
            else:
                G9.color = ((255,255,255))
        if G9.text == 'X' or G9.text == 'O':
            G9.color = ((255,255,255))

    draw(H1, WIN)
    if isOver(H1, pygame.mouse.get_pos()) == True:
        H1.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    H1.text = "X"
                    play = 2
                elif play == 2:
                    H1.text = "O"
                    play = 1
            else:
                H1.color = ((255,255,255))
        if H1.text == 'X' or H1.text == 'O':
            H1.color = ((255,255,255))

    draw(H2, WIN)
    if isOver(H2, pygame.mouse.get_pos()) == True:
        H2.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    H2.text = "X"
                    play = 2
                elif play == 2:
                    H2.text = "O"
                    play = 1
            else:
                H2.color = ((255,255,255))
        if H2.text == 'X' or A2.text == 'O':
            H2.color = ((255,255,255))

    draw(H3, WIN)
    if isOver(H3, pygame.mouse.get_pos()) == True:
        H3.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    H3.text = "X"
                    play = 2
                elif play == 2:
                    H3.text = "O"
                    play = 1
            else:
                H3.color = ((255,255,255))
        if H3.text == 'X' or H3.text == 'O':
            H3.color = ((255,255,255))

    draw(H4, WIN)
    if isOver(H4, pygame.mouse.get_pos()) == True:
        H4.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    H4.text = "X"
                    play = 2
                elif play == 2:
                    H4.text = "O"
                    play = 1
            else:
                H4.color = ((255,255,255))
        if H4.text == 'X' or A2.text == 'O':
            H4.color = ((255,255,255))

    draw(H5, WIN)
    if isOver(H5, pygame.mouse.get_pos()) == True:
        H5.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    H5.text = "X"
                    play = 2
                elif play == 2:
                    H5.text = "O"
                    play = 1
            else:
                H5.color = ((255,255,255))
        if H5.text == 'X' or H5.text == 'O':
            H5.color = ((255,255,255))

    draw(H6, WIN)
    if isOver(H6, pygame.mouse.get_pos()) == True:
        H6.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    H6.text = "X"
                    play = 2
                elif play == 2:
                    H6.text = "O"
                    play = 1
            else:
                H6.color = ((255,255,255))
        if H6.text == 'X' or H6.text == 'O':
            H6.color = ((255,255,255))

    draw(H7, WIN)
    if isOver(H7, pygame.mouse.get_pos()) == True:
        H7.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    H7.text = "X"
                    play = 2
                elif play == 2:
                    H7.text = "O"
                    play = 1
            else:
                H7.color = ((255,255,255))
        if H7.text == 'X' or H7.text == 'O':
            H7.color = ((255,255,255))

    draw(H8, WIN)
    if isOver(H8, pygame.mouse.get_pos()) == True:
        H8.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    H8.text = "X"
                    play = 2
                elif play == 2:
                    H8.text = "O"
                    play = 1
            else:
                H8.color = ((255,255,255))
        if H8.text == 'X' or H8.text == 'O':
            H8.color = ((255,255,255))

    draw(H9, WIN)
    if isOver(H9, pygame.mouse.get_pos()) == True:
        H9.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    H9.text = "X"
                    play = 2
                elif play == 2:
                    H9.text = "O"
                    play = 1
            else:
                H9.color = ((255,255,255))
        if H9.text == 'X' or H9.text == 'O':
            H9.color = ((255,255,255))

    draw(I1, WIN)
    if isOver(I1, pygame.mouse.get_pos()) == True:
        I1.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    I1.text = "X"
                    play = 2
                elif play == 2:
                    I1.text = "O"
                    play = 1
            else:
                I1.color = ((255,255,255))
        if I1.text == 'X' or I1.text == 'O':
            I1.color = ((255,255,255))

    draw(I2, WIN)
    if isOver(I2, pygame.mouse.get_pos()) == True:
        I2.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    I2.text = "X"
                    play = 2
                elif play == 2:
                    I2.text = "O"
                    play = 1
            else:
                I2.color = ((255,255,255))
        if I2.text == 'X' or I2.text == 'O':
            I2.color = ((255,255,255))

    draw(I3, WIN)
    if isOver(I3, pygame.mouse.get_pos()) == True:
        I3.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    I3.text = "X"
                    play = 2
                elif play == 2:
                    I3.text = "O"
                    play = 1
            else:
                I3.color = ((255,255,255))
        if I3.text == 'X' or I3.text == 'O':
            I3.color = ((255,255,255))

    draw(I4, WIN)
    if isOver(I4, pygame.mouse.get_pos()) == True:
        I4.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    I4.text = "X"
                    play = 2
                elif play == 2:
                    I4.text = "O"
                    play = 1
            else:
                I4.color = ((255,255,255))
        if I4.text == 'X' or I4.text == 'O':
            I4.color = ((255,255,255))

    draw(I5, WIN)
    if isOver(I5, pygame.mouse.get_pos()) == True:
        I5.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    I5.text = "X"
                    play = 2
                elif play == 2:
                    I5.text = "O"
                    play = 1
            else:
                I5.color = ((255,255,255))
        if I5.text == 'X' or I5.text == 'O':
            I5.color = ((255,255,255))

    draw(I6, WIN)
    if isOver(I6, pygame.mouse.get_pos()) == True:
        I6.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    I6.text = "X"
                    play = 2
                elif play == 2:
                    I6.text = "O"
                    play = 1
            else:
                I6.color = ((255,255,255))
        if I6.text == 'X' or I6.text == 'O':
            I6.color = ((255,255,255))

    draw(I7, WIN)
    if isOver(I7, pygame.mouse.get_pos()) == True:
        I7.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    I7.text = "X"
                    play = 2
                elif play == 2:
                    I7.text = "O"
                    play = 1
            else:
                I7.color = ((255,255,255))
        if I7.text == 'X' or I7.text == 'O':
            I7.color = ((255,255,255))

    draw(I8, WIN)
    if isOver(I8, pygame.mouse.get_pos()) == True:
        I8.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    I8.text = "X"
                    play = 2
                elif play == 2:
                    I8.text = "O"
                    play = 1
            else:
                I8.color = ((255,255,255))
        if I8.text == 'X' or I8.text == 'O':
            I8.color = ((255,255,255))

    draw(I9, WIN)
    if isOver(I9, pygame.mouse.get_pos()) == True:
        I9.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play == 1:
                    I9.text = "X"
                    play = 2
                elif play == 2:
                    I9.text = "O"
                    play = 1
            else:
                I9.color = ((255,255,255))
        if I9.text == 'X' or I9.text == 'O':
            I9.color = ((255,255,255))


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
