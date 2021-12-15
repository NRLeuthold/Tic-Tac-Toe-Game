import pygame
from pygame import color
pygame.init()

WIDTH, HEIGHT = 500,500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

white = (255,255,255)

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

start = button(white, 200, 225, 100, 50, text='START')


while True:

    draw(start, WIN)
    if isOver(start, pygame.mouse.get_pos()) == True:
        start.color = (255,255,0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                WIN.fill((0,255,0))
    else:
        start.color = (255,255,255)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    pygame.display.update()
