import pygame
pygame.init()
largura = 800
altura = 600
janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo do Vitor Meireles')

x = 380
y = 300
velocidade = 10

y_fundo=1800

fundo = pygame.image.load ('estrada.png')
carro_amarelo = pygame.image.load ('carro_da_estrada_amarelo.png')



janela_aberta = True
while janela_aberta:
    janela.fill((0,0,0))
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

        comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x <= 660:
        x += velocidade
    if comandos[pygame.K_LEFT] and x>=60:
        x -= velocidade

   
    

    if y_fundo >= altura:
        y_fundo = 0
    y_fundo = y_fundo +2
   
    janela.blit (fundo,(0,1500))
    
    janela.blit (carro_amarelo,(x,y))
    
    pygame.display.update()

pygame.quit()          