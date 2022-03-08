import cv2
from cvzone.HandTrackingModule import HandDetector
import time

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value
    
    def draw(self, img):
        cv2.rectangle(img, self.pos, 
                      (self.pos[0] + self.width, self.pos[1] + self.height), 
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, 
                      (self.pos[0] + self.width, self.pos[1] + self.height), 
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 35, self.pos[1] + 65), 
                    cv2.FONT_HERSHEY_PLAIN, 2, (50 ,50, 50), 2)
    
    def checkClick(self, x, y):
        if self.pos[0] < x and x < self.pos[0] + self.width and \
            self.pos[1] < y and y < self.pos[1] + self.height:
            cv2.rectangle(img, self.pos, 
                      (self.pos[0] + self.width, self.pos[1] + self.height), 
                      (255, 255, 255), cv2.FILLED)
            cv2.rectangle(img, self.pos, 
                        (self.pos[0] + self.width, self.pos[1] + self.height), 
                        (0, 0, 0), 3)
            cv2.putText(img, self.value, (self.pos[0] + 30, self.pos[1] + 70), 
                        cv2.FONT_HERSHEY_PLAIN, 5, (50 ,50, 50), 5)
            return True
        else:
            return False


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=2)
print("start")
buttons = []
button_value = [["7", "8", "9", "*"],
                ["4", "5", "6", "-"],
                ["1", "2", "3", "+"],
                ["0", "/", ".", "="]]
for i in range(4):
    for j in range(4):
        pos_x = i * 100 + 800
        pos_y = j * 100 + 150
        buttons.append(Button((pos_x, pos_y), 100, 100, button_value[j][i]))
equation = ""
ready = True

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, draw=True, flipType=False)
    cv2.rectangle(img, (800, 50), (800 + 400, 70 + 400), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (800, 50), (800 + 400, 70 + 400), (50, 50, 50), 3)
    for button in buttons:
        button.draw(img)

    if hands:
        lmList = hands[0]["lmList"]
        length, _, img = detector.findDistance(lmList[8], lmList[12], img)
        print("length ->", length)
        x, y = (lmList[8][0] + lmList[12][0])/2.0, (lmList[8][1] + lmList[12][1])/2.0
        if length < 50:
            for i, button in enumerate(buttons):
                if button.checkClick(x, y):
                    input_val = button_value[int(i%4)][int(i/4)]
                    print("your input ->", input_val)
                    if ready or (len(equation) == 0 or input_val != equation[-1]):
                        if input_val == "=":
                            time.sleep(0.15)
                            equation = str(eval(equation))
                        else:
                            equation += input_val
                        ready = False
        else:
            ready = True

    cv2.putText(img, equation, (810, 120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

    cv2.imshow("VirtualCalculator", img)

    key = cv2.waitKey(1)
    if key == 27:
        break

print("over")
cap.release()
cv2.destroyAllWindows()
