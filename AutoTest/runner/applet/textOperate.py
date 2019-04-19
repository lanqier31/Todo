import  os

filename = 'report_Ultrasound.txt'

with open(filename, 'r') as file_to_read:

    pos = []
    while True:
        lines = file_to_read.readline() # 整行读取数据
        if not lines:
            break
        print (lines)
        p_tmp, E_tmp = [float(i) for i in lines.split()] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
        pos.append(p_tmp)  # 添加新读取的数据

