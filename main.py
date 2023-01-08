import pygame
from pygame import mixer
pygame.init()

ANCHO = 800
ALTO = 400
anchoContainer = 740
altoContainer = 250
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
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

def drawKeys():
    #caja negra contenedora
    pygame.draw.rect(screen, black, [30, 35, anchoContainer, altoContainer], 0, 10)
    #teclas blancas
    for i in range(8):
        pygame.draw.rect(screen, blue, [i*(anchoContainer//8 - 6) + 60, 140, (anchoContainer//8 - 20), (anchoContainer//8 - 20)], 0, 3)
    #borrador
    # for i in range(8):
    #     pygame.draw.rect(screen, yellow, [i*(anchoContainer//8 - 6) + 60, 50, (anchoContainer//8 - 20), (anchoContainer//8 - 20)])
    #2 teclas negras
    for i in range(2):
        pygame.draw.rect(screen, blue, [i*(anchoContainer//8 - 6) + 110, 55, (anchoContainer//8 - 20), (anchoContainer//8 - 20)], 0, 3)
    #3 teclas negras
    for i in range(3):
        pygame.draw.rect(screen, blue, [i*(anchoContainer//8 - 6) + 365, 55, (anchoContainer//8 - 20), (anchoContainer//8 - 20)], 0, 3)
    #barra espaciadora referencia tonica
    pygame.draw.rect(screen, blue, [ANCHO//2 - 200, 225, 395, 40], 0, 3)
def drawInput():
    pygame.draw.rect(screen, blue, [0,0,0,0])
while run:
    timer.tick(fps)
    screen.fill(cafe)
    drawKeys()
    drawInput()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()