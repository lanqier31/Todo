#!flask/bin/python

import sys
# import xlwt
file='D:\shuqian1.txt'
with open(file) as f:
    line = f.readline()
    while line:
        print line
        line = f.readline()


