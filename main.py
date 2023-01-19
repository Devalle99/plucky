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
font = pygame.font.Font('Roboto-Bold.ttf', 32)
#TODO: borrar colores no usados al final
darkBlue = (64*0.5,130*0.5,159*0.5)
yellow = (248,178,1)
cafe = (213,128,41)
white = (255, 255, 230)
blue = (223,170,36)
red = (255, 0, 0)
green = (0, 200, 50)
gold = (212, 175, 55)
screen = pygame.display.set_mode([ANCHO, ALTO])
run = True


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

assoDict = {
0 : soundDo1,
1 : soundDi,
2 : soundRe,
3 : soundRi,
4 : soundMi,
5 : soundFa,
6 : soundFi,
7 : soundSol,
8 : soundSi,
9 : soundLa,
10 : soundLi,
11 : soundTi,
12 : soundDo2
}
#----------------------------graficos fijos-----------------------
screen.fill(cafe)
#caja negra contenedora
pygame.draw.rect(screen, darkBlue, [30, 35, anchoContainer, altoContainer], 0, 10)
#teclas blancas
for i in range(8):
    pygame.draw.rect(screen, blue, [i*(anchoContainer//8 - 6) + 60, 140, (anchoContainer//8 - 20), (anchoContainer//8 - 20)], 0, 3)
#primeras 2 teclas negras
for i in range(2):
    pygame.draw.rect(screen, blue, [i*(anchoContainer//8 - 6) + 110, 55, (anchoContainer//8 - 20), (anchoContainer//8 - 20)], 0, 3)
#ultimas 3 teclas negras
for i in range(3):
    pygame.draw.rect(screen, blue, [i*(anchoContainer//8 - 6) + 365, 55, (anchoContainer//8 - 20), (anchoContainer//8 - 20)], 0, 3)
#barra espaciadora referencia tonica
pygame.draw.rect(screen, blue, [ANCHO//2 - 200, 225, 395, 40], 0, 3)
#la parte inferior
# inputBox = pygame.draw.rect(screen, gold, [(ANCHO//2) - 150, 315, 300, 50], 0, 5)
btnOtroEjer = pygame.draw.rect(screen, darkBlue, [(ANCHO//2) - 350, 315, 180, 43], 5, 7)
btnComprobar = pygame.draw.rect(screen, darkBlue, [(ANCHO//2) + 170, 350, 190, 40], 5, 7)
lblCurrentScale = pygame.draw.rect(screen, darkBlue, [(ANCHO//2) + 170, 300, 190, 40], 5, 7)
#colores para la caja de entrada detexto
color_inactive = 'white'
color_active = 'black'
colorInput = color_inactive
active = False
inputStr = ''

# texto
font1 = pygame.font.SysFont(None, 90)
font2 = pygame.font.SysFont(None, 35)
whiteKeys = font1.render('z   x   c   v   b   n   m   ,', True, 'black')
screen.blit(whiteKeys, (75, 145))
blackKeys = font1.render('s   d        g   h   j', True, 'black')
screen.blit(blackKeys, (125, 60))
currentScale = font2.render('Jonico', True, 'black')
screen.blit(currentScale, (585, 308))
comprobar = font2.render('comprobar', True, 'black')
screen.blit(comprobar, (598, 357))
otroEj = font2.render('Otro ejercicio', True, 'black')
screen.blit(otroEj, (58, 323))

userText = ''
soundList = [soundDo1, soundDi, soundRe, soundRi, soundMi, soundFa,
soundFi, soundSol, soundSi, soundLa, soundLi, soundTi, soundDo2]
soundList_copy = soundList.copy()
def shuffleNotes():
    random.shuffle(soundList_copy)
# llamar a random antes de que empiece el loop
random.shuffle(soundList_copy)

while run:
    timer.tick(fps)
    # -----------------------------------
    # draw rectangle and argument passed which should
    # be on screen
    inputBox = pygame.draw.rect(screen, gold, [(ANCHO//2) - 150, 315, 300, 50], 0, 5)
    text_surface = font2.render(userText, True, ('black'))
    # render at position stated in arguments
    screen.blit(text_surface, (inputBox.x+8, inputBox.y+13))
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    inputBox.w = max(300, text_surface.get_width()+10)
    # --------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if inputBox.collidepoint(event.pos):
                    # cuando haces click en la caja se activa, la var active empieza siendo falsa
                    active = not active
                else:
                    active = False
                # Cambia el color actual de la caja de input
                colorInput = color_active if active else color_inactive

                if btnOtroEjer.collidepoint(event.pos):
                    shuffleNotes()
        if event.type == pygame.KEYDOWN:

            # Check for backspace
            if event.key == pygame.K_BACKSPACE: 
                # get text input from 0 to -1 i.e. end.
                userText = userText[:-1]  
            else:
                userText += event.unicode
            
            if event.key == pygame.K_SPACE:
                soundDo1.play()

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
    #funcionalidad input box
    txt_surface = font.render(inputStr, True, colorInput)
    screen.blit(txt_surface, (inputBox.x+7, inputBox.y+10))
    pygame.draw.rect(screen, colorInput, inputBox, 3, 5)

    pygame.display.flip()
    timer.tick(fps)
pygame.quit()