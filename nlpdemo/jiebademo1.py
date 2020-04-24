#coding: gbk
import  jieba
import jieba.analyse

jieba.load_userdict('./Database/Sample/dict.txt')

text = u'''
左颈IIa-III区可见2枚低回声结节，其一位于颈总动脉分叉处前外侧，大小约1.47*0.44cm，界清，形态规则，皮髓质结构清。 
左颈III-IV区可见2枚低回声结节，其一位于颈内静脉外侧，大小约0.96*0.24cm，界清，形态规则，皮髓质结构清。 
左颈IV区可见多发低回声结节，其一位于颈内静脉后方，大小约0.49*0.19cm，界清，形态规则，皮髓质结构清。
其中左Ⅳ区锁骨上可见一低回声结节，大小约0.53*0.38cm，界清，形态饱满，呈类圆形，皮髓质结构隐约可见，可见血流信号。 
左颈VI区甲状腺左叶下方可见一低回声结节，大小约0.54*0.41cm，界尚清，呈类圆形，皮髓质结构不清，内可见多发点状强回声，血供丰富紊乱
'''

# seg_list = jieba.cut(text,cut_all=False) # cut_all的参数：True为全模式  :切分太细；False 为精确模式，默认为精确模式
# print("Full Mode: " + "/ ".join(seg_list))

keywords = jieba.analyse.extract_tags(text)
print("/".join(keywords))

keywords2 = jieba.analyse.TFIDF(idf_path=None)
print(keywords2)

# seg_list2 = jieba.cut_for_search(text) #搜索引擎模式
# for s in seg_list2:
#     print(s)