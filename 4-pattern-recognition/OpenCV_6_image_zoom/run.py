import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
 
detector = HandDetector(detectionCon=0.8)
startDist = None
scale = 0
cx, cy = 360, 640

print("start")

img_1 = cv2.imread("kung_fu_pandas.jpg")
img_1 = cv2.resize(img_1, (180, 240))
cv2.imwrite("kung_fu_pandas.jpg", img_1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    img_1 = cv2.imread("kung_fu_pandas.jpg")

    if len(hands) == 2:
        # print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1]))
        if detector.fingersUp(hands[0]) == [0, 1, 0, 0, 0] and \
                detector.fingersUp(hands[1]) == [0, 1, 0, 0, 0]:
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            # point 8 is the tip of the index finger
            if startDist is None:
                length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
                print("length ->", length)
                startDist = length
  
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
            scale = int((length - startDist) // 2)
            print("info ->", info)
            cy, cx = info[4:]
    else:
        startDist = None
 
    try:
        w1, h1, _ = img_1.shape
        new_W, new_H = ((w1 + scale) // 2) * 2, ((h1 + scale) // 2) * 2
        img_1 = cv2.resize(img_1, (new_W, new_H))
        print("scale ->", scale, " w1, h1, new_W, new_H ->", w1, h1, new_W, new_H, " img_1.shape ->", img_1.shape)
        print("cx, cy ->", cx, cy)
        print("cx - (new_H // 2):cx + (new_H // 2), cy - cy - (new_W // 2):cy + (new_W // 2) ->", 
            cx - (new_H // 2), cx + (new_H // 2), cy - (new_W // 2), cy + (new_W // 2))
        print(" - ->", cx + (new_H // 2) - (cx - (new_H // 2)), 
            "  - ->", cy + (new_W // 2) - (cy - (new_W // 2)))
        img[cx - (new_H // 2):cx + (new_H // 2), 
            cy - (new_W // 2):cy + (new_W // 2)] = img_1
        # img[0:224, 0:300] = img_1 
    except:
        print("exception raised")
        pass
 
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:
        break

print("over")
cv2.destroyAllWindows()
cap.release()
