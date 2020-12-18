from django.http import HttpResponse
from django.shortcuts import render
import json
import pymysql
import re
import time
import codecs


""" 连接数据库 """
cur = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='humanSource', charset='utf8')
cur.commit()
db = cur  # 数据库

""" head字段 """
Account = ["Name", "Password"]
Staff = ["ID"]
Department = ["Department_id", "Department_name", "Manager_id", "Affairs"]
Position = ["Position_id", "Position_rank", "Position_name", "Salary", "Post_number"]
Employee = ["Employee_id", "Department_id", "Position_id", "Hiredate", "State", "Work_experience", "Achievement"]
user_info = ['id', 'sex', 'name', 'Email', 'phone']


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
    获取个人信息
    传入参数：{id}
    查询Employee表和experience表，将查询的个人信息汇总至一个字典中
        若查到个人信息，返回{status:True,data:{}}，其中data的取值为查询到的个人信息
        若未查找到此人，返回{status:False,data:{}}，其中data为空
'''
def getUserinfo(db,**kwargs):
    # 获取User_info表和Employee表的信息
    user_info_datas = search_table_info(db, "user_info")
    employee_datas = search_table_info(db, "employee")

    account_id_all = [rowdata[0] for rowdata in user_info_datas]  # 得到用户名
    account_id_all2 = [rowdata[0] for rowdata in employee_datas]  # 得到用户名

    if kwargs['id'] in account_id_all and kwargs['id'] in account_id_all2:
        for i in range(len(user_info_datas)):
            account_id = user_info_datas[i][0]  # 得到用户名
            if account_id == kwargs['id']:
                for j in range(len(employee_datas)):
                    account_id2 = employee_datas[j][0]  # 得到用户名
                    if account_id2 == kwargs['id']:
                        data = {}
                        for m in range(len(user_info_datas[i])):
                            if m ==0:continue
                            data[user_info[m]] = user_info_datas[i][m]
                        for n in range(len(employee_datas[j])):
                            if n == 0: continue
                            data[Employee[n]] = employee_datas[i][n]
        return {'status':True,'data':data}
    else:
        return {'status':False,'data':{}}

'''
    修改个人信息
    传入参数：{id,sex,name,Email,phone,Hiredate,Work_experience}
    说明：Work_experience为一个数组
    在User_info表中根据id查询到该条记录，并根据传入参数进行更新
        若更新成果，返回True
        否则，返回False
'''
def updateinfo(db,**kwargs):
    # 获取user_info
    user_infos = search_table_info(db, "user_info")
    account_id_all = [rowdata[0] for rowdata in user_infos]  # 得到用户名
    for index, account_id in enumerate(account_id_all):
        if account_id == kwargs['id']:  # 根据id查询到该条记录
            for i in range(len(user_info)):
                if user_infos[index][i] == kwargs[user_info[i]]:
                    continue
                else:
                    # 修改数据
                    if update_table_info(db, "user_info", user_info[i], str(kwargs[user_info[i]]),'id', str(account_id)):
                        return True
                    else:
                        return False
    return False

'''
    员工录用
    传入参数：{id,sex,name,Email,phone,Hiredate,Work_experience}
    为员工分配一个值为id的ID，向Staff表插入一条新纪录，并将其他信息插入Employee表
        若分配成功，返回True
        若分配不成功，返回False
'''
def hire(db,**kwargs):
    Staff_info = {}
    Employee_info = {}
    for key, value in kwargs.items():
        Employee_info[key] = value
        if key == 'id':
            Staff_info[key] = value
    if insert_alltable_info(db, "staff", **Staff_info) and insert_alltable_info(db, "employee",**Employee_info):  # 插入数据
        return True
    else:
        return False

'''
    为员工分配岗位
    传入参数：{id,Department_name,Position_name}
    查询position表：
        若该职位已达最大人数限制，分配失败，返回False
        若未达最大人数限制，则更改department表和position表和employee表，返回True
