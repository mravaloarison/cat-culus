import pygame, cv2
from Hand import HandTracker

pygame.font.init()

capture = cv2.VideoCapture(0)
hand_tracker = HandTracker(capture)

font_path = "./font/Itim-Regular.ttf"

SM_TEXT = pygame.font.Font(font_path, 24)
MD_TEXT = pygame.font.Font(font_path, 36)

GAME_WIDTH, GAME_HEIGHT = 1366, 1010