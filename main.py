import random
import pygame
from pygame import mixer
pygame.init()
pygame.mixer.init()
#TODO: importar modulos individuales en vez de librerias completas
ANCHO = 800
ALTO = 410
anchoContainer = 740
altoContainer = 250
fps = 30
timer = pygame.time.Clock()
darkBlue = (64*0.4,130*0.5,159*0.5)
mostaza = (213,128,41)
amarillo = (223,170,36)
gold = (212, 175, 55)
screen = pygame.display.set_mode([ANCHO, ALTO])
run = True

soundWin = pygame.mixer.Sound('sounds\win.wav')
soundLoss = pygame.mixer.Sound('sounds\loss.wav')
soundDo1 = pygame.mixer.Sound('sounds\do1Note.wav')
soundDi = pygame.mixer.Sound('sounds\diNote.wav')
soundRe = pygame.mixer.Sound('sounds\\reNote.wav')
soundRi = pygame.mixer.Sound('sounds\\riNote.wav')
soundMi = pygame.mixer.Sound('sounds\miNote.wav')
soundFa = pygame.mixer.Sound('sounds\\faNote.wav')
soundFi = pygame.mixer.Sound('sounds\\fiNote.wav')
soundSol = pygame.mixer.Sound('sounds\solNote.wav')
soundSi = pygame.mixer.Sound('sounds\siNote.wav')
soundLa = pygame.mixer.Sound('sounds\laNote.wav')
soundLi = pygame.mixer.Sound('sounds\liNote.wav')
soundTi = pygame.mixer.Sound('sounds\\tiNote.wav')
soundDo2 = pygame.mixer.Sound('sounds\do2Note.wav')
soundList = [soundDo1, soundDi, soundRe, soundRi, soundMi, soundFa,
soundFi, soundSol, soundSi, soundLa, soundLi, soundTi, soundDo2]
soundList_copy = soundList.copy()

#colores para la caja de entrada de texto
colorPassive = (250,200,110)
colorActive = 'black'
colorInput = colorPassive
passive = False

# texto
font1 = pygame.font.Font('Roboto-Bold.ttf', 60)
font2 = pygame.font.Font('Roboto-Bold.ttf', 25)
inputStr = ''

def pickScale():
    lidio = 'zxcgbnm,'
    jonico = 'zxcvbnm,'
    mixolidio = 'zxcvbnj,'
    dorico = 'zxdvbnj,'
    eolico = 'zxdvbhj,'
    frigio = 'zsdvbhj,'
    locrio = 'zsdvghj,'
    pentMin = 'zdvbj,'
    scales = [['Lidio', lidio], ['Jónico', jonico], ['Mixolidio', mixolidio], ['Dórico', dorico], 
    ['Eólico', eolico], ['Frigio', frigio], ['Locrio', locrio], ['Pent. menor', pentMin]]
    randScales = random.choice(scales)
    return randScales
