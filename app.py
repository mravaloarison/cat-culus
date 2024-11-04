import pygame, cv2
from Hand import HandTracker

GAME_WIDTH, GAME_HEIGHT = 1366, 1010

pygame.init()

screen = pygame.display.set_mode([GAME_WIDTH, GAME_HEIGHT], pygame.RESIZABLE)

capture = cv2.VideoCapture(0)
hand_tracker = HandTracker(capture)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame = hand_tracker.track_hands()
    count_left_hand, count_right_hand = hand_tracker.finger_count()

    if frame is not None:
        frame_surface = pygame.surfarray.make_surface(cv2.transpose(frame)) 
        screen.blit(frame_surface, (0, 0)) 

    pygame.display.update()

pygame.quit()
capture.release()