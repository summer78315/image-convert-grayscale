# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
# 讀取原始圖像
img = cv2.imread('./miao.png')
# 圖像灰度轉換
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 獲取圖像高度和寬度
height = grayImage.shape[0]
width = grayImage.shape[1]
# 創建一幅圖像
result = np.zeros((height, width), np.uint8)
# 圖像灰度反色變換 DB=255-DA
for i in range(height):
    for j in range(width):
        gray = 255 - grayImage[i, j]
        result[i, j] = np.uint8(gray)
# 顯示圖像
cv2.imshow("Gray Image", grayImage)
cv2.imshow("Result", result)
# 等待顯示
cv2.waitKey(0)
cv2.destroyAllWindows()
