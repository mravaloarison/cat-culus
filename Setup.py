import pygame, cv2
from Hand import HandTracker
from Thunder import Thunder


pygame.font.init()

capture = cv2.VideoCapture(0)
hand_tracker = HandTracker(capture)

font_path = "./font/Itim-Regular.ttf"

SM_TEXT = pygame.font.Font(font_path, 24)
MD_TEXT = pygame.font.Font(font_path, 36)

GAME_WIDTH, GAME_HEIGHT = 1366, 1010

thunder = Thunder("assets/thunder.png", scale_factor=1)

bg_image = pygame.image.load('./assets/bg.png')
bg_image = pygame.transform.scale(bg_image, (GAME_WIDTH, GAME_HEIGHT)) 

screen = pygame.display.set_mode([GAME_WIDTH, GAME_HEIGHT], pygame.RESIZABLE)
