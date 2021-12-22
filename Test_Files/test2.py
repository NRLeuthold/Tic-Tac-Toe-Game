import pygame

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
elem = []

def checkWin(tile=''):
    for i in tile:
        if i in letters:
            #print(i)
            pass
        elif int(i) in range(0, 10):
            #print(i)
            x = num.index(i)
            y = list(str(x))
            #print(y)
            for ii in y:
                elem.append(num[int(ii)])
                for iii in elem:
                    #Add 1 and 2 and use that as indexes for num list, use that to check for wins
            #print(elem)

            
checkWin('A1')
