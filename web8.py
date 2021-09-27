import cv2
import numpy as np
circles =np.zeros((4,2),np.int)
counter = 0

def mouseclick(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[c]=x,y
        c = c+1
        print(x,y)




img = cv2.imread("Resources/cards.jpg")
while True:
    if  c == 4:
     width, height = 250 ,350
     pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])

     pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
     matrix = cv2.getPerspectiveTransform(pts1, pts2)
     imgOutput = cv2.warpPerspective(img, matrix, (width, height))
     cv2.imshow("Output", imgOutput)
    for x in range(0, 4):
       cv2.circle(img,(circles[x][0],circles[x][1]),5,(255,0,0),3)

cv2.imshow("cards",img)
cv2.setMouseCallback("cards", mouseclick)
cv2.waitKey(0)