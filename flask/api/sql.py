import pymysql
import datetime
pymysql.install_as_MySQLdb()

# 连接数据库
def mysql_conn():
    return pymysql.connect(
        host='81.68.113.102',
        port=3306,
        user='mweb',
        password='123456',
        db='mweb',
        charset='utf8'
    )


# 登录验证
def logincheck(email,pwd):
    conn = mysql_conn()
    cursor = conn.cursor()

    sql = "select * from userinfo where email=\'"+ email+"\'"

    try:
        cursor.execute(sql)
        if cursor is not None:
            #所有    row = cursor.fetchall()
            row = cursor.fetchone()
            if row is not None:
                if(row[1]!=pwd) :
                    cursor.close()
                    conn.close()
                    return -2,0  # 密码错误
                elif(row[1]==pwd)  :
                    cursor.close()
                    conn.close()
                    return 1,row[2]  # 正确
    except Exception as e:
        print(e)
    cursor.close()
    conn.close()
    return -1,0


# 注册验证
def registercheck(email):
    conn = mysql_conn()
    cursor = conn.cursor()
    sql = "select * from userinfo where email=\'"+ str(email)+"\'"
    try:
        cursor.execute(sql)
        if cursor.fetchone() is not None:
            cursor.close()
            conn.close()
            return -1
        else :
            return 1
    except Exception as e:
        print(e)

# 注册用户
def register(email, pwd):
    conn = mysql_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO userinfo (email,name,pwd) VALUE (\'"+ email+"\',\'"+ email+"\',%s);" % pwd
    #sql = "select * from userinfo where email=\'" + email + "\'"
    #sql = "select * from userinfo "
    try:
        cursor.execute(sql)
        conn.commit()

        cursor.close()
        conn.close()
        return 1
    except Exception as e:
        print(e)
    cursor.close()
    conn.close()
    return -3

#获取电影信息
def getallmovies():
    conn = mysql_conn()
    cursor = conn.cursor()

    sql = "select * from movies where rating>8.5"

    try:
        cursor.execute(sql)
        if cursor is not None:
            row = cursor.fetchall()
            if len(row) != 0:
                cursor.close()
                conn.close()
                return row
    except Exception as e:
        print(e)
    cursor.close()
    conn.close()
    return None

#获取系列电影
def getgenre(genre):
    conn = mysql_conn()
    cursor = conn.cursor()

    sql = "select * from movies where genre like %s"
    param=['%' + genre + '%']
    try:
        cursor.execute(sql,param)
        if cursor is not None:
            row = cursor.fetchall()
            if len(row) != 0:
                cursor.close()
                conn.close()
                return row
    except Exception as e:
        print(e)
    cursor.close()
    conn.close()
    return None

#电影搜索
def getsearch(name):
    conn = mysql_conn()
    cursor = conn.cursor()

    sql = "select * from movies where name like %s"
    param = ['%' + name + '%']
    try:
        cursor.execute(sql, param)
        if cursor is not None:
            row = cursor.fetchall()

            if len(row) != 0:
                cursor.close()
                conn.close()
                return row
    except Exception as e:
        print(e)
    cursor.close()
    conn.close()
    return None

#评论展示
def getcomment(id):
    conn = mysql_conn()
    cursor = conn.cursor()
    sql = "select * from comment where id = \'"+ id+"\' "
    print(datetime.datetime.now())
    try:
        cursor.execute(sql)
        if cursor is not None:
            row = cursor.fetchall()
            if len(row) != 0:
                print(datetime.datetime.now())
                cursor.close()
                conn.close()
                return row
    except Exception as e:
        print(e)
    cursor.close()
    conn.close()
    return None

#id搜索影片
def getbyid(id):
    conn = mysql_conn()
    cursor = conn.cursor()
    sql = "select * from movies where id = \'"+ id+"\' "
    try:
        cursor.execute(sql)
        if cursor is not None:
            row = cursor.fetchall()
            if len(row) != 0:
                cursor.close()
                conn.close()
                return row
    except Exception as e:
        print(e)
    cursor.close()
    conn.close()
    return None
