import pymysql

class Mysql:
    db = pymysql.connect(
        host='localhost',
         user='root',
        password='bxdwQQ6625',
        db='test',
        charset='utf8', )


    def create_sql(self):
        cur = self.db.cursor()
        try:
            cerate = "create table zhuce (username text , password text)"
            cur.execute(cerate)
        except Exception as e:
            print("创建数据表失败", e)
        else:
            print("创建数据表成功！")

    def insert_sql(self , username , password):
        cur = self.db.cursor()
        try:
            ins_sql = "insert into zhuce values('%s' , '%s')" %(username , password)
            cur.execute(ins_sql)
            self.db.commit()
        except Exception as e:
            print("插入数据失败！",e)
        else:
            print("插入数据成功！")

    def select_user(self,username, password):
        # conn = pymysql.connect(host="localhost", user="root", password="bxdwQQ6625", db="test", charset="utf8")
        cur = self.db.cursor()
        select_sql = 'select username,password from zhuce '
        # try:
        cur.execute(select_sql)
        self.db.commit()
        result = cur.fetchall()
        for i in range(len(result)):
            if username == result[i][0] and password == result[i][1]:
                # print('yes')
                return 1
                break
            else:
                continue
            print('no')
            return False

    def select_school(self,school_name):
        cur_dict = self.db.cursor(cursor=pymysql.cursors.DictCursor)             #游标内参数使返回值为字典
        select_sql = "select SchoolCode,SchoolName,SchoolUrl from school where SchoolName = '%s'"%school_name
        cur_dict.execute(select_sql)
        self.db.commit()
        msg = cur_dict.fetchall()
        if msg :
            return msg
            print(msg)
        else:
            return '搜索错误！'
            print('error')

        #pass

    def insert_school(self,SchoolName):
        cur_ins = self.db.cursor()
        cur_dict = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        #检查school表是否存在该学校
        chack_sql = "select SchoolName from school where SchoolName = '%s'" %SchoolName
        cur_dict.execute(chack_sql)
        self.db.commit()
        chack_msg = cur_dict.fetchall()
        if chack_msg:
            return '该学校已存在'
        #从all_school表中获取数据
        select_sql = "select SchoolCode,SchoolName from all_school where SchoolName = '%s'" %SchoolName
        try:
            cur_dict.execute(select_sql)
            self.db.commit()
        except Exception as ex:
            print('SELECT ERROR!',ex)
        else:
            select_msg = cur_dict.fetchall()
            SchoolCode = select_msg[0]['SchoolCode']
            print(SchoolCode)
            #SchoolUrl = select_msg['SchoolUrl']
        #向school表中插入数据
        try:
            insert_sql = "insert into school_test values('%s','%s','')"%(SchoolCode,SchoolName)
            cur_ins.execute(insert_sql)
            self.db.commit()
        except Exception as e:
            print('Error',e)
            return 'ERROR'
        else:
            print('OK!')
            return 'OK!'



if __name__ == '__main__':
    pass