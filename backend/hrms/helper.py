# 用于封装具体的数据库操作

# 所有数据都是用字典格式传入


''' 
    注册检验
    传入参数：{id,password}
    首先查询该id是否已存在于Staff表，
        若不存在，返回False
        若存在，返回True
'''
def signUpPermissionTest(data):
    pass

'''
    注册
    传入参数：{id,password,sex,name,Email,phone}
    在Account表中插入一条记录{id,password}
    在User_info表中插入一条记录{id,sex,name,Email,phone}
        插入成功，返回True
        失败，返回False
'''
def signUp(data):
    pass

'''
    登录
    传入参数：{id,password}
    查询该idpassword是否存在于Account表，
        若存在，返回True
        不存在，返回False
'''
def login(data):
    pass

'''
    获取个人信息
    传入参数：{id}
    查询User_info表和Employee表，将查询的个人信息汇总至一个字典中
        若查到个人信息，返回{status:True,data:{}}，其中data的取值为查询到的个人信息
        若未查找到此人，返回{status:False,data:{}}，其中data为空
'''
def getUserinfo(data):
    pass

'''
    修改个人信息
    传入参数：{id,sex,name,Email,phone}
    在User_info表中根据id查询到该条记录，并根据传入参数进行更新
        若更新成果，返回True
        否则，返回False
'''
def updateinfo(data):
    pass

'''
    员工录用
    传入参数：{id,department,position,Hiredate,State,Work_experience,Achievement}
    为员工分配一个值为id的ID，向Staff表插入一条新纪录
        若分配成功，返回True
        若分配不成功，返回False
'''
def hire(data):
    pass

'''
    增加部门
    传入参数；{Department_name,Manager_id,Affairs}
    首先查询department表
        若department_name已存在，返回False
        若不存在，根据department表中已有记录的数目，分配一个Department_id，
        将{Department_id,Department_name,Manager_id,Affairs}插入department表，返回True
'''
def addDepartment(data):
    pass

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
def deleteDepartment(data):
    pass

'''
    修改部门信息
    传入参数：{Department_name,Manager_id,Affairs}
    根据Department_name查找Department表
        若为找到该部门，返回False
        若找到；
            按照传入信息在Department表中更改该条记录
            若Manager_id发生了改变，则在Employee表中更改涉及到的两位员工的position信息
'''
def updateDepartment(data):
    pass

'''
    部门内员工职位调整
    传入参数：{id,Department_name,position_id}
    首先，按id查找该员工，按Department_name查找该部门
        若未找到该员工或部门，返回False
        若都找到：
            更新员工的position属性值
            若Department_name和该员工原有的Department_name不同，更新其Department_name属性
            若position_id为B1（经理），则调用updateDepartment更新该部门的经理id
            返回True
'''
def updateStaffStatus(data):
    pass