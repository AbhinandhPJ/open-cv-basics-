import cv2
import numpy as np
import util6




frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

while True:
    success, img = cap.read()

    #cv2.imshow("Video", img)
    kernel = np.ones((5, 5), np.uint8)
    print(kernel)
    #path = ("Resources/lena.png")
    #img = cv2.imread(path)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (11, 11), 0)
    imgCanny = cv2.Canny(imgBlur, 100, 100)
    imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgEroded = cv2.erode(imgDialation, kernel, iterations=2)
    #cv2.imshow("lena", img)
    #cv2.imshow("gena", imgGray)
    # cv2.imshow("bena", imgBlur)
    # cv2.imshow("cena", imgCanny)
    # cv2.imshow("dena", imgDialation)
    # cv2.imshow("eena", imgEroded)
    imgStacked = util6.stackImages( 0.5, ([img, imgGray, imgBlur], [imgCanny, imgEroded, imgDialation]))
    cv2.imshow("stacked", imgStacked)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

    # cv2.waitKey(0)










