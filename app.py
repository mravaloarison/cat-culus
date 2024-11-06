import pygame
from utils.hand_tracker import get_hands, display_hands
import Setup as sp
from Quiz import play_quiz

from Test import ai_response

pygame.init()
pygame.display.set_caption("Cat-Culus")

init_quiz = ai_response
question_index = 0

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

    frame_cat = (pygame.time.get_ticks() // 100) % sp.cat.num_frames_idle
    frame_cat_hit = (pygame.time.get_ticks() // 100) % 3
    frame_cat_attack = (pygame.time.get_ticks() // 100) % 6
    frame_index_thunder = (pygame.time.get_ticks() // 100) % sp.thunder.num_frames_idle
    frame_index_thunder_hit = (pygame.time.get_ticks() // 100) % 5

    question_index = play_quiz(
        init_quiz, 
        sp.screen, 
        count_left_hand, count_right_hand, 
        question_index,
        current_time
    )

    sp.screen.blit(sp.broom, sp.BROOM_POSITION)

    if sp.isCatHit:
        sp.screen.blit(sp.cat.get_hit_frames()[int(frame_cat_hit)], sp.CAT_POSITION)
    elif sp.isCatAttack:
        sp.screen.blit(sp.cat.get_attack_frames()[int(frame_cat_attack)], sp.CAT_POSITION)
    else:
        sp.screen.blit(sp.cat.get_idle_frames()[int(frame_cat)], sp.CAT_POSITION)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
