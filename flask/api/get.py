from flask import Flask, render_template, request, Response, Blueprint
import json
import api.sql as sql
import api.rec.recommend as recd
getallemail_api = Blueprint('getallemail_api', __name__)
getgenre_api = Blueprint('getgenre_api', __name__)
getsearch_api = Blueprint('getsearch_api', __name__)
getcomment_api = Blueprint('getcomment_api', __name__)
getrecommend_api = Blueprint('getrecommend_api', __name__)

@getallemail_api.route('/api/getallmoives', methods=['POST'])
def getallmovies():

    res = sql.getallmovies()
    if (res != None):
        movies = []
        for i in range(50):
            tags = []
            list = res[i][6].replace("\'", '')
            list = list.replace("[", '')
            list = list.replace("]", '')
            list = list.split(',')
            for j in range(len(list)):
                tag = list[j]
                tags.append(tag)
            movie_data = {'id': res[i][0], 'name': res[i][1], 'year': res[i][2], 'rating': res[i][3], 'img': res[i][5],
                          'tags': tags, 'summary': res[i][7], 'genre': res[i][8], 'country': res[i][9], 'show': False}
            movies.append(movie_data)

        return Response(json.dumps({'code': 1000, 'msg': "success", 'data': movies}))
    else:
        return json.dumps({'code': 1004, 'msg': "error", 'data': {'detail': '其他错误'}})


@getgenre_api.route('/api/getgenre/<genre>', methods=['POST'])
def getgenre(genre):
    res = sql.getgenre(genre)
    if (res != None):
        movies = []
        lens = len(res)
        if lens > 50:
            lens = 50
        for i in range(lens):
            tags = []
            list = res[i][6].replace("\'", '')
            list = list.replace("[", '')
            list = list.replace("]", '')
            list = list.split(',')
            for j in range(len(list)):
                tag = list[j]
                tags.append(tag)
            movie_data = {'id': res[i][0], 'name': res[i][1], 'year': res[i][2], 'rating': res[i][3], 'img': res[i][5],
                          'tags': tags, 'summary': res[i][7], 'genre': res[i][8], 'country': res[i][9], 'show': False}
            movies.append(movie_data)

        return Response(json.dumps({'code': 1000, 'msg': "success", 'data': movies}))
    else:
        return Response(json.dumps({'code': 1004, 'msg': "error", 'data': {'detail': '其他错误'}}))


@getsearch_api.route('/api/getsearch/<name>', methods=['POST'])
def getsearch(name):
    res = sql.getsearch(name)

    if (res != None):
        movies = []
        lens = len(res)
        if lens > 100:
            lens = 100
        for i in range(lens):
            tags = []
            list = res[i][6].replace("\'", '')
            list = list.replace("[", '')
            list = list.replace("]", '')
            list = list.split(',')
            for j in range(len(list)):
                tag = list[j]
                tags.append(tag)
            movie_data = {'id': res[i][0], 'name': res[i][1], 'year': res[i][2], 'rating': res[i][3], 'img': res[i][5],
                          'tags': tags, 'summary': res[i][7], 'genre': res[i][8], 'country': res[i][9], 'show': False}
            movies.append(movie_data)

        return Response(json.dumps({'code': 1000, 'msg': "success", 'data': movies}))
    else:
        return Response(json.dumps({'code': 1004, 'msg': "error", 'data': {'detail': '没查找到'}}))


@getcomment_api.route('/api/getcomment/<id>', methods=['POST'])
def getcomment(id):
    res = sql.getcomment(id)
    if (res != None):
        com = []
        num=1

        for i in range(len(res)):
            com_data = {'id': num, 'name': res[i][0], 'comment': res[i][1], }
            com.append(com_data)
            num=num+1

        return Response(json.dumps({'code': 1000, 'msg': "success", 'data': com}))
    else:
        return Response(json.dumps({'code': 1004, 'msg': "error", 'data': {'detail': '没查找到'}}))
        
@getrecommend_api.route('/api/getrecommend', methods=['POST'])
def getrecommend():
    info = request.get_json()
    strs = info.get('info')
    id,dst,emo=recd.recommend(strs)
    for i in range(11):
        for j in range(7):
            emo[i][j]=round(emo[i][j], 1)

    movies=[]
    for i in id:
        im=str(i)
        res=sql.getbyid(im)

        if (res != None):
            tags = []
            list = res[0][6].replace("\'", '')
            list = list.replace("[", '')
            list = list.replace("]", '')
            list = list.split(',')
            for j in range(len(list)):
                tag = list[j]
                tags.append(tag)
            movie_data = {'id': res[0][0], 'name': res[0][1], 'year': res[0][2], 'rating': res[0][3], 'img': res[0][5],
                          'tags': tags, 'summary': res[0][7], 'genre': res[0][8], 'country': res[0][9], 'show': False}
            movies.append(movie_data)
    if(len(movies)>0):
        return Response(json.dumps({'code': 1000, 'msg': "success", 'data': movies,'list':emo}))
    else:
        return Response(json.dumps({'code': 1004, 'msg': "error", 'data': {'detail': '没查找到'}}))
