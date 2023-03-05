import cv2

# img = cv2.imread("Resources/lena.png")
cap = cv2.VideoCapture("Resources/test_video.mp4")
# cap = cv2.VideoCapture(0)
cap.set(3, 640)      # 宽
cap.set(4, 480)      # 高
cap.set(10, 100)      # 亮度

# cv2.imshow("Output", img)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
