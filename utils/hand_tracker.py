import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def run_hand_tracker(cam_id = 0):
    capture = cv2.VideoCapture(cam_id)

    WIDTH, HEIGHT = 1024, 768

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5
    ) as hands:
        while capture.isOpened():
            ret, frame = capture.read()
            if not ret:
                print("Ignoring empty camera frame.")
                continue
            
            frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
            
            frame.shape
            frame = cv2.resize(frame, (WIDTH, HEIGHT))

            frame.flags.writeable = False
            results = hands.process(frame)
            frame.flags.writeable = True

            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.imshow('MediaPipe Hands', frame)
            if cv2.waitKey(5) & 0xFF == 27:
                break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_hand_tracker()