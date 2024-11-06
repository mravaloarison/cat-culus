import pygame, cv2
from Hand import HandTracker
from Thunder import Thunder
from Cat import Cat

pygame.font.init()

capture = cv2.VideoCapture(0)
hand_tracker = HandTracker(capture)

font_path = "./font/Itim-Regular.ttf"

SM_TEXT = pygame.font.Font(font_path, 24)
MD_TEXT = pygame.font.Font(font_path, 36)

GAME_WIDTH, GAME_HEIGHT = 1366, 1010

bg_image = pygame.image.load('./assets/bg1.png')
bg_image = pygame.transform.scale(bg_image, (GAME_WIDTH, GAME_HEIGHT)) 

screen = pygame.display.set_mode([GAME_WIDTH, GAME_HEIGHT], pygame.RESIZABLE)

thunder = Thunder("assets/thunder.png", scale_factor=1)
cat = Cat("assets/cat.png", scale_factor=1)

thunder_managers = []

broom = pygame.image.load("assets/broom.png")

CAT_POSITION = (GAME_WIDTH // 2 - 90, GAME_HEIGHT // 1.4 - 200)
BROOM_POSITION = (GAME_WIDTH // 2 - 90, GAME_HEIGHT // 1.4 - 34)
THUNDER_FINAL_POSITION = (GAME_WIDTH // 2 - 90, GAME_HEIGHT // 1.4 - 336)

isCatHit = False
isCatAttack = False
