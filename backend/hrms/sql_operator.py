import pymysql
import datetime
import pymysql
import re
import time
import codecs
import sys
sys.setrecursionlimit(1500)


""" 连接数据库 """
cur = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=6666, db='humansource', charset='utf8')
cur.commit()
db = cur  # 数据库

""" 创建表需要的head字段 """
account = ["Name", "Password"]
staff = ["ID"]
department = ["Department_id", "Department_name", "Manager_id", "Affairs"]
position = ["Position_id", "Position_rank", "Position_name", "Salary", "Post_number", "Post_already"]
user_info = ['ID', 'Sex', 'Name', 'Email', 'Phone']
employee = ["Employee_id", "Department_id", "Position_id", "Hire_date", "State"]
experience = ["ID", "Work_experience", "Achievement"]

def table_exists(cur, table_name):  # 这个函数用来判断表是否存在
    cur.execute( "show tables;")
    tables = [cur.fetchall()]
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        return True  # 存在
    else:
        return False  # 不存在

# 创建表
def create_table_head(db ,table, head):
    """
    :param db:  数据库
    :param table: 表名
    :param head:  表头名
    :return:
    """
    sql = 'create table if not exists {}('.format(table)  # 创建表
    for i in range(0, len(head)):
        sql += '`{}` varchar(50)'.format(head[i])
        if i != len(head) - 1:
            sql += ','
        sql += '\n'
    sql += ');'
    try:
        cur = db.cursor()  # 创建光标
        if (table_exists(cur, table)):
            print(table,"表已经存在")
        else:
            cur.execute(sql)  # 执行命令
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table,'表创建完成')
    except Exception as e:
        print(table,'表创建失败,失败原因', e)

# 插入数据
def insert_table_info( db,table, info):
    sql = 'insert into {} values ('.format(table)
    for i in range(0, len(info)):
        sql += '"{}" '.format(info[i])
        if i != len(info) - 1:
            sql += ','
    sql += ');'
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table,'表数据插入成功')
        else:
            print(table,'表不存在')
    except Exception as e:
        print(table,'表数据插入失败,失败原因', e)

# 表需要的数据
def insert_alltable_info(db, table,filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        row = 0
        for line in f.readlines():
            data = line.split()  # 遍历文件中每一行
            row += 1
            if row == 1: continue
            rowdata = data[0].split(',')
            """ 先查询数据是否已经存在 """
            searchdata = search_table_info(db,table)
            if rowdata in searchdata:
                print(rowdata,"数据已存在")
            else:
                insert_table_info(db, table,rowdata)  # 存储单条数据

def search_table_info(db,table):
    sql = 'SELECT * FROM {}'.format(table)
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            result = cur.fetchall()
            print(table, '表数据查询成功')
            searchdata = []
            for item in result:
                searchdata.append(list(item))
            print(table, "表存在", len(searchdata), "条数据")
            return searchdata
        else:
            print(table, '表不存在')
    except Exception as e:
        print(table, '表数据查询失败,失败原因', e)

def delete_table_info( db, table,table_head,head_value):
    # SQL语句删除数据
    sql = 'DELETE FROM {} WHERE {} = {}'.format(table,table_head,head_value)
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table, '表中',head_value,'该条数据删除成功')
        else:
            print(table, '表不存在')
    except Exception as e:
        print(table, '表数据删除失败,失败原因', e)

def update_table_info(db, table,table_head1,head_value1,table_head2,head_value2):
    # SQL语句更新数据
    sql = 'UPDATE {} SET {}= {} WHERE {} = {}'.format(table,table_head1,head_value1,table_head2,head_value2)
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table, '表中',head_value2,'该条数据修改成功')
        else:
            print(table, '表不存在')
    except Exception as e:
        print(table, '表数据修改失败,失败原因', e)


