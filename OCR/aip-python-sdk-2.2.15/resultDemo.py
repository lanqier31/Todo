
import pandas as pd
total={}
t1,t2,t3,t4,t5,t6,t7,key=[],[],[],[],[],[],[],[]
data = {'data': {'ret': [{'probability': {'average': 0.887168, 'min': 0.887168, 'variance': 0.0}, 'location': {'height': 8, 'left': 21, 'top': 76, 'width': 6}, 'word_name': '检测结果#1#基因', 'word': 'A'}, {'probability': {'average': 0.795226, 'min': 0.377409, 'variance': 0.035159}, 'location': {'height': 9, 'left': 71, 'top': 76, 'width': 52}, 'word_name': '检测结果#1#转录本编号', 'word': 'NM03503'}, {'probability': {'average': 0.0, 'min': 0.0, 'variance': 0.0}, 'word_name': '检测结果#1#外显子位置', 'word': ''}, {'probability': {'average': 0.702453, 'min': 0.677658, 'variance': 0.007378}, 'location': {'height': 9, 'left': 203, 'top': 76, 'width': 52}, 'word_name': '检测结果#1#核苷酸变化', 'word': '16920A'}, {'probability': {'average': 0.702453, 'min': 0.677658, 'variance': 0.007378}, 'location': {'height': 9, 'left': 253, 'top': 76, 'width': 42}, 'word_name': '检测结果#1#氨基酸变化', 'word': 'Imp564'}, {'probability': {'average': 0.0, 'min': 0.0, 'variance': 0.0}, 'word_name': '检测结果#1#dbSNP', 'word': ''}, {'probability': {'average': 0.0, 'min': 0.0, 'variance': 0.0}, 'word_name': '检测结果#1#突变比例', 'word': ''}, {'probability': {'average': 0.830491, 'min': 0.830491, 'variance': 0.0}, 'location': {'height': 6, 'left': 23, 'top': 102, 'width': 21}, 'word_name': '检测结果#2#基因', 'word': 'HRAUR'}, {'probability': {'average': 0.0, 'min': 0.0, 'variance': 0.0}, 'word_name': '检测结果#2#转录本编号', 'word': ''}, {'probability': {'average': 0.704416, 'min': 0.577812, 'variance': 0.009746}, 'location': {'height': 9, 'left': 151, 'top': 101, 'width': 25}, 'word_name': '检测结果#2#外显子位置', 'word': 'cwnl5'}, {'probability': {'average': 0.704416, 'min': 0.577812, 'variance': 0.009746}, 'location': {'height': 9, 'left': 205, 'top': 101, 'width': 34}, 'word_name': '检测结果#2#核苷酸变化', 'word': 'l799TA'}, {'probability': {'average': 0.704416, 'min': 0.577812, 'variance': 0.009746}, 'location': {'height': 9, 'left': 258, 'top': 101, 'width': 44}, 'word_name': '检测结果#2#氨基酸变化', 'word': 'pVaGh'}, {'probability': {'average': 0.704416, 'min': 0.577812, 'variance': 0.009746}, 'location': {'height': 9, 'left': 331, 'top': 101, 'width': 45}, 'word_name': '检测结果#2#dbSNP', 'word': 'l3488022'}, {'probability': {'average': 0.704416, 'min': 0.577812, 'variance': 0.009746}, 'location': {'height': 9, 'left': 404, 'top': 101, 'width': 1}, 'word_name': '检测结果#2#突变比例', 'word': ''}, {'probability': {'average': 0.772299, 'min': 0.772299, 'variance': 0.0}, 'location': {'height': 8, 'left': 25, 'top': 126, 'width': 20}, 'word_name': '检测结果#3#基因', 'word': 'PAHI'}, {'probability': {'average': 0.91148, 'min': 0.720314, 'variance': 0.007564}, 'location': {'height': 11, 'left': 71, 'top': 124, 'width': 52}, 'word_name': '检测结果#3#转录本编号', 'word': 'NM0019914'}, {'probability': {'average': 0.767024, 'min': 0.618945, 'variance': 0.017058}, 'location': {'height': 11, 'left': 151, 'top': 125, 'width': 26}, 'word_name': '检测结果#3#外显子位置', 'word': 'ccnls'}, {'probability': {'average': 0.767024, 'min': 0.618945, 'variance': 0.017058}, 'location': {'height': 11, 'left': 208, 'top': 125, 'width': 32}, 'word_name': '检测结果#3#核苷酸变化', 'word': '195C>T'}, {'probability': {'average': 0.767024, 'min': 0.618945, 'variance': 0.017058}, 'location': {'height': 11, 'left': 177, 'top': 125, 'width': 217}, 'word_name': '检测结果#3#氨基酸变化', 'word': '33'}, {'probability': {'average': 0.767024, 'min': 0.618945, 'variance': 0.017058}, 'location': {'height': 11, 'left': 318, 'top': 125, 'width': 55}, 'word_name': '检测结果#3#dbSNP', 'word': '991894'}, {'probability': {'average': 0.767024, 'min': 0.618945, 'variance': 0.017058}, 'location': {'height': 11, 'left': 394, 'top': 125, 'width': 1}, 'word_name': '检测结果#3#突变比例', 'word': ''}], 'templateSign': '3f8c7bd213fbe2e82d4f3881f450fdb1', 'templateName': '3突变', 'scores': 1.0, 'isStructured': True, 'logId': '156454964712254', 'clockwiseAngle': 360.0}, 'error_code': 0, 'error_msg': ''}

result = data['data']['ret']

for r in result:
    word_name = r['word_name'].split("#")[-1]
    word=r['word']
    if word_name not in key:
        key.append(word_name)
    if word_name=='基因':
        t1.append(r['word'] if len(r['word'])> 0 else u'/')
    if word_name=='转录本编号':
        t2.append(r['word']if len(r['word'])> 0 else u'/')
    if word_name=='外显子位置':
        t3.append(r['word']if len(r['word'])> 0 else u'/')
    if word_name=='核苷酸变化':
        t4.append(r['word']if len(r['word'])> 0 else u'/')
    if word_name=='氨基酸变化':
        t5.append(r['word']if len(r['word'])> 0 else u'/')
    if word_name=='dbSNP':
        t6.append(r['word']if len(r['word'])> 0 else u'/')
    if word_name == '突变比例':
        t7.append(r['word']if len(r['word'])> 0 else u'/')
total=dict(zip(key,[t1,t2,t3,t4,t5,t6,t7]))
df = pd.DataFrame(total)
print(df)

