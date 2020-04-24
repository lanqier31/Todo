#coding:gbk
"""
Desc:jieba分词操作详解
"""
'''
精确分词：jieba.cut()
全模式分词：jieba.cut(cut_all=True)
搜索引擎分子：
自定义词
'''
import jieba

#基本操作

seg_list = jieba.cut('我来到了北京大学')