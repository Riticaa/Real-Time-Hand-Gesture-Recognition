import cv2
from hand_tracker import HandTracker

cap = cv2.VideoCapture(0)

tracker = HandTracker()

while True:
    success, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame, landmarks = tracker.detect_hands(frame)

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()