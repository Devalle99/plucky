import random
import pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Plucky')
ANCHO = 800
ALTO = 420
anchoContainer = 740
altoContainer = 250
fps = 60
timer = pygame.time.Clock()
darkBlue = (83, 127, 231)
celeste = (192, 238, 242)
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
colorPassive = (0, 159, 221)
colorActive = 'black'
colorInput = colorPassive
passive = False

font1 = pygame.font.Font('Roboto-Bold.ttf', 60)
font2 = pygame.font.Font('Roboto-Bold.ttf', 25)
font3 = pygame.font.Font('Roboto-Bold.ttf', 22)
inputStr = ''
strCorrecto = ''

def pickScale():
    lidio = 'zxcgbnm,'
    jonico = 'zxcvbnm,'
    mixolidio = 'zxcvbnj,'
    dorico = 'zxdvbnj,'
    eolico = 'zxdvbhj,'
    frigio = 'zsdvbhj,'
    locrio = 'zsdvghj,'
    pentMin = 'zdvbj,'
    pentMaj = 'zxcbn,'
    melMin = 'zxdvbnm,'
    blues = 'zdvgbj,'
    armMin = 'zxdvbhm,'
    lidFlat7 = 'zxcgbnj,'
    mixoFlat13 = 'zxcvbhj,'
    scales = [['Lidio', lidio], ['Jónico', jonico], ['Mixolidio', mixolidio],
    ['Dórico', dorico], ['Eólico', eolico], ['Frigio', frigio], ['Locrio', locrio],
    ['Pent. menor', pentMin], ['Pent. mayor', pentMaj], ['Melodica men.', melMin],
    ['Blues', blues], ['Armónica men.', armMin],
    ['Lidio b7', lidFlat7], ['Mixo. b13', mixoFlat13]]
    randScales = random.choice(scales)
    return randScales
currentScale = pickScale()
clrCorrecto = 'white'

zColor = 'white'
sColor = 'black'
xColor = 'white'
dColor = 'black'
cColor = 'white'
vColor = 'white'
gColor = 'black'
bColor = 'white'
hColor = 'black'
nColor = 'white'
jColor = 'black'
mColor = 'white'
comaColor = 'white'

