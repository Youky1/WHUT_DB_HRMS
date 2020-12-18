import pymysql
import re
import time
import codecs

""" 创建表需要的head字段 """
Account = ["Name","Password"]
Staff = ["ID"]
Department = ["Department_id","Department_name","Manager_id","Affairs"]
Position = ["Position_id", "Position_rank", "Position_name", "Salary", "Post_number"]
Employee = ["Employee_id", "Department_id", "Position_id", "Hiredate", "State", "Work_experience", "Achievement"]
user_info = ['id','sex','name','Email','phone']

'''
实现mysql的操作类
'''
class PyMysql:
    def table_exists(self,cur, table_name):  # 这个函数用来判断表是否存在
        cur.execute( "show tables;")
        tables = [cur.fetchall()]
        table_list = re.findall('(\'.*?\')', str(tables))
        table_list = [re.sub("'", '', each) for each in table_list]
        if table_name in table_list:
            return True  # 存在
        else:
            return False  # 不存在

    # 创建表
    def create_table_head(self, db ,table, head):
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
            if (self.table_exists(cur, table)):
                print(table,"表已经存在")
            else:
                cur.execute(sql)  # 执行命令
                db.commit()  # 一定要进行事务更新
                time.sleep(0.1)
                print(table,'表创建完成')
        except Exception as e:
            print(table,'表创建失败,失败原因', e)

    # 插入数据
    def insert_table_info(self, db,table, info):
        sql = 'insert into {} values ('.format(table)
        for i in range(0, len(info)):
            sql += '"{}" '.format(info[i])
            if i != len(info) - 1:
                sql += ','
        sql += ');'
        try:
            cur = db.cursor()
            if (self.table_exists(cur, table)):
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
    def insert_alltable_info(self, db, table,**kwargs):
        rowdata = []
        for key, value in kwargs.items():
            rowdata.append(str(value))

        """ 先查询数据是否已经存在 """
        searchdata = self.search_table_info(db,table)
        if rowdata in searchdata:
            print("该条数据已存在")
            return False
        else:
            if self.insert_table_info(db, table,rowdata):  # 存储单条数据
                return True
            else:
                return False


    def search_table_info(self,db,table):
        sql = 'SELECT * FROM {}'.format(table)
        try:
            cur = db.cursor()
            if (self.table_exists(cur, table)):
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

    def delete_table_info(self, db, table,table_head,head_value):
        # SQL语句删除数据
        sql = "DELETE FROM {} WHERE {} = '%s'".format(table,table_head) % head_value
        try:
            cur = db.cursor()
            if (self.table_exists(cur, table)):
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

    def update_table_info(self, db, table,table_head1,head_value1,table_head2,head_value2):
        # SQL语句更新数据
        sql = "UPDATE {} SET {}= '%s' WHERE {} = '%s'".format(table,table_head1,table_head2) % (head_value1,head_value2)
        print(sql)
        try:
            cur = db.cursor()
            if (self.table_exists(cur, table)):
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
        注册检验
        传入参数：{id,password}
        首先查询该id是否已存在于Staff表，
            若不存在，返回False
            若存在，返回True
    '''
    def signUpPermissionTest(self,db,**kwargs):
        # 获取已注册用户的账户ID和密码
        account_datas = self.search_table_info(db, "staff")
        account_name = [rowdata[0] for rowdata in account_datas]  # 得到用户名
        if kwargs['id'] in account_name:
            return True
        else:
            return False

    '''
        注册
        传入参数：{id,password,sex,name,Email,phone}
        在Account表中插入一条记录{id,password}
        在User_info表中插入一条记录{id,sex,name,Email,phone}
            插入成功，返回True
            失败，返回False
    '''
    def signUp(self,db,**kwargs):
        account = {}
        User_info = {}
        for key, value in kwargs.items():
            if key == 'id' or key == 'password':
                account[key] = value
            if key == "id" or key == 'sex' or key == 'name' or key == 'Email' or key == 'phone':
                User_info[key] = value
        if self.insert_alltable_info(db, "account", **account) and self.insert_alltable_info(db, "user_info", **User_info):  # 插入数据
            return True
        else:
            return False

    '''
        登录
        传入参数：{id,password}
        查询该idpassword是否存在于Account表，
            若存在，返回True
            不存在，返回False
    '''
    def login(self,db,**kwargs):
        # 获取已注册用户的账户ID和密码
        account_datas = self.search_table_info(db, "account")
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

    '''
        获取个人信息
        传入参数：{id}
        查询User_info表和Employee表，将查询的个人信息汇总至一个字典中
            若查到个人信息，返回{status:True,data:{}}，其中data的取值为查询到的个人信息
            若未查找到此人，返回{status:False,data:{}}，其中data为空
    '''
    def getUserinfo(self,db,**kwargs):
        # 获取User_info表和Employee表的信息
        user_info_datas = self.search_table_info(db, "user_info")
        employee_datas = self.search_table_info(db, "employee")

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
        传入参数：{id,sex,name,Email,phone}
        在User_info表中根据id查询到该条记录，并根据传入参数进行更新
            若更新成果，返回True
            否则，返回False
    '''
    def updateinfo(self,db,**kwargs):
        # 获取user_info
        user_infos = self.search_table_info(db, "user_info")
        account_id_all = [rowdata[0] for rowdata in user_infos]  # 得到用户名
        for index, account_id in enumerate(account_id_all):
            if account_id == kwargs['id']:  # 根据id查询到该条记录
                for i in range(len(user_info)):
                    if user_infos[index][i] == kwargs[user_info[i]]:
                        continue
                    else:
                        # 修改数据
                        if self.update_table_info(db, "user_info", user_info[i], str(kwargs[user_info[i]]),'id', str(account_id)):
                            return True
                        else:
                            return False
        return False

    '''
        员工录用
        传入参数：{Employee_id,Department_id,Position_id,Hiredate,State,Work_experience,Achievement}
        为员工分配一个值为id的ID，向Staff表插入一条新纪录，并将其他信息插入Employee表
            若分配成功，返回True
            若分配不成功，返回False
    '''
    def hire(self,db,**kwargs):
        Staff_info = {}
        Employee_info = {}
        for key, value in kwargs.items():
            Employee_info[key] = value
            if key == 'id':
                Staff_info[key] = value
        if self.insert_alltable_info(db, "staff", **Staff_info) and self.insert_alltable_info(db, "employee",**Employee_info):  # 插入数据
            return True
        else:
            return False

    '''
        增加部门
        传入参数；{Department_name,Manager_id,Affairs}
        首先查询department表
            若department_name已存在，返回False
            若不存在，根据department表中已有记录的数目，分配一个Department_id，
            将{Department_id,Department_name,Manager_id,Affairs}插入department表，返回True
    '''
    def addDepartment(self,db,**kwargs):
        # 获取部门名字
        department_infos = self.search_table_info(db, "department")
        department_name_all = [rowdata[1] for rowdata in department_infos]  # 得到用户名
        if kwargs['Department_name'] in department_name_all:
            return False
        else:
            number = len(department_name_all)
            Department_info = {}
            Department_info['id'] = number+1
            for key, value in kwargs.items():
                Department_info[key] = value
            if self.insert_alltable_info(db, "department", **Department_info):
                return True
            else:
                return False

    '''
        解散部门
        传入参数：{Department_name}
        首先查询department表
            若department_name不存在，返回False
            若存在：
                删除该条记录；
                并在Employee表中按该部门的Manager_id查找用户，将其position改为普通员工；
                返回True
    '''
    def deleteDepartment(self,db,**kwargs):
        # 获取部门表
        department_infos = self.search_table_info(db, "department")
        department_name_all = [rowdata[1] for rowdata in department_infos]

        for index, department_name in enumerate(department_name_all):
            if department_name == kwargs['Department_name']:  # 根据Department_name查询到该条记录

                # 删除数据
                Department_id = kwargs['Department_id']
                if self.delete_table_info(db,'department','Department_name',department_name):
                    # 修改Employee表的信息： 1、找到属于该部门的所有员工
                    employee_infos = self.search_table_info(db, "employee")
                    employee_departmentid_all = [rowdata[1] for rowdata in employee_infos]
                    # employee_posiontionid_all = [rowdata[2] for rowdata in employee_infos]
                    for inde, department_id in enumerate(employee_departmentid_all):
                        if department_id == Department_id:
                            # 2、修改他们的职位为G1
                            if self.update_table_info(db, "employee", 'Position_id','G1', 'Department_id',department_id) and self.update_table_info(db, "employee", 'Department_id',str(0), 'Department_id',department_id):
                                continue
                            else:
                                return False

                    # 修改部门的id
                    for i in range(len(department_name_all)-index-1):
                        if self.update_table_info(db, "department", 'Department_id', str(int(department_infos[index+i][0])-1), 'Department_id',department_infos[index+i][0]):
                            continue
                        else:
                            return False
                    return True
        return False


    '''
        修改部门信息
        传入参数：{Department_id,Department_name,Manager_id,Affairs}
        根据Department_id查找Department表
            若为找到该部门，返回False
            若找到；
                按照传入信息在Department表中更改该条记录
                若Manager_id发生了改变，则在Employee表中更改涉及到的两位员工的position信息
    '''
    # def updateDepartment(self,db,**kwargs):
    #     # 获取Department_info
    #     department_infos = self.search_table_info(db, "department")
    #     department_name_all = [rowdata[1] for rowdata in department_infos]
    #
    #     for index, department_name in enumerate(department_name_all):
    #         if department_name == kwargs['Department_name']:  # 根据name查询到该条记录
    #
    #             for i in range(len(user_info)):
    #                 if user_infos[index][i] == kwargs[user_info[i]]:
    #                     continue
    #                 else:
    #                     # 修改数据
    #                     if self.update_table_info(db, "user_info", user_info[i], str(kwargs[user_info[i]]), 'id',str(account_id)):
    #                         return True
    #                     else:
    #                         return False
    #     return False


    '''
        部门内员工职位调整
        传入参数：{employee_id,Department_name,Position_name}
        首先，按id查找该员工，按Department_name查找该部门
            若未找到该员工或部门，返回False
            若都找到：
                更新员工的position属性值
                若Department_name和该员工原有的Department_name不同，更新其Department_name属性
                若position_id为B1（经理），则调用updateDepartment更新该部门的经理id
                返回True
    '''
    def updateStaffStatus(self,db,**kwargs):
        # 获取员工_info
        employee_infos = self.search_table_info(db, "employee")
        employee_id_all = [rowdata[0] for rowdata in employee_infos]

        for index, employee_id in enumerate(employee_id_all):
            if employee_id == kwargs['employee_id']:  # 根据id查询到该员工
                department_idnow = employee_infos[index][1]
                Position_idnow = employee_infos[index][2]
                if Position_idnow == kwargs['position_id']:
                    continue
                else:
                    if self.update_table_info(db, "employee", 'Position_id', kwargs['position_id'], 'Employee_id',employee_id ):
                        continue
                    else:
                        return False
                # 获取Department_info
                department_infos = self.search_table_info(db,"department")
                if department_infos[department_idnow][1] == kwargs['Department_name']:
                    continue
                else:
                    if self.update_table_info(db, "employee", 'department_id', kwargs['position_id'], 'Employee_id',employee_id ):
                        continue
                    else:
                        return False
        return False


