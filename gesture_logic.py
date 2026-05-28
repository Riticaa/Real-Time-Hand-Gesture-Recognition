def is_finger_open(tip, pip):
    return tip[1] < pip[1]

def detect_gesture(landmarks):
    fingers = []

    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]

    for tip, pip in zip(tips, pips):
        fingers.append(is_finger_open(landmarks[tip], landmarks[pip]))

    thumb = landmarks[4][0] > landmarks[3][0]

    if all(fingers) and thumb:
        return "OPEN PALM ✋"
    elif not any(fingers):
        return "FIST ✊"
    elif thumb and not any(fingers):
        return "THUMBS UP 👍"
    elif fingers[0] and fingers[1]:
        return "PEACE ✌️"
    else:
        return "UNKNOWN"
    
class GestureRecognizer:

    def recognize_gesture(self, fingers):

        if fingers == [0, 1, 0, 0, 0]:
            return "One Finger"

        elif fingers == [0, 1, 1, 0, 0]:
            return "Peace Sign"

        elif fingers == [1, 1, 1, 1, 1]:
            return "Open Palm"

        elif fingers == [0, 0, 0, 0, 0]:
            return "Fist"

        else:
            return "Unknown"
    