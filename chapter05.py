# 透视变换

import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")

width, height = 250, 250
pts1 = np.float32([[85, 150], [194, 131], [86, 262], [213, 230]])
pts2 = np.float32([[0.0], [width, 0], [0, height], [width, height]])
# 转换矩阵
matrix = cv2.getPerspectiveTransform(pts1, pts2)
# 透视变换
new_img = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("img", img)
cv2.imshow("output", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
