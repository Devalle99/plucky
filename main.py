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
fps = 60
timer = pygame.time.Clock()
darkBlue = (64*0.5,130*0.5,159*0.5)
mostaza = (213,128,41)
amarillo = (223,170,36)
gold = (212, 175, 55)
screen = pygame.display.set_mode([ANCHO, ALTO])
run = True
inputStr = ''

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
soundList = [soundDo1, soundDi, soundRe, soundRi, soundMi, soundFa,
soundFi, soundSol, soundSi, soundLa, soundLi, soundTi]
soundList_copy = soundList.copy()

#----------------------------graficos fijos-----------------------
screen.fill(mostaza)
pygame.draw.rect(screen, darkBlue, [30, 35, anchoContainer, altoContainer], 0, 10)
#teclas blancas
for i in range(7):
    pygame.draw.rect(screen, amarillo, [i*86 + 60, 140, 72, 72], 0, 3)
#primeras 2 teclas negras
for i in range(2):
    pygame.draw.rect(screen, amarillo, [i*86 + 110, 55, 72, 72], 0, 3)
#ultimas 3 teclas negras
for i in range(3):
    pygame.draw.rect(screen, amarillo, [i*86 + 365, 55, 72, 72], 0, 3)
inputBox = pygame.draw.rect(screen, (255,255,180), [(ANCHO//2) - 150, 315, 300, 50], 0, 5)
btnOtroEjer = pygame.draw.rect(screen, darkBlue, [50, 315, 180, 43], 5, 7)
btnComprobar = pygame.draw.rect(screen, darkBlue, [570, 350, 190, 40], 5, 7)
lblCurrentScale = pygame.draw.rect(screen, darkBlue, [570, 300, 190, 40], 5, 7)
#colores para la caja de entrada de texto
colorPassive = mostaza
colorActive = 'black'
colorInput = colorPassive
passive = False

# texto
font1 = pygame.font.SysFont(None, 90)
font2 = pygame.font.SysFont(None, 35)
whiteKeys = font1.render('z   x   c   v   b   n   m', True, 'black')
screen.blit(whiteKeys, (75, 145))
blackKeys = font1.render('s   d        g   h   j', True, 'black')
screen.blit(blackKeys, (125, 60))
currentScale = font2.render('Jonico', True, 'black')
screen.blit(currentScale, (585, 308))
comprobar = font2.render('comprobar', True, 'black')
screen.blit(comprobar, (598, 357))
otroEj = font2.render('Otro ejercicio', True, 'black')
screen.blit(otroEj, (58, 323))

def pickScale():
    lidio = 'zxcgbnm'
    jonico = 'zxcvbnm,'
    mixolidio = 'zxcvbnj'
    dorico = 'zxdvbnj,'
    eolico = 'zxdvbhj'
    frigio = 'zsdvbhj'
    locrio = 'zsdvghj'
    pentMin = 'zdvbj'
    scales = [['Lidio', lidio], ['Jónico', jonico], ['Mixolidio', mixolidio], ['Dórico', dorico], 
    ['Eólico', eolico], ['Frigio', frigio], ['Locrio', locrio], ['Pentatónica menor', pentMin]]
    randScales = random.choice(scales)
    return randScales
pickScale()

while run:
    timer.tick(fps)
    # -----------------?????------------------
    # text_surface = font2.render(inputStr, True, 'black')
    # screen.blit(text_surface, (inputBox.x+8, inputBox.y+13))
    # inputBox.width = max(300, text_surface.get_width()+10)
    # ------------------?????--------------------
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
                if btnOtroEjer.collidepoint(event.pos):
                    pickScale()
                    inputStr=''
        if event.type == pygame.KEYDOWN:
            if passive == True:
                # if event.key == pygame.K_RETURN:
                #     pass
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

    pygame.draw.rect(screen, colorInput, inputBox, 3, 5)
    text_surface = font2.render(inputStr, True, 'black')
    screen.blit(text_surface, (inputBox.x+8, inputBox.y+13))
    inputBox.width = max(300, text_surface.get_width()+10)

    pygame.display.flip()
pygame.quit()