# refered https://github.com/pdhruv93/computer-vision/tree/main/fingers-count
# https://google.github.io/mediapipe/solutions/hands.html

import cv2
import mediapipe as mp
from handdetector import HandDetector

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_hands = mp.solutions.hands
handDetector = HandDetector(min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read() #capture 장비 가져옴
        handLandmarks = handDetector.findHandLandMarks(image=frame, draw=False)

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # detections
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # print(results.right_hand_landmarks) #face, pose, left_hand, right_hand

        if (len(handLandmarks) != 0):
            # and handLandmarks[12][2] < handLandmarks[10][2] and handLandmarks[16][2] < handLandmarks[14][2] and handLandmarks[20][2] < handLandmarks[18][2]
            if handLandmarks[8][2] > handLandmarks[6][2] \
                    and handLandmarks[12][2] > handLandmarks[10][2] \
                    and handLandmarks[16][2] > handLandmarks[14][2] \
                    and handLandmarks[20][2] > handLandmarks[18][2]: # index, middle, ring, little
                print("pam closed")
                break
        # mp_drawing.draw_landmarks(image, results.multi_hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Test', cv2.flip(image, 1))


        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        print(results.multi_hand_landmarks)


cap.release()
cv2.destroyAllWindows()
