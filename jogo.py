import pygame
import random
from random import randint
pygame.init()


largura = 800
altura  = 600
janela  = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo do Vitor Meireles')

fundo                          = pygame.image.load ("estrada_antiga.png") 
y_fundo                        = 0

carro_amarelo                  = pygame.image.load ('carro_amarelo.png')
x_principal                    = 380
y_principal                    = 400
velocidade                     = 15

carro_vermelho                 = pygame.image.load ('carro_vermelho.png')
x_vermelho                     = 60
y_vermelho                     = 600

carro_azul_claro               = pygame.image.load ('carro_azul_claro.png')
x_azul_claro                   = 260
y_azul_claro                   = 600

carro_azul_escuro              = pygame.image.load ('carro_azul_escuro.png')
x_azul_escuro                  = 465
y_azul_escuro                  = 600

carro_verde                    = pygame.image.load ('carro_verde.png')
x_verde                        = 620
y_verde                        = 600


velocidade_outros = 4


 
janela_aberta = True
while janela_aberta:
    
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # comandos de esquerda e direita

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x_principal <= 605:
        x_principal += velocidade

    if comandos[pygame.K_LEFT]  and x_principal >= 60:
        x_principal -= velocidade

    # condicionais de aleatoriedade na queda do carro
    
    if (y_vermelho    > altura):
        y_vermelho    = randint (-500,-185)

    if (y_azul_escuro > altura):
        y_azul_escuro = randint (-1800,-1200)

    if (y_azul_claro  > altura ): 
        y_azul_claro  = randint (-1000,-700)

    if (y_verde       > altura):
        y_verde       = randint (-2700,-1800)
        
    y_vermelho    += velocidade_outros
    y_verde       += velocidade_outros
    y_azul_claro  += velocidade_outros
    y_azul_escuro += velocidade_outros

    # colisão do carro

    jogador_forma           = pygame.Rect(x_principal,   y_principal,   carro_amarelo.get_width(),     carro_amarelo.get_height())
    carro_vermelho_forma    = pygame.Rect(x_vermelho,    y_vermelho,    carro_vermelho.get_width(),    carro_vermelho.get_height())
    carro_azul_escuro_forma = pygame.Rect(x_azul_escuro, y_azul_escuro, carro_azul_escuro.get_width(), carro_azul_escuro.get_height())
    carro_azul_claro_forma  = pygame.Rect(x_azul_claro,  y_azul_claro,  carro_azul_claro.get_width(),  carro_azul_claro.get_height())
    carro_verde_forma       = pygame.Rect(x_verde,       y_verde,       carro_verde.get_width(),       carro_verde.get_height())

    if jogador_forma.colliderect(carro_vermelho_forma) or jogador_forma.colliderect(carro_azul_escuro_forma) or  jogador_forma.colliderect(carro_azul_claro_forma) or jogador_forma.colliderect(carro_verde_forma):
        y_principal = 1200
        
        
        
    
    # condicional de movimentação do fundo

    if y_fundo >= altura:
        y_fundo = 0
    y_fundo = y_fundo + 6

    janela.blit (fundo,             (0,                  y_fundo))
    janela.blit (fundo,             (0,                  y_fundo - altura ))
    janela.blit (carro_amarelo,     (x_principal,        y_principal))
    janela.blit (carro_vermelho,    (x_vermelho,         y_vermelho))
    janela.blit (carro_azul_escuro, (x_azul_escuro,      y_azul_escuro ))
    janela.blit (carro_azul_claro,  (x_azul_claro,       y_azul_claro ))
    janela.blit (carro_verde,       (x_verde,            y_verde))
    
    pygame.display.update()

pygame.quit()          