# 创建表
def create_table_head(db ,table, head):
    """
    :param db:  数据库
    :param table: 表名
    :param head:  表头名
    :return:
    """
    sql = 'create table if not exists {}('.format(table)  # 创建表
    for i in range(0, len(head)):
        sql += '`{}` varchar(50)'.format(head[i])
        if i != len(head) - 1:
            sql += ','
        sql += '\n'
    sql += ');'
    try:
        cur = db.cursor()  # 创建光标
        if (table_exists(cur, table)):
            print(table,"表已经存在")
        else:
            cur.execute(sql)  # 执行命令
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table,'表创建完成')
    except Exception as e:
        print(table,'表创建失败,失败原因', e)

# 插入数据
def insert_table_info(db,table, info):
    sql = 'insert into {} values ('.format(table)
    for i in range(0, len(info)):
        sql += '"{}" '.format(info[i])
        if i != len(info) - 1:
            sql += ','
    sql += ');'
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            # print(table,'表数据插入成功')
            return True
        else:
            # print(table,'表不存在')
            return False
    except Exception as e:
        print(table,'表数据插入失败,失败原因', e)
        return False


# 表需要的数据
def insert_alltable_info(db, table,**kwargs):
    rowdata = []
    for key, value in kwargs.items():
        rowdata.append(str(value))

    """ 先查询数据是否已经存在 """
    searchdata = search_table_info(db,table)
    if rowdata in searchdata:
        print("该条数据已存在")
        return False
    else:
        if insert_table_info(db, table,rowdata):  # 存储单条数据
            return True
        else:
            return False


def search_table_info(db,table):
    sql = 'SELECT * FROM {}'.format(table)
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            result = cur.fetchall()
            # print(table, '表数据查询成功')
            searchdata = []
            for item in result:
                searchdata.append(list(item))
            # print(table, "表存在", len(searchdata), "条数据")
            return searchdata
        else:
            # print(table, '表不存在')
            return None
    except Exception as e:
        print(table, '表数据查询失败,失败原因', e)

def delete_table_info(db, table,table_head,head_value):
    # SQL语句删除数据
    sql = "DELETE FROM {} WHERE {} = '%s'".format(table,table_head) % head_value
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table, '表中', head_value, '该条数据删除成功')
            return True
        else:
            print(table, '表不存在')
            return False
    except Exception as e:
        print(table, '表数据删除失败,失败原因', e)
        return False

def update_table_info(db, table,table_head1,head_value1,table_head2,head_value2):
    # SQL语句更新数据
    sql = "UPDATE {} SET {}= '%s' WHERE {} = '%s'".format(table,table_head1,table_head2) % (head_value1,head_value2)
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table, '表中',head_value2,'该条数据修改成功')
            return True
        else:
            print(table, '表不存在')
            return False
    except Exception as e:
        print(table, '表数据修改失败,失败原因', e)
        return False

'''
    登录
    传入参数：{id,password}
    查询该idpassword是否存在于Account表，
        若存在，返回True
        不存在，返回False
'''
def login(db,**kwargs):
    # 获取已注册用户的账户ID和密码
    account_datas = search_table_info(db, "account")
    for i in range(len(account_datas)):
        account_name = account_datas[i][0]   # 得到用户名
        if account_name == kwargs['id']:
            # 找到用户名一样的判断密码是否正确：
            if account_datas[i][1] == kwargs['password']:
                return True
            else:
                print("密码错误！")
                return False
        else:
            print("用户名不存在！")
            return False

""" 
    根据id换成对应的name 【供部门id和职位id和雇员id的兑换使用】
    传入参数：表名，id
    返回数据：name
"""
def id_name(db,table_name,id):
    # 获取Department_info
    infos = search_table_info(db, table_name)
    id_all = [rowdata[0] for rowdata in infos]
    for index, temp_id in enumerate(id_all):
        if temp_id == id:  # 根据id查询到对应的数据
            if table_name == 'position2':
                Name =infos[index][2]
                return Name
            elif table_name == 'department':
                Name = infos[index][1]
                return Name
            elif table_name == 'user_info':
                Name = infos[index][2]
                return Name
            else:
                return None


