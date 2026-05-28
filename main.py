import cv2

from hand_tracker import HandTracker
from gesture_logic import GestureRecognizer
from gesture_controller import GestureController


cap = cv2.VideoCapture(0)

tracker = HandTracker()

recognizer = GestureRecognizer()

controller = GestureController()


while True:

    success, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame, landmarks = tracker.detect_hands(frame)

    h, w, _ = frame.shape

    if len(landmarks) != 0:

        fingers = tracker.fingers_up(landmarks)

        gesture = recognizer.recognize_gesture(fingers)

        cv2.putText(
            frame,
            gesture,
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3
        )

        index_x = landmarks[8][1]
        index_y = landmarks[8][2]

        if gesture == "One Finger":

            controller.move_mouse(index_x, index_y, w, h)

        elif gesture == "Peace Sign":

            controller.left_click()

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()