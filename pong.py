from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

janela = Window(1280, 640)
janela.set_title("Pong")

fundo = GameImage("terra.jpg")
bola = Sprite("bola.png", 1)
pad_direita = Sprite("pads.png", 1)
pad_esquerda = Sprite("pads.png", 1)

bola.x = (janela.width/2)-(bola.width/2)
bola.y = (janela.height/2)-(bola.height/2)
pad_esquerda.x = 10
pad_esquerda.y = janela.height/2 - pad_esquerda.height/2
pad_direita.x = janela.width - pad_direita.width - 10
pad_direita.y = janela.height/2 - pad_direita.height/2
contador_batida_direita = 0
contador_batida_esquerda = 0

velocidade_pad = 200
velocidade_bolaX = 400
velocidade_bolaY = 300
pontuacao_esquerda = 0
pontuacao_direita = 0
padY = 0

teclado = Window.get_keyboard()
clock = pygame.time.Clock()

while True:
    #Entrada de dados
    if (teclado.key_pressed("UP")) and (pad_esquerda.y >= 0):
        pad_esquerda.y = pad_esquerda.y - velocidade_pad * janela.delta_time()
    elif (teclado.key_pressed("DOWN")) and (pad_esquerda.y + pad_esquerda.height <= janela.height):
        pad_esquerda.y = pad_esquerda.y + velocidade_pad * janela.delta_time()

    if velocidade_bolaX > 0:

        if velocidade_bolaY > 0:
            if pad_direita.y < janela.height - pad_direita.height:
                pad_direita.y = pad_direita.y + velocidade_pad * janela.delta_time()
            elif pad_direita.y > janela.height - pad_direita.height:
                pad_direita.y = janela.height - pad_direita.height
        elif velocidade_bolaY < 0:
            if pad_direita.y > 0:
                pad_direita.y = pad_direita.y - velocidade_pad * janela.delta_time()
            elif pad_direita.y < 0:
                pad_direita.y = 0

    #Update
    bola.x = bola.x + velocidade_bolaX * janela.delta_time()
    bola.y = bola.y + velocidade_bolaY * janela.delta_time()
    if bola.collided(pad_direita):
        velocidade_bolaX = velocidade_bolaX*(-1)
        contador_batida_direita = contador_batida_direita + 1
        if (bola.x + bola.width > pad_direita.x):
            bola.x = pad_direita.x - bola.width - 1
    elif bola.collided(pad_esquerda):
        velocidade_bolaX = velocidade_bolaX*(-1)
        contador_batida_esquerda = contador_batida_esquerda + 1.
        if (bola.x < pad_esquerda.x + pad_esquerda.width):
            bola.x = pad_esquerda.x + pad_esquerda.width + 1

    if (bola.y + bola.height >= janela.height) or (bola.y < 0):
        velocidade_bolaY = velocidade_bolaY*(-1)
        if (bola.y + bola.height > janela.height):
            bola.y = janela.height - bola.height - 1
        elif bola.y < 0:
            bola.y = 1

    if (contador_batida_direita >= 2) and (contador_batida_esquerda >= 2):
        padY = pad_esquerda.y
        contador_batida_direita = 0
        contador_batida_esquerda = 0
        pad_esquerda = Sprite("pad_menor.png", 1)
        pad_esquerda.y = padY
        pad_esquerda.x = 10
    
    if bola.x + bola.width >= janela.width:
        velocidade_bolaX = velocidade_bolaX*(-1)
        velocidade_bolaY = velocidade_bolaY*(-1)
        pontuacao_esquerda = int(pontuacao_esquerda)
        pontuacao_esquerda = pontuacao_esquerda + 1
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2
    elif bola.x < 0:
        velocidade_bolaX = velocidade_bolaX*(-1)
        velocidade_bolaY = velocidade_bolaY*(-1)
        pontuacao_direita = int(pontuacao_direita)
        pontuacao_direita = pontuacao_direita + 1
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2

    clock.tick(60)

    #Desenho
    fundo.draw()
    pontuacao_esquerda = str(pontuacao_esquerda)
    pontuacao_direita = str(pontuacao_direita)
    janela.draw_text(pontuacao_esquerda, janela.width*1/3, 40, 40, (250, 0, 0), "Arial", False, False)
    janela.draw_text(pontuacao_direita, janela.width*2/3, 40, 40, (250, 0, 0), "Arial", False, False)
    janela.draw_text(str(round(clock.get_fps())), janela.width-20, 20, 20, (0, 250, 0), "Arial", True, False)
    bola.draw()
    pad_direita.draw()
    pad_esquerda.draw()
    janela.update()