'''
    获取个人信息
    传入参数：{ID}
    查询User_info表和Employee表和experience表，将查询的个人信息汇总至一个字典中
        若查到个人信息，返回{status:True,data:{id,sex,name,Email,phone,department_name,position_name,Hire_date,Work_experience}}，其中Work_experience是list类型
        若未查找到此人，返回{status:False,data:{}}，其中data为空
'''
def getUserinfo(db,kwargs):
    # 获取User_info表和Employee表的信息
    print(db)
    print(kwargs)
    user_info_datas = search_table_info(db, "user_info")
    employee_datas = search_table_info(db, "employee")
    experience_datas = search_table_info(db, "experience")

    user_info_id_all = [rowdata[0] for rowdata in user_info_datas]  # 得到用户名
    employee_id_all = [rowdata[0] for rowdata in employee_datas]  # 得到用户名
    experienc_id_all = [rowdata[0] for rowdata in experience_datas]  # 得到用户名
    print(kwargs)

    if kwargs['ID'] in user_info_id_all and kwargs['ID'] in employee_id_all:
        for i in range(len(user_info_datas)):
            account_id = user_info_datas[i][0]  # 得到用户名
            if account_id == kwargs['ID']:
                for j in range(len(employee_datas)):
                    account_id2 = employee_datas[j][0]  # 得到用户名
                    if account_id2 == kwargs['ID']:
                        data = {}
                        for m in range(len(user_info_datas[i])):
                            data[user_info[m]] = user_info_datas[i][m]
                        for n in range(len(employee_datas[j])):
                            if n == 0 or n == len(employee_datas[j])-1: continue
                            if employee[n] == 'Department_id':
                                data['Department_name'] = id_name(db,'department',employee_datas[i][n])
                            elif employee[n] == 'Position_id':
                                data['Position_name'] = id_name(db,'position2',employee_datas[i][n])
                            else:
                                data[employee[n]] = employee_datas[i][n]

                        if len(experienc_id_all) != 0:
                            experience_data = []
                            for i in range(len(experienc_id_all)):
                                if experienc_id_all[i] == kwargs['ID']:
                                    temp = {}
                                    for j in range(len(experience_datas[i])):
                                        if j == 0:continue
                                        temp[experience[j]] = experience_datas[i][j]
                                    experience_data.append(temp)
                            data['Work_experience'] = experience_data
                        else:
                            data['Work_experience'] = []
                        return {'status':True,'data':data}
    else:
        return {'status':False,'data':{}}

'''
    员工录用
    传入参数：{Sex,Name,Email,Phone,Hire_date,Work_experience}，其中Work_experience是list类型
    需要先查employee表，然后为员工分配一个唯一的Employee_id，向Staff表插入一条新纪录，并将其他信息插入Employee表
    然后，向employee表，experience表，position表插入数据
        若分配成功，返回True
        若分配不成功，返回False
'''
def hire(db,kwargs):
    # 修改Employee表的信息：
    employee_infos = search_table_info(db, "employee")
    lenth = len(employee_infos)
    Employee_id = str(lenth+1).zfill(4)
    curr_time = datetime.datetime.now()
    Hire_date = curr_time.strftime("%Y/%m/%d")

    user_data = {}
    for i in range(len(user_info)):
        if i == 0:
            user_data[user_info[i]] = Employee_id
        else:
            user_data[user_info[i]] = kwargs[user_info[i]]

    Employee_info = {}
    for i in range(len(employee)):
        if i == 0:
            Employee_info[employee[i]] = Employee_id
        elif i ==1:
            Employee_info[employee[i]] = 0
        elif i == 2:
            Employee_info[employee[i]] = 'G1'
        elif i == 3:
            Employee_info[employee[i]] = kwargs[employee[i]]
        else:
            Employee_info[employee[i]] = 1


    Work_experience = kwargs['Work_experience']
    for i in range(len(Work_experience)):
        experience_info = {}
        for j in range(len(experience)):
            if j == 0:
                experience_info[experience[j]] = Employee_id
            else:
                experience_info[experience[j]] = Work_experience[i][experience[j]]
        insert_alltable_info(db, "experience", **experience_info)

    if insert_alltable_info(db, "user_info", **user_data) and insert_alltable_info(db, "employee",**Employee_info):  # 插入数据
        return True
    else:
        return False

