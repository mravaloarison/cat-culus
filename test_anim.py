import pygame
import Setup as sp

pygame.init()

screen = pygame.display.set_mode((sp.GAME_WIDTH, sp.GAME_HEIGHT))

clock = pygame.time.Clock()
running = True

hearts_total = 5
hearts_used = 2
while running:
    screen.fill((0, 0, 0))
    sp.screen.blit(sp.bg_image, (0, 0))

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    heart_width = sp.full_heart.get_width()
    heart_spacing = 20
    total_heart_width = heart_width * hearts_total + heart_spacing * (hearts_total - 1)
    start_x = sp.GAME_WIDTH // 2 - total_heart_width // 2

    for i in range(hearts_total):
        x = start_x + i * (heart_width + heart_spacing)
        if i >= hearts_total - hearts_used:
            sp.screen.blit(sp.empty_heart, (x, 30))
        else:
            sp.screen.blit(sp.full_heart, (x, 30))

    sp.display_msg("Hello World")

    pygame.display.update()
    clock.tick(60)

pygame.quit()