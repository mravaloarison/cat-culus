import pygame, cv2
from Hand import HandTracker
from Thunder import Thunder
from Cat import Cat

from utils.quiz_generator import generate_quiz

pygame.font.init()

capture = cv2.VideoCapture(0)
hand_tracker = HandTracker(capture)

init_quiz = generate_quiz()
question_index = 0

SCORE = 0

font_path = "./font/Itim-Regular.ttf"

SM_TEXT = pygame.font.Font(font_path, 24)
MD_TEXT = pygame.font.Font(font_path, 36)
LG_TEXT = pygame.font.Font(font_path, 48)
XL_TEXT = pygame.font.Font(font_path, 60)

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

full_heart = pygame.image.load("assets/full_heart.png")
empty_heart = pygame.image.load("assets/empty_heart.png")

hearts_total = 5
hearts_used = 0

is_game_over = False
is_game_complete = False

game_over_bg = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
game_over_bg.set_alpha(128)

try_again = pygame.image.load("assets/try_again.png")
try_again_hovered = pygame.image.load("assets/try_again_hovered.png")

def display_msg(msg):
    global SCORE
    game_over_bg.fill((0, 0, 0))
    game_over_text_surface = LG_TEXT.render(msg, True, (255, 255, 255))
    score_text_surface = XL_TEXT.render(f"{SCORE}", True, (255, 255, 255))
    text_x, text_y = game_over_text_surface.get_size()
    score_x, score_y = score_text_surface.get_size()
    screen.blit(game_over_bg, (0, 0))
    screen.blit(game_over_text_surface, ((GAME_WIDTH - text_x) // 2, (GAME_HEIGHT - text_y) // 2 - 60))
    screen.blit(score_text_surface, ((GAME_WIDTH - score_x) // 2, (GAME_HEIGHT - score_y) // 2 - 150))

    try_again_btn = pygame.Rect(GAME_WIDTH // 2 - try_again.get_width() // 2, GAME_HEIGHT // 2, try_again.get_width(), try_again.get_height())
    pygame.Rect(GAME_WIDTH // 2 - try_again.get_width() // 2, GAME_HEIGHT // 2, try_again.get_width(), try_again.get_height())

    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if try_again_btn.collidepoint(mouse_x, mouse_y):
        screen.blit(try_again_hovered, (GAME_WIDTH // 2 - try_again.get_width() // 2, GAME_HEIGHT // 2))
    else:
        screen.blit(try_again, (GAME_WIDTH // 2 - try_again.get_width() // 2, GAME_HEIGHT // 2))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if try_again_btn.collidepoint(mouse_x, mouse_y):
                global is_game_over
                global is_game_complete
                global hearts_used
                global question_index
                global init_quiz
                global question_index

                is_game_over = False
                is_game_complete = False
                hearts_used = 0
                question_index = 0
                init_quiz = generate_quiz()
                question_index = 0
                SCORE = 0

                return