'''
    获取部门信息
    传入参数：{}
    首先查询department表
        若department_name不存在，返回False
        若存在：
            删除该条记录；
            并在Employee表中按该部门的Manager_id查找用户，将其position改为普通员工；
            若成功，返回的数据格式：{status:True,data:[{Department_id,Department_name,Manager,Affairs}]}
            若失败，返回数据：{status:False}
'''
def getDepartmentinfo(db):
    # 获取部门表
    department_infos = search_table_info(db, "department")
    # 获取user_info表
    user_infos = search_table_info(db, "user_info")
    info = []
    for i in range(len(department_infos)):
        info_temp = {}
        info_temp['Department_id'] = department_infos[i][0]
        info_temp['Department_name'] = department_infos[i][1]
        flag = 0
        for j in range(len(user_infos)):
            if user_infos[j][0] == department_infos[i][2]:
                info_temp['Manager'] =  user_infos[j][2]
                flag = 1
        if flag == 0:
            info_temp['Manager'] = '暂无'
        info_temp['Affairs'] = department_infos[i][3]
        info.append(info_temp)
    if len(info) == 0:
        return {'status':False}
    else:
        return {'status':True,'data':info}


'''
    修改部门信息
    传入参数：{Department_id,New_Department_name,New_Manager_id,New_Affairs}
    根据Department_id查找Department表
        若为找到该部门，返回False
        若找到；
            按照传入信息在Department表中更改该条记录
            若Manager_id发生了改变，则在Employee表中更改涉及到的两位员工的position信息
'''
def updateDepartment(db,kwargs):
    # 获取Department_info
    department_infos = search_table_info(db, "department")
    department_id_all = [rowdata[0] for rowdata in department_infos]

    for index, department_id in enumerate(department_id_all):
        if department_id == kwargs['Department_id']:  # 根据id查询到该条记录
            department_name = department_infos[index][1]
            department_Manageg = department_infos[index][2]
            department_Affairs = department_infos[index][3]
            # 接下来判断是否修改
            if department_name == kwargs['New_Department_name'] and department_Manageg == kwargs['New_Manager_id'] and department_Affairs== kwargs['New_Affairs']:
                return True
            else:
                if update_table_info(db, "department", 'Department_name', kwargs['New_Department_name'], 'Department_id', department_id) and \
                        update_table_info(db, "department", 'Manager_id', kwargs['New_Manager_id'], 'Department_id',department_id) and \
                        update_table_info(db, "department", 'Affairs', kwargs['New_Affairs'], 'Department_id',department_id):
                    return True
                else:
                    return False


