#coding:gbk
import cv2,os
import matplotlib.pyplot as plt

img = cv2.imread('../imgs/tes01.jpg', 0)    #加载图片，参数0表示灰度图,1表示彩色，-1表示透明通道的彩色图
# print(img)       #若输出为None ，说明没有加载该图片
# cv2.imshow('demo',img)
# cv2.waitKey(0)


# cv2.imwrite('lena_gray.jpg', img)  #保存图片

# capture = cv2.VideoCapture('../imgs/00.mp4')   #播放本地视频
# while(capture.isOpened()):
#     ret, frame = capture.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(30) == ord('q'):
#         break
# print(img.shape)
roi = img[100:300,100:550]
# 自适应均衡化，参数可选
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(roi)
cv2.imshow('roi',cl1)
cv2.waitKey(0)
#固定阈值
# ret,th1 = cv2.threshold(roi,127,255,cv2.THRESH_BINARY)
# #自适应阈值
# th2 = cv2.adaptiveThreshold(roi,220,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,4)
# title = ['Original','Global(v=127)','Adaptive Gaussian']
# images = [roi,th1,th2]
#
# for i in range(3):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(title[i], fontsize=12)
#     plt.xticks([]), plt.yticks([])  # 隐藏坐标轴
#
# plt.show()








