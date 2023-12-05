import pygame
pygame.init()
from random import randint

#posição do carro principal e velocidade
x=250
y=0
velocidade = 10

#posições dos outros carros
pos_x_prata = -50
pos_y_prata = 250

pos_x_azul = 550
pos_y_azul = 1000

pos_x_preto = 250
pos_y_preto = 1200

velocidade_outros = randint(5,15)

#imagens do jogo e plano de fundo
fundo = pygame.image.load('Estrada.png')
carro = pygame.image.load('carro_amarelov2.png')
carro_prata = pygame.image.load('carro_prata.png')
carro_preto = pygame.image.load('carro_preto.png')
carro_azul = pygame.image.load('carro_azul.png')

#placar de tempo
font = pygame.font.SysFont('arial black',20)
texto = font.render("Tempo: ",True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center=(65,50)

#tempo
timer=0
tempo_segundo = 0

#tamanho e nome da janela 
janela = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Jogo do Vitor Meireles')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
# comandos de direita e esquerda do carro
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and x <= 550:
        x += velocidade
    if comandos[pygame.K_LEFT] and x>=-50:
        x -= velocidade
# condicional de aleatoriedade de spawn dos carros
    if (pos_y_prata <= -720) and (pos_y_preto <= -720) and (pos_y_azul <= -720):

        pos_y_azul = randint (900,2000)
        pos_y_prata = randint (720,1480)
        pos_y_preto = randint (720,4000)

    #velocidade após mudar de posição
    pos_y_preto -= velocidade_outros
    pos_y_azul -= velocidade_outros 
    pos_y_prata -= velocidade_outros 

    if (timer <80):
        timer += 1
    else:
        tempo_segundo+=1
        texto = font.render("Tempo: "+str(tempo_segundo),True, (255,255,255), (0,0,0))
        timer = 0

    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(carro_prata, (pos_x_prata,pos_y_prata))
    janela.blit(carro_azul,(pos_x_azul,pos_y_azul))
    janela.blit(carro_preto, (pos_x_preto,pos_y_preto))
    janela.blit(texto,pos_texto)
    
    pygame.display.update()

pygame.quit()          