while run:
    timer.tick(fps)
    screen.fill(celeste)
    pygame.draw.rect(screen, darkBlue, [30, 35, anchoContainer, altoContainer], 0, 10)
    #teclas blancas
    pygame.draw.rect(screen, zColor, [0*86 + 60, 165, 72, 95], 0, 3)
    pygame.draw.rect(screen, xColor, [1*86 + 60, 165, 72, 95], 0, 3)
    pygame.draw.rect(screen, cColor, [2*86 + 60, 165, 72, 95], 0, 3)
    pygame.draw.rect(screen, vColor, [3*86 + 60, 165, 72, 95], 0, 3)
    pygame.draw.rect(screen, bColor, [4*86 + 60, 165, 72, 95], 0, 3)
    pygame.draw.rect(screen, nColor, [5*86 + 60, 165, 72, 95], 0, 3)
    pygame.draw.rect(screen, mColor, [6*86 + 60, 165, 72, 95], 0, 3)
    pygame.draw.rect(screen, comaColor, [7*86 + 60, 165, 72, 95], 0, 3)
    #primeras 2 teclas negras
    pygame.draw.rect(screen, sColor, [0*86 + 110, 55, 72, 95], 0, 3)
    pygame.draw.rect(screen, dColor, [1*86 + 110, 55, 72, 95], 0, 3)
    #ultimas 3 teclas negras
    pygame.draw.rect(screen, gColor, [0*86 + 365, 55, 72, 95], 0, 3)
    pygame.draw.rect(screen, hColor, [1*86 + 365, 55, 72, 95], 0, 3)
    pygame.draw.rect(screen, jColor, [2*86 + 365, 55, 72, 95], 0, 3)

    key = font1.render('Z', True, 'black')
    screen.blit(key, (77, 178))
    key = font1.render('X', True, 'black')
    screen.blit(key, (162, 178))
    key = font1.render('C', True, 'black')
    screen.blit(key, (247, 178))
    key = font1.render('V', True, 'black')
    screen.blit(key, (333, 178))
    key = font1.render('B', True, 'black')
    screen.blit(key, (420, 178))
    key = font1.render('N', True, 'black')
    screen.blit(key, (504, 178))
    key = font1.render('M', True, 'black')
    screen.blit(key, (585, 178))
    key = font1.render(',', True, 'black')
    screen.blit(key, (690, 170))
    key = font1.render('S', True, 'white')
    screen.blit(key, (127, 68))
    key = font1.render('D', True, 'white')
    screen.blit(key, (213, 68))
    key = font1.render('G', True, 'white')
    screen.blit(key, (380, 68))
    key = font1.render('H', True, 'white')
    screen.blit(key, (466, 68))
    key = font1.render('J', True, 'white')
    screen.blit(key, (555, 68))
    
    inputBox = pygame.draw.rect(screen, (255, 255, 232), [(ANCHO//2) - 150, 300, 300, 50], 0, 5)
    pygame.draw.rect(screen, colorInput, inputBox, 3, 5)
    lblInput = font2.render(inputStr, True, 'black')
    screen.blit(lblInput, (inputBox.x+10, inputBox.y+10))
    if len(inputStr) > 20:
        inputStr=''

    btnComprobar = pygame.draw.rect(screen, darkBlue, [(ANCHO//2) - 95, 360, 190, 40], 5, 7)
    lblComprobar = font2.render('Comprobar', True, 'black')
    screen.blit(lblComprobar, ((ANCHO//2) - 64, 363))

    lblCorrecto = font2.render(strCorrecto, True, clrCorrecto)
    screen.blit(lblCorrecto, (338, 308))
    
    btnSiguiente = pygame.draw.rect(screen, darkBlue, [50, 315, 180, 70], 5, 7)
    lblSiguiente = font2.render('Siguiente', True, 'black')
    screen.blit(lblSiguiente, (85, 320))
    lblEjer = font2.render('ejercicio', True, 'black')
    screen.blit(lblEjer, (89, 348))
     
    lblIngresa = font3.render('Ingresa la escala:', True, 'black')
    screen.blit(lblIngresa, (570, 304))
    boxCurrent = pygame.draw.rect(screen, darkBlue, [570, 340, 200, 40], 5, 7)
    lblCurrent = font2.render(str(currentScale[0]), True, 'black')
    screen.blit(lblCurrent, (585, 344))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputBox.collidepoint(event.pos):
                passive = not passive
            else:
                passive = False
            colorInput = colorActive if passive else colorPassive
            if btnComprobar.collidepoint(event.pos):
                if inputStr == currentScale[1]:
                    inputStr = ''
                    strCorrecto = '  Correcto'
                    clrCorrecto = (0,170,0)
                    soundWin.play()        
                else:
                    inputStr = ''
                    strCorrecto = 'Incorrecto'
                    clrCorrecto = (190,0,0)
                    soundLoss.play()
            if btnSiguiente.collidepoint(event.pos):
                strCorrecto = ''
                temp = currentScale
                currentScale = pickScale()
                while currentScale == temp:
                    currentScale = pickScale()
                inputStr=''
        if event.type == pygame.KEYDOWN:
            if passive == True:
                if event.key == pygame.K_RETURN:
                    if inputStr == currentScale[1]:
                        inputStr = ''
                        strCorrecto = '  Correcto'
                        clrCorrecto = (0,170,0)
                        soundWin.play()        
                    else:
                        inputStr = ''
                        strCorrecto = 'Incorrecto'
                        clrCorrecto = (190,0,0)
                        soundLoss.play()
                if event.key == pygame.K_BACKSPACE:
                    inputStr = inputStr[:-1]
                else:
                    if strCorrecto == '':
                        inputStr += event.unicode
            if event.key == pygame.K_z:
                zColor = 'green'
                soundList_copy[0].play()
            if event.key == pygame.K_s:
                sColor = 'green'
                soundList_copy[1].play()
            if event.key == pygame.K_x:
                xColor = 'green'
                soundList_copy[2].play()
            if event.key == pygame.K_d:
                dColor = 'green'
                soundList_copy[3].play()
            if event.key == pygame.K_c:
                cColor = 'green'
                soundList_copy[4].play()
            if event.key == pygame.K_v:
                vColor = 'green'
                soundList_copy[5].play()
            if event.key == pygame.K_g:
                gColor = 'green'
                soundList_copy[6].play()
            if event.key == pygame.K_b:
                bColor = 'green'
                soundList_copy[7].play()
            if event.key == pygame.K_h:
                hColor = 'green'
                soundList_copy[8].play()
            if event.key == pygame.K_n:
                nColor = 'green'
                soundList_copy[9].play()
            if event.key == pygame.K_j:
                jColor = 'green'
                soundList_copy[10].play()
            if event.key == pygame.K_m:
                mColor = 'green'
                soundList_copy[11].play()
            if event.key == pygame.K_COMMA:
                comaColor = 'green'
                soundList_copy[12].play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                zColor = 'white'
            if event.key == pygame.K_s:
                sColor = 'black'
            if event.key == pygame.K_x:
                xColor = 'white'
            if event.key == pygame.K_d:
                dColor = 'black'
            if event.key == pygame.K_c:
                cColor = 'white'
            if event.key == pygame.K_v:
                vColor = 'white'
            if event.key == pygame.K_g:
                gColor = 'black'
            if event.key == pygame.K_b:
                bColor = 'white'
            if event.key == pygame.K_h:
                hColor = 'black'
            if event.key == pygame.K_n:
                nColor = 'white'
            if event.key == pygame.K_j:
                jColor = 'black'
            if event.key == pygame.K_m:
                mColor = 'white'
            if event.key == pygame.K_COMMA:
                comaColor = 'white'
    pygame.display.flip()
pygame.quit()