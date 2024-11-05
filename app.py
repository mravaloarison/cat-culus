import pygame
from utils.hand_tracker import get_hands, display_hands
import Setup as sp
from Quiz import play_quiz

from Test import ai_response

pygame.init()
pygame.display.set_caption("Cat-Culus")

screen = pygame.display.set_mode([sp.GAME_WIDTH, sp.GAME_HEIGHT], pygame.RESIZABLE)

init_quiz = ai_response
question_index = 0

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    count_left_hand, count_right_hand = get_hands(sp.hand_tracker, screen, pygame)
    display_hands(screen, count_left_hand, count_right_hand, sp)
    
    question_index = play_quiz(init_quiz, screen, count_left_hand, count_right_hand, question_index)

    pygame.display.update()

pygame.quit()