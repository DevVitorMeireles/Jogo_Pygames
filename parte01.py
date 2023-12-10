import random
import pygame
pygame.init()
from random import randint

#posição do carro principal e velocidade
x=250
y=0
velocidade = 10

#posições dos outros carros
pos_carros_prata= [-50,250,550]
pos_y_prata = 250

pos_carros_azul = [-50,250,550]
pos_y_azul = 1000

pos_carros_preto = [-50,250,550]
pos_y_preto = 1200

pos_escolhida_carro_preto  =  random.choice(pos_carros_preto)
pos_escolhida_carros_prata = random.choice (pos_carros_prata)
pos_escolhida_carros_azul = random.choice (pos_carros_azul)

velocidade_outros = randint(5,15)

pontuacao = 0
ultrapassagem = 0

#imagens do jogo e plano de fundo
fundo = pygame.image.load('estrada.png')
carro = pygame.image.load('carro_amarelov2.png')
carro_prata = pygame.image.load('carro_prata.png')
carro_preto = pygame.image.load('carro_preto.png')
carro_azul = pygame.image.load('carro_azul.png')

#placar de tempo
font_tempo = pygame.font.SysFont('arial black',20)
texto = font_tempo.render("Tempo: ",True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center=(65,50)

font_pontuacao = pygame.font.SysFont('arial black',20)
texto_pontuacao = font_pontuacao.render("Pontuação:"+str(pontuacao), True, (255,255,255))
pos_texto_pontuacao = texto_pontuacao.get_rect()
pos_texto_pontuacao.center = (65,30)

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

# condicional de pontuação
    if y>pos_y_azul:
        pontuacao += 100
        ultrapassagem += 1
    

# condicional de aleatoriedade de spawn dos carros
    if (pos_y_prata <= -720) and (pos_y_preto <= -720) and (pos_y_azul <= -720):

        pos_y_azul = randint (900,2000)
        pos_y_prata = randint (800,1480)
        pos_y_preto = randint (1000,3000)

        pos_carros_prata= [-50,250,550]        
        pos_carros_preto= [-50,550,250] 
        pos_carros_azul= [550,250,-50] 

        pos_escolhida_carro_preto  =  random.choice (pos_carros_preto)
        pos_escolhida_carros_prata = random.choice (pos_carros_prata)
        pos_escolhida_carros_azul = random.choice (pos_carros_azul)  

         

    #velocidade após mudar de posição
    pos_y_preto -= velocidade_outros
    pos_y_azul -= velocidade_outros 
    pos_y_prata -= velocidade_outros 

    


       

    if (timer <80):
        timer += 1
    else:
        tempo_segundo+=1
        texto = font_tempo.render("Tempo: "+str(tempo_segundo),True, (255,255,255), (0,0,0))
        timer = 0

    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(carro_prata, (pos_escolhida_carros_prata,pos_y_prata))
    janela.blit(carro_azul,(pos_escolhida_carros_azul,pos_y_azul))
    janela.blit(carro_preto, (pos_escolhida_carro_preto,pos_y_preto))
    janela.blit(texto,pos_texto)
    janela.blit(texto_pontuacao,pos_texto_pontuacao)
    
    pygame.display.update()

pygame.quit()          



carro_azul_claro = pygame.image.load ('carro_da_estrada_azul_claro.png')
carro_amarelo = pygame.image.load ('carro_da_estrada_amarelo.png')
carro_azul_escuro = pygame.image.load ('carro_da_estrada-azul_escuro.png')
carro_verde = pygame.image.load ('carro_da estrada_verde.png')
carro_vermelho = pygame.image.load ('carro_da estrada_vermelho.png')