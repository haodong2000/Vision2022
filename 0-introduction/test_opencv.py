# -*- coding: utf-8 -*-

import cv2

def show_image(path):
    print(path)
    img = cv2.imread(path)
    cv2.imshow("kitty", img)
    key = cv2.waitKey(0)
    if key == 'q' or key == '27':
        cv2.destroyAllWindows()


if __name__ == '__main__':
    path = "../images/cat.jpg"
    show_image(path)
