import time
import threading
event = threading.Event()

def lighter():
    count =0
    event.set()  #设置绿灯
    while True:
        if count >5 and count<10: #改成红灯
            event.clear() #把标志位清除
            print("此时是红灯")
        elif count>10:
            event.set() #变绿灯了
            count = 0
        else:
            print('此时是绿灯')
            time.sleep(1)
            count+=1
def car(name):
    while True:
        if event.is_set():#代表绿色
            print(name,'正在开')
            time.sleep(1)
        else:
            print('此时红灯',name,'正在等待')
            event.wait() #这个代码很重要，只要它在，就必须绿灯才能往下执行
            print('绿灯'.name,'正在跑')


light = threading.Thread(target=lighter,)
light.start()
car1 = threading.Thread(target=car,args=('Tesla',))
car1.start()
