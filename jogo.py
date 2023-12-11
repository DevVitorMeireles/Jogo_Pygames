import pygame
import random
from random import randint
pygame.init()


largura = 800
altura  = 600
janela  = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo do Vitor Meireles')

x = 380
y = 300
velocidade = 10

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