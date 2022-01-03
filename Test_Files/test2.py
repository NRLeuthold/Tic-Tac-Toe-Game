import pygame

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
elem = []

def checkWin(tile=''):
    for i in tile:
        if i in letters:
            let = i
        elif int(i) in range(0, 10):
            x = num.index(i)
            y = list(str(x))
            for ii in y:
                elem.append(num[int(ii)])
                for iii in elem:
                    if iii=='1' or iii=='4' or iii=='7':
                        iii1 = int(iii) + 1
                        iii2 = int(iii) + 2
                        iii1 = str(let) + str(iii1)
                        iii2 = str(let) + str(iii2)
                        return iii1
                        return iii2
                    elif iii=='2' or iii=='5' or iii=='8':
                        iii1 = int(iii) - 1
                        iii2 = int(iii) + 1
                        iii1 = str(let) + str(iii1)
                        iii2 = str(let) + str(iii2)
                        return iii1
                        return iii2
                    elif iii=='3' or iii=='6' or iii=='9':
                        iii1 = int(iii) - 1
                        iii2 = int(iii) - 2
                        iii1 = str(let) + str(iii1)
                        iii2 = str(let) + str(iii2)
                        return iii1
                        return iii2
                    else:
                        print("Out of Range: 3")

            
checkWin('A1')
