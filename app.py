import pygame
from utils.hand_tracker import get_hands, display_hands
import Setup as sp
from UIElements import RoundedTextBox

from Test import ai_response

pygame.init()
pygame.display.set_caption("Cat-Culus")

screen = pygame.display.set_mode([sp.GAME_WIDTH, sp.GAME_HEIGHT], pygame.RESIZABLE)

text_box = RoundedTextBox("Hello, Centered!", sp.MD_TEXT, sp.GAME_WIDTH, sp.GAME_HEIGHT, (400, 100))

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    count_left_hand, count_right_hand = get_hands(sp.hand_tracker, screen, pygame)
    display_hands(screen, count_left_hand, count_right_hand, sp)

    text_box.draw(screen)

    pygame.display.update()

pygame.quit()