'''
    部门内员工职位调整
    传入参数：{Employee_id,New_Department_name,New_Position_name}
    首先，按id查找该员工，按Department_name查找该部门,按Position_id查找岗位
        若未找到该员工或部门，岗位，返回False
        若都找到：
            1. 若position与原来不同，更新员工的Position_id属性值，更新Position表
            2. 若Department与原来不同，更新员工的Department_id属性
            3. 若该员工原本的职位为部门经理，则更改department表相应的Manager_id属性
            4. 若Position_id为部门经理对应的id，则更改department表相应的Manager_id属性
            5. 返回True
'''
def updateStaffStatus(db,kwargs):
    # 获取员工_info
    employee_infos = search_table_info(db, "employee")
    employee_id_all = [rowdata[0] for rowdata in employee_infos]
    # 获取Department_info
    department_infos = search_table_info(db, "department")
    # 获取Position_info
    Position_infos = search_table_info(db, "position2")
    for index, employee_id in enumerate(employee_id_all):
        if employee_id == kwargs['Employee_id']:  # 根据id查询到该员工
            department_idnow = employee_infos[index][1]
            Position_idnow = employee_infos[index][2]
            department_id_new,Position_id_new,new_post_already,now_post_already,new_post_num = 0,0,0,0,0
            print('Position_idnow is: ',Position_idnow)
            # 查询到department和Position的id
            for j in range(len(department_infos)):
                if department_infos[j][1] == kwargs['Department_name']:
                    department_id_new = department_infos[j][0]
            for j in range(len(Position_infos)):
                if Position_infos[j][2] == kwargs['Position_name']:
                    Position_id_new = Position_infos[j][0]
                    new_post_already = Position_infos[j][5]
                    new_post_num = Position_infos[j][4]
                if Position_infos[j][0] == Position_idnow:
                    print('find')
                    now_post_already = Position_infos[j][5]

            if int(new_post_already) >= int(new_post_num) :
                return False
            else:
                if department_id_new == 0 or Position_id_new==0:
                    return False
                else:
                    # 接下来判断是否修改
                    if Position_idnow == Position_id_new and department_idnow == department_id_new:
                        return True
                    else:
                        print('update once')
                        print(int(now_post_already),now_post_already)
                        update_table_info(db, "employee", 'Position_id', Position_id_new, 'Employee_id',employee_id )
                        update_table_info(db, "employee", 'Department_id', department_id_new, 'Employee_id',employee_id )
                        update_table_info(db, "position2", 'Post_already', int(now_post_already) - 1, 'Position_id', Position_idnow)
                        update_table_info(db, "position2", 'Post_already', int(new_post_already) + 1, 'Position_id',Position_id_new)

                        # 3.若该员工原本的职位为部门经理，则更改department表相应的Manager_id属性     C1是部门经理
                        if Position_idnow  == 'C1':
                            update_table_info(db, "department", 'Manager_id', 0000, 'Department_id', department_idnow)
                        # 4.若Position_id为部门经理对应的id，则更改department表相应的Manager_id属性
                        if Position_id_new  == 'C1':
                            update_table_info(db, "department", 'Manager_id', employee_id, 'Department_id', department_id_new)
                        return True
    return False


'''
    为员工分配岗位
    传入参数：{ID,Department_id,Position_id}
    查询Position表：
        若该职位已达最大人数限制，分配失败，返回False
        若未达最大人数限制
            1. 更改employee表，position表，
            2. 若Position_id为总经理的id则更改department表
            3. 返回True
'''
def disTribution(db,kwargs):
    print('kwargs is:  ',kwargs)
    # 获取Position_info
    Position_infos = search_table_info(db, "position2")
    Position_id_all = [rowdata[0] for rowdata in Position_infos]
    # 获取员工_info
    employee_infos = search_table_info(db, "employee")
    employee_id_all = [rowdata[0] for rowdata in employee_infos]
    for index, Position_id in enumerate(Position_id_all):
        if Position_id == kwargs['Position_id']:  # 根据id查询到该员工
            post_num = Position_infos[index][4]
            post_already = Position_infos[index][5]
            if post_already >= post_num :
                return False
            else:
                # 1.更改employee表，position表
                update_table_info(db, "position2", 'Post_already', int(post_already)+1, 'Position_id', Position_id)
                for index, employee_id in enumerate(employee_id_all):
                    if employee_id == kwargs['ID']:  # 根据id查询到该员工
                        update_table_info(db, "employee", 'Department_id', kwargs['Department_id'], 'Employee_id', employee_id)
                        update_table_info(db, "employee", 'Position_id', kwargs['Position_id'], 'Employee_id', employee_id)
                        update_table_info(db, "employee", 'State', 1, 'Employee_id', employee_id)

                # 2.若Position_id为总经理的id则更改department表   C1是部门经理
                if kwargs['Position_id']== 'C1':
                    update_table_info(db, "department", 'Manager_id', kwargs['ID'], 'Department_id', kwargs['Department_id'])
                # 3.返回True
                return True


