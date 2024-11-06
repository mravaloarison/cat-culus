import Setup as sp
from UIElements import RoundedTextBox
from Thunder import ThunderManager
import time

animation_start_time = None  
thunder_created = False

class Quiz:
    def __init__(self, quiz):
        self.instructions = quiz["instructions"]
        self.combinations = quiz["combinations"]

    def is_correct(self, x, y):
        for item in self.combinations:
            if x == item[0] and y == item[1]:
                return True
            
        return False
    
def prepare_quiz(init_quiz):
    generated_quiz = Quiz(init_quiz)
    quiz = RoundedTextBox(
        generated_quiz.instructions, 
        sp.MD_TEXT, sp.GAME_WIDTH, sp.GAME_HEIGHT, (400, 100)
    )

    return quiz, generated_quiz

def play_quiz(
        init_quiz, 
        screen, 
        count_left_hand, 
        count_right_hand, 
        quiz_index,
        current_time,
    ):
    global animation_start_time, thunder_created

    if quiz_index >= len(init_quiz):
        quiz = RoundedTextBox(
            "Game Completed!", 
            sp.MD_TEXT, sp.GAME_WIDTH, sp.GAME_HEIGHT, (400, 100)
        )
        quiz.draw(screen)
        return quiz_index

    quiz, generated_quiz = prepare_quiz(init_quiz[quiz_index])
    quiz.draw(screen)

    if not thunder_created:
        thunder_created = True
        thunder_manager = ThunderManager(sp.thunder, sp.THUNDER_FINAL_POSITION)
        sp.thunder_managers.append(thunder_manager)

    for thunder_manager in sp.thunder_managers:
        thunder_frame, thunder_position = thunder_manager.update(current_time)
        
        if thunder_frame and thunder_position:
            screen.blit(thunder_frame, thunder_position)

    if generated_quiz.is_correct(count_left_hand, count_right_hand):
        if animation_start_time is None:
            animation_start_time = current_time

            thunder_manager.was_hit = True

        else:
            animation_start_time = None
            sp.isCatAttack = False
            quiz_index += 1
        
    return quiz_index