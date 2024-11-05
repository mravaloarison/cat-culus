import pygame
from utils.hand_tracker import get_hands, display_hands
import Setup as sp
from Quiz import play_quiz

from Test import ai_response

pygame.init()
pygame.display.set_caption("Cat-Culus")

init_quiz = ai_response
question_index = 0

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
    
    question_index = play_quiz(init_quiz, sp.screen, count_left_hand, count_right_hand, question_index)

    pygame.display.update()

pygame.quit()