'''
def disTribution(data):
    pass

'''
    获取所有部门信息
    传入参数：无
    返回信息：所有部门的信息
        若成功，返回的数据格式：{status:True,data:[]}
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
        info_temp['Department_name'] = department_infos[i][1]
        for j in range(len(user_infos)):
            if user_infos[j][0] == department_infos[i][2]:
                info_temp['Manager'] =  user_infos[j][2]
        info_temp['Affairs'] = department_infos[i][3]
        info.append(info_temp)
    return info

'''
    查询各个岗位的情况
    传入参数：无
    查询position表，
        若position表为空，返回{status:False}
        若不为空，返回position表中所有数据，{status:True,data:[]}
'''
def getPositionInfo():
    pass



'''
    修改部门信息
    传入参数：{Department_id,Department_name,Manager_id,Affairs}
    根据Department_id查找Department表
        若为找到该部门，返回False
        若找到；
            按照传入信息在Department表中更改该条记录
            若Manager_id发生了改变，则在Employee表中更改涉及到的两位员工的position信息
'''
def updateDepartment(db,**kwargs):
    # 获取Department_info
    department_infos = search_table_info(db, "department")
    department_id_all = [rowdata[0] for rowdata in department_infos]

    for index, department_id in enumerate(department_id_all):
        if department_id == kwargs['Department_id']:  # 根据id查询到该条记录
            department_name = department_infos[index][1]
            department_Manageg = department_infos[index][2]
            department_Affairs = department_infos[index][3]
            # 接下来判断是否修改
            if department_name == kwargs['Department_name'] and department_Manageg == kwargs['Manager_id'] and department_Affairs== kwargs['Affairs']:
                return True
            else:
                if update_table_info(db, "department", 'Department_name', kwargs['Department_name'], 'Department_id', department_id) and \
                        update_table_info(db, "department", 'Manager_id', kwargs['Manager_id'], 'Department_id',department_id) and \
                        update_table_info(db, "department", 'Affairs', kwargs['Affairs'], 'Department_id',department_id):
                    return True
                else:
                    return False


'''
    员工职位调整
    传入参数：{employee_id,Department_name,Position_name}
    首先，按id查找该员工，按Department_name查找该部门
        若未找到该员工或部门，返回False
        若都找到：
            更新员工的position属性值
            若Department_name和该员工原有的Department_name不同，更新其Department_name属性
            若position_id为B1（经理），则调用updateDepartment更新该部门的经理id
            返回True
'''
def updateStaffStatus(db,**kwargs):
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
            department_id_new,Position_id_new = 0,0
            # 查询到department和Position的id
            for j in range(len(department_infos)):
                if department_infos[j][1] == kwargs['Department_name']:
                    department_id_new = department_infos[j][0]
            for j in range(len(Position_infos)):
                if Position_infos[j][2] == kwargs['Position_name']:
                    Position_id_new = Position_infos[j][0]
            if department_id_new == 0 or Position_id_new==0:
                return False
            else:
                # 接下来判断是否修改
                if Position_idnow == Position_id_new and department_idnow == department_id_new:
                    return True
                else:
                    if update_table_info(db, "employee", 'Position_id', Position_id_new, 'Employee_id',employee_id ) and \
                        update_table_info(db, "employee", 'Department_id', department_id_new, 'Employee_id',employee_id ):
                        return True
                    else:
                        return False




# ***处理请求部分的函数***

# 注册检验：检查该ID是否已被HR授权
# def signupTest(request):
#     body = getBody(request)
#     # 检验账号是否授权

#     res = json.dumps({
#         'status': True
#     })
#     return HttpResponse(res)

# # 注册函数
# def signup(request):
#     body = getBody(request)
#     res = json.dumps({
#         'status': True
#     })
#     return HttpResponse(res)

# 获取request的body部分携带的信息
def getBody(request):
    return eval(str(request.body, encoding = "utf-8"))

# 登录函数
def login(request):
    body = getBody(request)
    # 检验登录是否能完成
    
    res = json.dumps({
        'status': True
    })
    return HttpResponse(res)

# 

# 获取个人信息
def getUserInfo(request):
    body = getBody(request)
    res = json.dumps({
        'status': True
    })
    return HttpResponse(res)

# 获取公司的部门信息
def getCompanyInfo(request):
    body = getBody(request)
    res = json.dumps({
        'status': True
    })
    return HttpResponse(res)
