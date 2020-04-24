import cv2
import numpy as np
import pytesseract


image = cv2.imread('imgs/1194827.jpg', 1)
#二值化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(~gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -20)
# cv2.imshow("cell", binary)
# cv2.waitKey(0)

rows,cols=binary.shape
scale = 10
#识别横线
kernel  = cv2.getStructuringElement(cv2.MORPH_RECT,(cols//scale,1))
eroded = cv2.erode(binary,kernel,iterations = 1)
# cv2.imshow("Eroded Image",eroded)
dilatedcol = cv2.dilate(eroded,kernel,iterations = 1)
# cv2.imshow("Dilated Image",dilatedcol)
# cv2.waitKey(0)

#绘制纵向线 将开始和结束没有线的地方自动画上线段
ys,xs = np.where(dilatedcol>0)
i = 0
dx = np.sort(xs)
dy = np.sort(ys)
dot1=(dx[0],dy[0])
dot2=(dx[-1],dy[0])
dot3=(dx[0],dy[-1])
dot4 = (dx[-1],dy[-1])
cv2.line(binary, dot1, dot3, (255,255,255), 3, 8)
cv2.line(binary, dot2, dot4, (255,255,255), 3, 8)

#识别竖线
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,rows//scale))
eroded = cv2.erode(binary,kernel,iterations = 1)
dilatedrow = cv2.dilate(eroded,kernel,iterations = 1)


cv2.imshow("Dilated Image",dilatedrow)
cv2.waitKey(0)

#标识交点
bitwiseAnd = cv2.bitwise_and(dilatedcol,dilatedrow)
cv2.imshow("bitwiseAnd Image",bitwiseAnd)
cv2.waitKey(0)

#标识表格
merge = cv2.add(dilatedcol,dilatedrow)
cv2.imshow("add Image",merge)
cv2.waitKey(0)

#识别黑白图中的白色点
ys,xs = np.where(bitwiseAnd>0)
mylisty=[]
mylistx=[]

# 通过排序，获取跳变的x和y的值，说明是交点，否则交点会有好多像素值值相近，我只取相近值的最后一点
# 这个10的跳变不是固定的，根据不同的图片会有微调，基本上为单元格表格的高度（y坐标跳变）和长度（x坐标跳变）
i = 0
myxs = np.sort(xs)
for i in range(len(myxs) - 1):
    if (myxs[i + 1] - myxs[i] > 10):
        mylistx.append(myxs[i])
    i = i + 1
mylistx.append(myxs[i])  # 要将最后一个点加入

i = 0
myys = np.sort(ys)
# print(np.sort(ys))
for i in range(len(myys) - 1):
    if (myys[i + 1] - myys[i] > 10):
        mylisty.append(myys[i])
    i = i + 1
mylisty.append(myys[i])  # 要将最后一个点加入
temp={}
# 循环y坐标，x坐标分割表格
for i in range(len(mylisty) - 1):
    for j in range(len(mylistx) - 1):
        # 在分割时，第一个参数为y坐标，第二个参数为x坐标
        ROI = image[mylisty[i] + 3:mylisty[i + 1] - 3, mylistx[j]:mylistx[j + 1] - 3]  # 减去3的原因是由于我缩小ROI范围
        # cv2.imshow("分割后子图片展示：", ROI)
        # cv2.waitKey(0)
        # special_char_list = '`~!@#$%^&*()-_=+[]{}|\\;:‘’，。《》/？ˇ'
        pytesseract.pytesseract.tesseract_cmd = r'D:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
        text1 = pytesseract.image_to_string(ROI)  # 读取文字，此为默认英文
        temp[str(i)].append(text1)
        # text2 = ''.join([char for char in text2 if char not in special_char_list])
        print(temp)
        j = j + 1
    i = i + 1
