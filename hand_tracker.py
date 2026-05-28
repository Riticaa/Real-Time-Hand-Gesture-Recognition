import cv2
import mediapipe as mp


class HandTracker:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mp_draw = mp.solutions.drawing_utils

        self.tip_ids = [4, 8, 12, 16, 20]

    def detect_hands(self, frame):

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb_frame)

        landmarks = []

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                h, w, _ = frame.shape

                for id, lm in enumerate(hand_landmarks.landmark):

                    cx = int(lm.x * w)
                    cy = int(lm.y * h)

                    landmarks.append((id, cx, cy))

        return frame, landmarks

    def fingers_up(self, landmarks):

        fingers = []

        if len(landmarks) != 0:

            if landmarks[self.tip_ids[0]][1] > landmarks[self.tip_ids[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):

                if landmarks[self.tip_ids[id]][2] < landmarks[self.tip_ids[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        return fingers