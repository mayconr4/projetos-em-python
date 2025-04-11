import pygame
import random
import sys
import math

# Configuração inicial do pygame
pygame.init()  # Inicia o jogo 
screen = pygame.display.set_mode((800, 768))  # Cria o tamanho da tela do jogo
clock = pygame.time.Clock()  # Controla os FPS do jogo (instanciando o objeto Clock corretamente)
pygame.display.set_caption("snake-game")  # Define o título da janela
running = True 

# Propriedades do personagem (um quadrado/player)
player_color = (0, 128, 0)  # Amarelo
player_size = 30  # Tamanho do quadrado/player
player_x = 150  # Posição inicial do quadrado/player
player_y = 150  # Posição inicial do quadrado/player
player_speed = 10  # Velocidade de movimentação 

maca_color = (255, 0, 0) 
maca_size = 30  
maca_x = random.randint(0, 800)
maca_y = random.randint(0, 768)  

player1 = [player_color, player_size, player_x, player_y, player_speed]    

maca = [maca_color, maca_size, maca_x, maca_y]    

 
def checar_se_cobra_comeu_maca(x,y,size,macax,macay,macaSize):
    if x ==macaSize or  x + size == macax or y == macaSize or y + size == maca_y:
        print("player comeu maçã +1 ponto")  
         
        

        
     

 
def checar_se_slayer_saiu(x, y, size, screen_width, screen_height): 
    if x < 0 or x + size > screen_width or y < 0 or y + size > screen_height: 
        print("O player saiu da tela. Encerrando o jogo...") 
        pygame.quit() 
        sys.exit()
        
 

# Loop principal do jogo
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False          

    keys = pygame.key.get_pressed()  # Retorna uma lista das teclas pressionadas
    
    # Movimentação do personagem com as setas do teclado
    if keys[pygame.K_LEFT]:
        player_x -= player_speed  # Mover para a esquerda
    if keys[pygame.K_RIGHT]:
        player_x += player_speed  # Mover para a direita
    if keys[pygame.K_UP]:
        player_y -= player_speed  # Mover para cima
    if keys[pygame.K_DOWN]:
        player_y += player_speed  # Mover para baixo                 
             
 
    checar_se_slayer_saiu(player_x,player_y,player_size,800, 768) 

    a = checar_se_cobra_comeu_maca(player_x,player_y,player_size,maca_x,maca_y,maca_size)
    if a == True: 
       pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size)) 
             
        
    # Preenche o fundo com a cor azul
    screen.fill((0, 0, 255))

    # Desenha o personagem
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen,maca_color,(maca_x, maca_y,player_size,player_size))                        

    # Atualiza a tela
    pygame.display.flip()        

    # Controla os FPS do jogo (60 FPS)
    clock.tick(60)
    
# Encerra o Pygame
pygame.quit()
 

 
