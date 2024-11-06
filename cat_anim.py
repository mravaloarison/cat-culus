import pygame
import Setup as sp
from Thunder import Thunder, ThunderManager

pygame.init()

screen = pygame.display.set_mode((sp.GAME_WIDTH, sp.GAME_HEIGHT))

thunder_sprite = Thunder("assets/thunder.png", scale_factor=1)

thunder_managers = []

target_position = sp.THUNDER_FINAL_POSITION

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                thunder_manager = ThunderManager(thunder_sprite, target_position)
                thunder_managers.append(thunder_manager)

    for thunder_manager in thunder_managers:
        thunder_frame, thunder_position = thunder_manager.update(current_time)
        
        if thunder_frame and thunder_position:
            screen.blit(thunder_frame, thunder_position)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
