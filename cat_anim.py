import pygame
import Setup as sp
from Thunder import Thunder

pygame.init()

screen = pygame.display.set_mode((sp.GAME_WIDTH, sp.GAME_HEIGHT))

thunder = Thunder("assets/thunder.png", scale_factor=1)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    frame_index_thunder = (pygame.time.get_ticks() // 100) % thunder.num_frames_idle
    frame_index_thunder_hit = (pygame.time.get_ticks() // 100) % 3
    
    screen.blit(thunder.get_idle_frames()[int(frame_index_thunder)], (0, 0))
    screen.blit(thunder.get_hit_frames()[int(frame_index_thunder_hit)], (300, 300))

    pygame.display.update()

pygame.quit()