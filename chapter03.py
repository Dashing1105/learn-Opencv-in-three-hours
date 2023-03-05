import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)
# 重定义大小
imgResize = cv2.resize(img, (400, 180))
print(imgResize.shape)
# 裁剪
imgCropped = img[:200, :300]
print(imgCropped.shape)

cv2.imshow("Image", img)
cv2.imshow("ImageResize", imgResize)
cv2.imshow("ImageCropped", imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
