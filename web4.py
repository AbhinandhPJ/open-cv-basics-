import cv2
path = "Resources/OIP.jpg"
img = cv2.imread(path)
print(img.shape)
#width, height = 180 , 180
#imgResize = cv2.resize(img,(width,height))
#print(imgResize.shape)
imgCropped = img[90:180,0:144]
imgCropResize = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))
cv2.imshow("Road",img)
#cv2.imshow("Roadresize",imgResize)
cv2.imshow("Roadcropped",imgCropped)
cv2.imshow("Roadcroppedrezize",imgCropResize)



cv2.waitKey(0 )