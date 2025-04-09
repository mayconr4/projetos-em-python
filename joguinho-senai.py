import pygame
import random

# Configuração inicial do pygame
pygame.init()  # Inicia o jogo 
screen = pygame.display.set_mode((1080, 768))  # Cria o tamanho da tela do jogo
clock = pygame.time.Clock()  # Controla os FPS do jogo (instanciando o objeto Clock corretamente)
pygame.display.set_caption("snake-game")  # Define o título da janela
running = True 

# Propriedades do personagem (um quadrado/player)
player_color = (255, 255, 0)  # Amarelo
player_size = 50  # Tamanho do quadrado/player
player_x = 100  # Posição inicial do quadrado/player
player_y = 100  # Posição inicial do quadrado/player
player_speed = 5  # Velocidade de movimentação 

player2_color = (255, 0, 0) 
player2_size = 50  
player2_x = 100
player2_y = 100 
player2_position = random.randint(1,1080)

player1 = [player_color, player_size, player_x, player_y, player_speed]    

player2 = [player2_color, player2_size, player2_x, player2_y,player2_position]

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

    if player1 in range(player2): 
       contador = 0
       while True: 
           player1[1] = +20  
           break
       contador +=0

    
     



    

    # Preenche o fundo com a cor azul
    screen.fill((0, 0, 255))

    # Desenha o personagem
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen,player2_color,(player2_x, player2_y,player_size,player_size))


    # Atualiza a tela
    pygame.display.flip() 



    # Controla os FPS do jogo (60 FPS)
    clock.tick(60)

# Encerra o Pygame
pygame.quit()

