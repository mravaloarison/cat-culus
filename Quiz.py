import Setup as sp
from UIElements import RoundedTextBox

animation_start_time = None  

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
        frame_cat_attack,
        frame_index_thunder_hit,
        current_time
    ):
    global animation_start_time

    if quiz_index >= len(init_quiz):
        quiz = RoundedTextBox(
            "Game Completed!", 
            sp.MD_TEXT, sp.GAME_WIDTH, sp.GAME_HEIGHT, (400, 100)
        )
        quiz.draw(screen)
        return quiz_index

    quiz, generated_quiz = prepare_quiz(init_quiz[quiz_index])
    quiz.draw(screen)

    if generated_quiz.is_correct(count_left_hand, count_right_hand):
        if animation_start_time is None:
            animation_start_time = current_time

        if current_time - animation_start_time < 600:
            sp.screen.blit(sp.cat.get_attack_frames()[int(frame_cat_attack)], sp.CAT_POSITION)
            sp.screen.blit(sp.thunder.get_hit_frames()[int(frame_index_thunder_hit)], sp.THUNDER_FINAL_POSITION)
        else:
            animation_start_time = None
            quiz_index += 1

    return quiz_index