currentScale = pickScale()
altoTeclas = 95
while run:
    screen.fill(mostaza)
    #----------------------------graficos fijos-----------------------
    pygame.draw.rect(screen, darkBlue, [30, 35, anchoContainer, altoContainer], 0, 10)
    #teclas blancas
    for i in range(8):
        pygame.draw.rect(screen, 'white', [i*86 + 60, 165, 72, altoTeclas], 0, 3)
    #primeras 2 teclas negras
    for i in range(2):
        pygame.draw.rect(screen, 'black', [i*86 + 110, 55, 72, altoTeclas], 0, 3)
        # pygame.draw.rect(screen, amarillo, [i*86 + 110, 55, 72, 72], 0, 3)
    #ultimas 3 teclas negras
    for i in range(3):
        pygame.draw.rect(screen, 'black', [i*86 + 365, 55, 72, altoTeclas], 0, 3)
    inputBox = pygame.draw.rect(screen, (255,255,180), [(ANCHO//2) - 150, 315, 300, 50], 0, 5)
    btnOtroEjer = pygame.draw.rect(screen, darkBlue, [50, 315, 180, 43], 5, 7)
    btnComprobar = pygame.draw.rect(screen, darkBlue, [570, 350, 190, 40], 5, 7)
    lblCurrentScale = pygame.draw.rect(screen, darkBlue, [570, 300, 190, 40], 5, 7)

    whiteKeys = font1.render('Z', True, 'black')
    screen.blit(whiteKeys, (77, 178))
    whiteKeys = font1.render('X', True, 'black')
    screen.blit(whiteKeys, (162, 178))
    whiteKeys = font1.render('C', True, 'black')
    screen.blit(whiteKeys, (247, 178))
    whiteKeys = font1.render('V', True, 'black')
    screen.blit(whiteKeys, (333, 178))
    whiteKeys = font1.render('B', True, 'black')
    screen.blit(whiteKeys, (420, 178))
    whiteKeys = font1.render('N', True, 'black')
    screen.blit(whiteKeys, (504, 178))
    whiteKeys = font1.render('M', True, 'black')
    screen.blit(whiteKeys, (585, 178))
    whiteKeys = font1.render(',', True, 'black')
    screen.blit(whiteKeys, (690, 170))
    
    blackKeys = font1.render('S', True, 'white')
    screen.blit(blackKeys, (127, 68))
    blackKeys = font1.render('D', True, 'white')
    screen.blit(blackKeys, (213, 68))
    blackKeys = font1.render('G', True, 'white')
    screen.blit(blackKeys, (380, 68))
    blackKeys = font1.render('H', True, 'white')
    screen.blit(blackKeys, (466, 68))
    blackKeys = font1.render('J', True, 'white')
    screen.blit(blackKeys, (555, 68))
    comprobar = font2.render('Comprobar', True, 'black')
    screen.blit(comprobar, (598, 354))
    otroEj = font2.render('Otro ejercicio', True, 'black')
    screen.blit(otroEj, (63, 320))
    #-------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputBox.collidepoint(event.pos):
                # cambia el estado de passive
                passive = not passive
            else:
                passive = False
            colorInput = colorActive if passive else colorPassive
            if btnComprobar.collidepoint(event.pos):
                if inputStr == currentScale[1]:
                    # lblCorrecto = font2.render('Correcto', True, 'green')
                    # screen.blit(lblCorrecto, (335, 323))
                    soundWin.play()        
                else:
                    # lblIncorrecto = font2.render('Incorrecto', True, 'red')
                    # screen.blit(lblIncorrecto, (335, 323))
                    soundLoss.play()
            if btnOtroEjer.collidepoint(event.pos):
                pygame.draw.rect(screen, mostaza, [575, 305, 180, 30], 0, 7)
                currentScale = pickScale()
                inputStr=''
        if event.type == pygame.KEYDOWN:
            if passive == True:
                if event.key == pygame.K_RETURN:
                    pass
                if event.key == pygame.K_BACKSPACE:
                    inputStr = inputStr[:-1]
                else:
                    inputStr += event.unicode    
            if event.key == pygame.K_z:
                soundList_copy[0].play()
            if event.key == pygame.K_s:
                soundList_copy[1].play()
            if event.key == pygame.K_x:
                soundList_copy[2].play()
            if event.key == pygame.K_d:
                soundList_copy[3].play()
            if event.key == pygame.K_c:
                soundList_copy[4].play()
            if event.key == pygame.K_v:
                soundList_copy[5].play()
            if event.key == pygame.K_g:
                soundList_copy[6].play()
            if event.key == pygame.K_b:
                soundList_copy[7].play()
            if event.key == pygame.K_h:
                soundList_copy[8].play()
            if event.key == pygame.K_n:
                soundList_copy[9].play()
            if event.key == pygame.K_j:
                soundList_copy[10].play()
            if event.key == pygame.K_m:
                soundList_copy[11].play()
            if event.key == pygame.K_COMMA:
                soundList_copy[12].play()
    
    lblCurrent = font2.render(str(currentScale[0]), True, 'black')
    screen.blit(lblCurrent, (585, 304))
    pygame.draw.rect(screen, colorInput, inputBox, 3, 5)
    lblInput = font2.render(inputStr, True, 'black')
    screen.blit(lblInput, (inputBox.x+8, inputBox.y+13))
    inputBox.width = max(300, lblInput.get_width()+10)
    timer.tick(fps)
    pygame.display.flip()
pygame.quit()