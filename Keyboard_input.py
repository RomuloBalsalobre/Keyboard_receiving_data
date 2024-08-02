import time
import keyboard


mapa = [10,10]
wall = []
posicao = [1,1]
direcao = ''
tiro = False
bala = [0,0]
roda = False

while(True):

    for i in range(mapa[0]):
        for j in range(mapa[1]):
            if i == 0 or i == (mapa[0]-1) or j == 0 or j == (mapa[1]-1):
                wall.append('$')
            else:
                if i == posicao[0] and j == posicao[1]:
                    wall.append('P')
                elif tiro == True and j == bala[1] and i == bala[0]: 
                    wall.append('*')
                else:
                    wall.append(' ')
        print(str(wall).strip('[]').replace(',', '').replace("'", ''))
        wall.clear()


    #detecta se o usuario apertou a seta no teclado
    if keyboard.is_pressed('d'):
        direcao = 'd'
    if keyboard.is_pressed('a'):
        direcao = 'e'
    if keyboard.is_pressed('w'):
        direcao = 'c'
    if keyboard.is_pressed('s'):
        direcao = 'b'
    #se apartar a barra de espaço atira
    if keyboard.is_pressed('space'):
        bala[0] = posicao[0]
        bala[1] = posicao[1]+1 
        tiro = True 


    if  direcao == 'd':
        if posicao[1] < mapa[1]-2:
            posicao[1] += 1
        direcao = ''
    if direcao == 'b':
        if posicao[0] < mapa[0]-2:
            posicao[0] += 1
        direcao = ''
    if direcao == 'c':
        if posicao[0] > 1:
            posicao[0] -= 1
        direcao = ''
    if direcao == 'e':
        if posicao[1] > 1:
            posicao[1] -= 1
        direcao = ''
    if tiro == True:

        bala[1] += 1

    time.sleep(0.1)
    print('\033c')


    

