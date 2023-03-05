import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
# 所有值为 1 ones  矩阵 5*5 uint8表示整，从0到255
kernel = np.ones((5, 5), np.uint8)

# 灰度处理
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 高斯滤波
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
# 边缘检测
imgCanny = cv2.Canny(img, 100, 100)
# 图像膨胀
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# 图像腐蚀
imgEroded = cv2.erode(imgDilation, kernel)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilate Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