'''
    查询各个岗位的情况
    传入参数：无
    查询position表，
        若position表为空，返回{status:False}
        若不为空，返回position表中所有数据，{status:True,data:[{Position_id,Position_rank,Position_name,Salary,Post_number,Post_already}]}
'''
def getPositionInfo(db):
    # 获取Position_info
    Position_infos = search_table_info(db, "position2")
    if len(Position_infos) == 0:
        return {'status':False}
    else:
        data = []
        for i in range(len(Position_infos)):
            temp ={}
            for j in range(len(Position_infos[i])):
                key = position[j]
                temp[key] = Position_infos[i][j]
            data.append(temp)
        return {'status':True,'data':data}


"""
查询所有员工的信息
传入参数：无
返回数据：{'states':True,data:[]}
data是一个list，里面的每个项是一个字典，代表每一位员工的全部信息（从两个表中获取）
"""
def getAllStaff(db):
    # 获取Position_info
    employee_infos = search_table_info(db, "employee")
    if len(employee_infos) == 0:
        return {'status':False}
    else:
        data = []
        for i in range(len(employee_infos)):
            kw ={}
            kw['ID'] = employee_infos[i][0]
            temp_dic = getUserinfo(db,kw)
            temp = temp_dic['data']
            data.append(temp)
        return {'status':True,'data':data}

"""  
查询已分配员工的信息
传入参数：无
返回数据：{'states':True,data:[]}  data是一个list，里面的每个项是一个字典，代表每一位员工的全部信息（从两个表中获取）
"""
def getAllocated(db):
    # 获取Position_info
    employee_infos = search_table_info(db, "employee")
    if len(employee_infos) == 0:
        return {'status': False}
    else:
        data = []
        for i in range(len(employee_infos)):
            if employee_infos[i][2] == 'G1': continue
            kw = {}
            kw['ID'] = employee_infos[i][0]
            temp_dic = getUserinfo(db, kw)
            temp = temp_dic['data']
            data.append(temp)
        return {'status': True, 'data': data}

"""  
查询未分配员工的信息
传入参数：无
返回数据：{'states':True,data:[]}  data是一个list，里面的每个项是一个字典，代表每一位员工的全部信息（从两个表中获取）
"""
def getUnallocated(db):
    # 获取Position_info
    employee_infos = search_table_info(db, "employee")
    if len(employee_infos) == 0:
        return {'status': False}
    else:
        data = []
        for i in range(len(employee_infos)):
            if employee_infos[i][2] != 'G1': continue
            kw = {}
            kw['ID'] = employee_infos[i][0]
            temp_dic = getUserinfo(db, kw)
            temp = temp_dic['data']
            data.append(temp)
        return {'status': True, 'data': data}

"""
查询某个部门的员工的信息
传入参数：{Department_id}
返回数据：{'states':True,data:[]}
data是一个list，里面的每个项是一个字典，代表每一位员工的全部信息（从两个表中获取）
"""
def getSomeStaff(db, kwargs):
    # 获取Position_info
    employee_infos = search_table_info(db, "employee")
    # 获取Department_info
    department_all_id = [rowdata[1] for rowdata in employee_infos]
    if len(employee_infos) == 0 and kwargs['Department_id'] not in department_all_id:
        return {'status':False}
    else:
        data = []
        for i in range(len(employee_infos)):
            if employee_infos[i][1] != kwargs['Department_id']:
                continue
            temp ={}
            for j in range(len(employee_infos[i])):
                key = employee[j]
                if key == 'Position_id':
                    key = 'Position_name'
                    position_name = id_name(db,'position2',employee_infos[i][j])
                    temp[key] = position_name
                elif key == 'Employee_id':
                    temp[key] = employee_infos[i][j]
                    Employee_name = id_name(db, 'user_info', employee_infos[i][j])
                    temp['Employee_name'] = Employee_name
                elif  key == 'Department_id':
                    key = 'Department_name'
                    department_name = id_name(db,'department',employee_infos[i][j])
                    temp[key] = department_name
                else:
                    temp[key] = employee_infos[i][j]
            data.append(temp)
        return {'status':True,'data':data}

