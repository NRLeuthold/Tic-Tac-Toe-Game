import pygame
import main

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
elem = []

def pull_apart(tile=''):
    for i in tile:
        if i in letters:
            let = i
        elif int(i) in range(0, 10):
            x = num.index(i)
            y = list(str(x))
            for ii in y:
                elem.append(num[int(ii)])
                for iii in elem:
                    row(iii, let)
                    
                    

def row(iii, let):
    if iii=='1':
        iii1 = int(iii) + 1
        iii2 = int(iii) + 2

        iii1 = str(let) + str(iii1)
        iii2 = str(let) + str(iii2)

        dict = {iii1:str(let) + str(iii1), iii2:str(let) + str(iii2)}

        if dict[iii1].text == dict[iii2].text:
            message = "Victory"
            return message

    if iii=='2':
        pass

    if iii=='3':
        pass

    if iii=='4':
        pass

    if iii=='4':
        pass
    
    if iii=='5':
        pass
    
    if iii=='6':
        pass
    
    if iii=='7':
        pass
    
    if iii=='8':
        pass
    
    if iii=='9':
        pass


def col(iii):
    pass

def diag(iii):
    pass

####################################################################################################

