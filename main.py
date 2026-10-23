import pygame
from Vector import Vector2D 
from Vector import Inimigo 
# pygame setup

WIDTH, HEIGHT = 600, 600
BLUE = (20, 150, 250)
RED = (250, 20, 20)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = Vector2D(screen.get_width() / 2, screen.get_height() / 2)
enemy_pos = Vector2D(0, 0)
my_enemy = Inimigo(0, 0)

while running:
    # poll for events
    dt = clock.tick(60) / 1000  # limits FPS to 60

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, BLUE, (int(player_pos.x), int(player_pos.y)), 20)
    pygame.draw.circle(screen, RED, (int(my_enemy.posicao.x), int(my_enemy.posicao.y)), 20)

    my_enemy.perseguir(player_pos, dt)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    
    # flip() the display to put your work on screen
    pygame.display.flip()

  

pygame.quit()