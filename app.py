import pygame
from utils.hand_tracker import get_hands, display_hands
import Setup as sp
from Quiz import play_quiz

pygame.init()
pygame.display.set_caption("Cat-Culus")

clock = pygame.time.Clock()

running = True
while running:
    sp.screen.fill((0, 0, 0))
    sp.screen.blit(sp.bg_image, (0, 0))

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    count_left_hand, count_right_hand = get_hands(sp.hand_tracker, sp.screen, pygame)
    display_hands(sp.screen, count_left_hand, count_right_hand, sp)

    score_text = sp.LG_TEXT.render(f"Score: {sp.SCORE}", True, (0, 255, 0))
    sp.screen.blit(score_text, (sp.GAME_WIDTH - score_text.get_width() - 30, 120))

    frame_cat = (pygame.time.get_ticks() // 100) % sp.cat.num_frames_idle
    frame_cat_hit = (pygame.time.get_ticks() // 100) % 3
    frame_cat_attack = (pygame.time.get_ticks() // 100) % 6
    frame_index_thunder = (pygame.time.get_ticks() // 100) % sp.thunder.num_frames_idle
    frame_index_thunder_hit = (pygame.time.get_ticks() // 100) % 5

    sp.question_index = play_quiz(
        sp.init_quiz, 
        sp.screen, 
        count_left_hand, count_right_hand, 
        sp.question_index,
        current_time
    )

    sp.screen.blit(sp.broom, sp.BROOM_POSITION)

    if sp.isCatHit:
        sp.screen.blit(sp.cat.get_hit_frames()[int(frame_cat_hit)], sp.CAT_POSITION)
    elif sp.isCatAttack:
        sp.screen.blit(sp.cat.get_attack_frames()[int(frame_cat_attack)], sp.CAT_POSITION)
    else:
        sp.screen.blit(sp.cat.get_idle_frames()[int(frame_cat)], sp.CAT_POSITION)

    heart_width = sp.full_heart.get_width()
    heart_spacing = 20
    total_heart_width = heart_width * sp.hearts_total + heart_spacing * (sp.hearts_total - 1)
    start_x = sp.GAME_WIDTH // 2 - total_heart_width // 2

    for i in range(sp.hearts_total):
        x = start_x + i * (heart_width + heart_spacing)
        if i >= sp.hearts_total - sp.hearts_used:
            sp.screen.blit(sp.empty_heart, (x, 30))
        else:
            sp.screen.blit(sp.full_heart, (x, 30))

    if sp.hearts_used == sp.hearts_total:
        sp.is_game_over = True

    if sp.is_game_over:
        sp.display_msg("Game Over!")

    elif sp.is_game_complete:
        sp.display_msg("Game Completed!")

    pygame.display.update()
    clock.tick(60)

pygame.quit()
