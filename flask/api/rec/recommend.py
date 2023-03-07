# from sklearn.neighbors import NearestNeighbors
from joblib import dump, load
import emotext as ex
import numpy as np
import pickle
from collections import namedtuple

def softmax_dict(x: dict):
    s = sum(v for v in x.values())
    for k in x:
        x[k] /= s
    return x

def recommend(text):
    emo=[]
    vary = [2, 5, 1, 4, 3, 5, 1]
    feature = ['乐', '好', '怒', '哀', '惧', '恶', '惊']
    nbrs = load('/www/wwwroot/newflask/api/rec/nbrs.pkl')
    t = text
    Emotext = ex.Emotions()
    r = Emotext.emotion_count(t)
    Emotion = namedtuple('Emotion', ex.emotions)
    r.emotions = softmax_dict(r.emotions)
    e = Emotion(**r.emotions)
    print(e)
    value_1 = []
    n = 0
    for i in range(len(vary)):
        value = 0
        for j in range(vary[i]):
            value += e[n]
            n += 1
        value += 0.2
        value_1.append(value)
    emo.append(value_1)
    distances, indices = nbrs.kneighbors([e], 10)#推荐五个
    X = np.load("/www/wwwroot/newflask/api/rec/save_x.npy")  # 读取文件
    print(X[0])
    data_ids = np.loadtxt('/www/wwwroot/newflask/api/rec/data_ids.txt', dtype=bytes).astype(int)
    data_ids = list(data_ids)
    #print(len(data_ids))
    dst=[]
    id=[]
    for i in range(len(indices[0])):
        dst.append(distances[0][i])
        idx = indices[0][i]
        id.append(data_ids[idx])
        #print(id)
        #print(distances[0][i])
        value_2 = []
        n = 0
        for i in range(len(vary)):
            value = 0
            for j in range(vary[i]):
                value += X[idx][n]
                n += 1
            value += 0.2
            value_2.append(value)
        emo.append(value_2)
    # file = open('recommend_ids.txt', 'a')
    # mid = str(id).replace('[', '').replace(']', '')
    # # 删除单引号并用字符空格代替逗号
    # mid = mid.replace("'", '').replace(',', '') + '\n'
    # file.write(mid)
    # file.close()
    # np.save('recommend_value', emo)
    return id,dst,emo
    


    # t = text
    # Emotext = ex.Emotions()
    # r = Emotext.emotion_count(t)
    # Emotion = namedtuple('Emotion', ex.emotions)
    
    
    # r.emotions = softmax_dict(r.emotions)
    # e = Emotion(**r.emotions)
    # #print(e)
    # distances, indices = nbrs.kneighbors([e], 10)#推荐N个
    # data_ids = np.loadtxt('/www/wwwroot/newflask/api/rec/data_ids.txt', dtype=bytes).astype(int)
    # data_ids = list(data_ids)
    # #print(len(data_ids))
    # dst=[]
    # id=[]
    # for i in range(len(indices[0])):
    #     dst.append(distances[0][i])
    #     idx = indices[0][i]
    #     id.append(data_ids[idx])
    #     #print(id)
    #     #print(distances[0][i])
    # return id,dst

def main():
    id,dst,emo=recommend('我开心')
    file = open('ids.txt', 'a')
    mid = str(id).replace('[', '').replace(']', '')
    # 删除单引号并用字符空格代替逗号
    mid = mid.replace("'", '').replace(',', '') + '\n'
    file.write(mid)
    file.close()
