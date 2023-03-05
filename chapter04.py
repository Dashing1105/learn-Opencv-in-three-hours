# 图片上放置文本

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img)
# img[200:300, 100:300] = [255, 0, 0]

# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
# 先宽后高   img.shape[1] 表示宽度  img.shape[0] 表示高度  img.shape[2] 表示通道数
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (255, 0, 0), 2)
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

cv2.putText(img, "OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 150, 0))
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
