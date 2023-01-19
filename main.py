import random
import pygame
from pygame import mixer
pygame.init()
#TODO: importar modulos individuales en vez de librerias completas
ANCHO = 800
ALTO = 410
anchoContainer = 740
altoContainer = 250
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('Roboto-Bold.ttf', 32)
#TODO: borrar colores no usados al final
darkBlue = (0,40,58)
yellow = (248,178,1)
cafe = (198,113,0)
white = (255, 255, 230)
blue = (1,171,183)
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
inputBox = pygame.draw.rect(screen, gold, [(ANCHO//2) - 150, 315, 300, 50], 0, 5)
btnOtroEjer = pygame.draw.rect(screen, darkBlue, [(ANCHO//2) - 350, 315, 150, 40], 0, 7)
btnComprobar = pygame.draw.rect(screen, darkBlue, [(ANCHO//2) + 170, 350, 150, 40], 0, 7)
lblCurrentScale = pygame.draw.rect(screen, darkBlue, [(ANCHO//2) + 170, 300, 190, 40], 0, 7)
#colores para la caja de entrada detexto
color_inactive = blue
color_active = (0,0,0)
colorInput = color_inactive
active = False
inputStr = ''


soundList = [soundDo1, soundDi, soundRe, soundRi, soundMi, soundFa,
soundFi, soundSol, soundSi, soundLa, soundLi, soundTi, soundDo2]
soundList_copy = soundList.copy()
def shuffleNotes():
    random.shuffle(soundList_copy)
random.shuffle(soundList_copy)

while run:
    timer.tick(fps)
    # screen.fill(cafe)
    # drawGraphs()
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