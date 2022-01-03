import pygame
import main
pygame.display.init()
pygame.init()

icon = pygame.image.load("Assets/board_icon.png")
pygame.display.set_icon(icon)

WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption("Tic-Tac-Toe")

white = (255,255,255)
dark_red = (153,0,0)

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
        pygame.draw.rect(WIN, outline, (self.x,self.y,self.width+2,self.height+2),0)
    
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

running = True
pygame.display.init()

while running:
    x, y = WIN.get_size()

    x_pos = x * .4
    y_pos = y * .45

    x_wid = x * .2
    y_hei = y * .1

    if x_wid < 75:
        x_wid = 75
    
    if y_hei < 22:
        y_hei = 22

    start = button((255,0,0), x_pos, y_pos, x_wid, y_hei, text='START')

    draw(start, WIN, outline=dark_red)
    if isOver(start, pygame.mouse.get_pos()) == True:
        start.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                main.main()
    else:
        start.color = (255,255,255)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()