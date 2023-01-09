import random
import pygame
from pygame import mixer
pygame.init()
# TODO: importar modulos individuales en vez de librerias completas
ANCHO = 800
ALTO = 400
anchoContainer = 740
altoContainer = 250
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
#TODO: borrar colores no usados al final
black = (0,40,58)
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

assoList = [soundDo1, soundDi, soundRe, soundRi, soundMi, soundFa,
soundFi, soundSol, soundSi, soundLa, soundLi, soundTi, soundDo2]

assoList_copy = assoList.copy()



def drawGraphs():
    #caja negra contenedora
    pygame.draw.rect(screen, black, [30, 35, anchoContainer, altoContainer], 0, 10)
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
    #rectangulo vacio
    pygame.draw.rect(screen, blue, [0,0,0,0])

while run:
    timer.tick(fps)
    screen.fill(cafe)
    drawGraphs()
    #-----------------shuffle asso dict-------------------
    keys = list(asso.keys())
    random.shuffle(keys)
    shuffledAsso = dict()
    for key in keys:
        shuffledAsso.update({key: asso[key]})
    #-----------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                soundDo1.play()
            if event.key == pygame.K_z:
                shuffledAsso.get(0).play()
            if event.key == pygame.K_s:
                shuffledAsso.get(1).play()
            if event.key == pygame.K_x:
                shuffledAsso.get(2).play()
            if event.key == pygame.K_d:
                shuffledAsso.get(3).play()
            if event.key == pygame.K_c:
                shuffledAsso.get(4).play()
            if event.key == pygame.K_v:
                shuffledAsso.get(5).play()
            if event.key == pygame.K_g:
                shuffledAsso.get(6).play()
            if event.key == pygame.K_b:
                shuffledAsso.get(7).play()
            if event.key == pygame.K_h:
                shuffledAsso.get(8).play()
            if event.key == pygame.K_n:
                shuffledAsso.get(9).play()
            if event.key == pygame.K_j:
                shuffledAsso.get(10).play()
            if event.key == pygame.K_m:
                shuffledAsso.get(11).play()
            if event.key == pygame.K_COMMA:
                shuffledAsso.get(12).play()
    pygame.display.flip()
pygame.quit()