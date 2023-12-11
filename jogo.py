import pygame
import random
from random import randint
pygame.init()


largura = 800
altura  = 600
janela  = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo do Vitor Meireles')

fundo             = pygame.image.load ("estrada_antiga.png") 
y_fundo           = 0

carro_amarelo     = pygame.image.load ('carro_amarelo.png')
x_principal       = 380
y_principal       = 300
velocidade        = 10

carro_vermelho    = pygame.image.load ('carro_vermelho.png')
x_vermelho        = 620
y_vermelho        = 300

carro_azul_claro  = pygame.image.load ('carro_azul_claro.png')
x_azul_claro      = 260
y_azul_claro      = 300

carro_azul_escuro = pygame.image.load ('carro_azul_escuro.png')
x_azul_escuro     = 465
y_azul_escuro     = 300

carro_verde       = pygame.image.load ('carro_verde.png')
x_verde           = 60
y_verde           = 300


velocidade_outros = 2

 



janela_aberta = True
while janela_aberta:
    
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x_principal <= 605:
        x_principal += velocidade
    if comandos[pygame.K_LEFT]  and x_principal >= 60:
        x_principal -= velocidade
    def movimento_outros_carros (y_carro):
        if y_carro > altura:
            y_carro = randint(-600,0)
        y_carro += velocidade_outros
        return y_carro
    y_vermelho  = movimento_outros_carros (y_vermelho)
    if y_fundo >= altura:
        y_fundo = 0
    y_fundo = y_fundo + 2.5

    janela.blit (fundo, (0,y_fundo))
    janela.blit (fundo, (0,y_fundo - altura ))
    janela.blit (carro_amarelo, (x_principal,y_principal))
    janela.blit (carro_vermelho, (x_vermelho,y_vermelho))
    pygame.display.update()

pygame.quit()          