# if __name__ == '__main__':
#     self = PyMysql()

#     """ 连接数据库 """
#     cur = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='humanSource',charset='utf8')
#     cur.commit()
#     db = cur  #数据库



#     """ 注册检验 """
#     if self.signUpPermissionTest(db, **{"id":'0001','password':'123'}):
#         print("该用户名已存在")

#     """ 注册 """
#     if self.signUp(db, **{"id":"0001","password":"123","sex":"男","name":"冯永祺","Email":"1242387556@qq.com","phone":"15647894231"}):
#         print("插入注册数据成功！！")
#     else:
#         print("插入注册数据失败！")


#     """ 登录 """
#     if self.login(db, **{"id":'0001','password':'123'}):
#         print("登录成功！")

#     """ 获取个人信息 """
#     data = self.getUserinfo(db,**{"id":'0123'})
#     print(data)

#     """ 修改个人信息 """
#     if self.updateinfo(db, **{"id":"0001","sex":"男","name":"冯永祺","Email":"1242387556@qq.com","phone":"15647894231"}):
#         print("修改数据成功！")
#     else:
#         print("修改数据失败！")

#     """ 录入新员工 """
#     if self.hire(db, **{'Employee_id':'0003','Department_id':'2','Position_id':'A1','Hiredate':'2020/12/01','State':'1','Work_experience':'已上班5年','Achievement':'98'}):
#         print("录入成功！")
#     else:
#         print("录入失败")

#     """ 增加部门 """
#     if self.addDepartment(db,**{'Department_name':'×部门',',Manager_id':'Null',',Affairs':'管理'}):
#         print("增加部门成功！")

#     """ 删除部门 """
#     if self.deleteDepartment( db, **{"Department_name":"×部门"}):
#         print("删除部门成功！")

#     """ 调换职位 """
#     # self.updateStaffStatus(db, **{"Employee_id":'0010','Department_name':'管理部门','position_id':'B1'})
