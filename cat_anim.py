import pygame
import Setup as sp
from Thunder import Thunder
from Sprite import Sprite
from Cat import Cat

pygame.init()

screen = pygame.display.set_mode((sp.GAME_WIDTH, sp.GAME_HEIGHT))

thunder = Thunder("assets/thunder.png", scale_factor=1)
test = Sprite("assets/cat.png", scale_factor=1, num_frames=19, sprite_width=2850, sprite_height=180)

cat = Cat("assets/cat.png", scale_factor=1)

test_count = 9

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

    frame_index_test = (pygame.time.get_ticks() // 100) % test.num_frames

    frame_index_cat = (pygame.time.get_ticks() // 100) % cat.num_frames_idle
    frame_index_cat_hit = (pygame.time.get_ticks() // 100) % 3
    frame_index_cat_attack = (pygame.time.get_ticks() // 100) % 6
    
    screen.blit(thunder.get_idle_frames()[int(frame_index_thunder)], (0, 0))
    screen.blit(thunder.get_hit_frames()[int(frame_index_thunder_hit)], (300, 300))

    screen.blit(test.get_frame()[int(frame_index_test)], (900, 0))

    screen.blit(cat.get_idle_frames()[int(frame_index_cat)], (0, 300))
    screen.blit(cat.get_hit_frames()[int(frame_index_cat_hit)], (300, 0))
    screen.blit(cat.get_attack_frames()[int(frame_index_cat_attack)], (600, 0))

    pygame.display.update()

pygame.quit()