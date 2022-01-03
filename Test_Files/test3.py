class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

white = (255,255,255)

A1 = button(white, 50, 50, 20, 20, text='Hello World')

var = 'A1'

print(locals()[var].text)