if __name__ == '__main__':
    
    update_table_info(db, "position2","Post_number",1,"Position_id",'B1')


    # """ 注册检验 """
    # # if signUpPermissionTest(db, **{"id":'0001','password':'123'}):
    # #     print("该用户名已存在")

    # # """ 注册 """
    # # if signUp(db, **{"id":"0001","password":"123","sex":"男","name":"冯永祺","Email":"1242387556@qq.com","phone":"15647894231"}):
    # #     print("插入注册数据成功！！")
    # # else:
    # #     print("插入注册数据失败！")
    # #
    # #
    # # """ 登录 """
    # # if login(db, **{"id":'0001','password':'123'}):
    # #     print("登录成功！")

    # """ 获取个人信息 """
    # data = getUserinfo(db,**{"ID":'0009'})
    # print(data)

    # # """ 修改个人信息 """
    # # if updateinfo(db, **{"id":"0001","sex":"男","name":"冯永祺","Email":"1242387556@qq.com","phone":"15647894231"}):
    # #     print("修改数据成功！")
    # # else:
    # #     print("修改数据失败！")

    # """ 录入新员工 """
    # # testdata = {'Sex': '女', 'Name': 'jany', 'Email': 'com', 'Phone': '910', 'Hire_date': '2020/12/19',
    # #  'Work_experience': [{'Work_experience': '已上班5年', 'Achievement': '暂无'}, {'Work_experience': '阿里上班2年', 'Achievement': '暂无'}, {'Work_experience': '摩拜1个月', 'Achievement': '暂无'}]}
    # # if hire(db, **testdata):
    # #     print("录入成功！")
    # # else:
    # #     print("录入失败")



    # # """ 增加部门 """
    # # if addDepartment(db,**{'Department_name':'×部门',',Manager_id':'Null',',Affairs':'管理'}):
    # #     print("增加部门成功！")
    # #
    # # """ 删除部门 """
    # # if deleteDepartment( db, **{"Department_name":"×部门"}):
    # #     print("删除部门成功！")
    # #
    # """ 获取部门信息 """
    # getDepartmentinfo(db)

    # # """ 修改部门信息 """
    # # if updateDepartment(db, **{'Department_id':'1','New_Department_name':'管理部门','New_Manager_id':'0010','New_Affairs':'管理公司日常事务'}):
    # #     print("部门信息修改成功！")

    # """ 调换职位 """
    # if updateStaffStatus(db, **{"Employee_id":'0001','Department_name':'宣传部门','Position_name':'总经理'}):
    #     print("员工职位调整成功！")

    # """ 为员工分配岗位 """
    # # disTribution(db, **{"Employee_id":'0010','Department_name':'管理部门','Position_name':'总经理'})

    # """ 查询各个岗位 """
    # getPositionInfo(db)

    # """ 查询所有员工 """
    # getAllStaff(db)

    # """ 查询某个部门的员工 """
    # getSomeStaff(db, **{'Department_id':'3'})
    # update_table_info(db, "position2","Post_number",3,"Position_id",'A1')
    # update_table_info(db, "position2","Post_number",4,"Position_id",'B1')
    # update_table_info(db, "position2","Post_number",5,"Position_id",'C1')
    # update_table_info(db, "position2","Post_number",6,"Position_id",'D1')
    # update_table_info(db, "position2","Post_number",7,"Position_id",'E1')
    # update_table_info(db, "position2","Post_number",8,"Position_id",'F1')
    # update_table_info(db, "position2","Post_number",0,"Position_id",'G1')

    # update_table_info(db, "position2","Post_already",1,"Position_id",'A1')
    # update_table_info(db, "position2","Post_already",3,"Position_id",'B1')
    # update_table_info(db, "position2","Post_already",3,"Position_id",'C1')
    # update_table_info(db, "position2","Post_already",6,"Position_id",'D1')
    # update_table_info(db, "position2","Post_already",5,"Position_id",'E1')
    # update_table_info(db, "position2","Post_already",3,"Position_id",'F1')
    # update_table_info(db, "position2","Post_already",0,"Position_id",'G1')