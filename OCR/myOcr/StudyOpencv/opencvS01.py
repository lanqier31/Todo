#coding:gbk
import cv2,os
import matplotlib.pyplot as plt

img = cv2.imread('../imgs/tes01.jpg', 0)    #����ͼƬ������0��ʾ�Ҷ�ͼ,1��ʾ��ɫ��-1��ʾ͸��ͨ���Ĳ�ɫͼ
# print(img)       #�����ΪNone ��˵��û�м��ظ�ͼƬ
# cv2.imshow('demo',img)
# cv2.waitKey(0)


# cv2.imwrite('lena_gray.jpg', img)  #����ͼƬ

# capture = cv2.VideoCapture('../imgs/00.mp4')   #���ű�����Ƶ
# while(capture.isOpened()):
#     ret, frame = capture.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(30) == ord('q'):
#         break
# print(img.shape)
roi = img[100:300,100:550]
# ����Ӧ���⻯��������ѡ
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(roi)
cv2.imshow('roi',cl1)
cv2.waitKey(0)
#�̶���ֵ
# ret,th1 = cv2.threshold(roi,127,255,cv2.THRESH_BINARY)
# #����Ӧ��ֵ
# th2 = cv2.adaptiveThreshold(roi,220,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,4)
# title = ['Original','Global(v=127)','Adaptive Gaussian']
# images = [roi,th1,th2]
#
# for i in range(3):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(title[i], fontsize=12)
#     plt.xticks([]), plt.yticks([])  # ����������
#
# plt.show()








