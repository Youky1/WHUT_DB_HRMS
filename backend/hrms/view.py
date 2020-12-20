from django.http import HttpResponse
from django.shortcuts import render
import json
from .sql_operator import *


# 获取request的body部分携带的信息
def getBody(request):
    return json.loads(eval(str(request.body, encoding = "utf-8")))

# 登录函数
def login(request):
    body = getBody(request)
    # 检验登录是否能完成
    if(body['password'] == '123456'):
        res = json.dumps({
            'status': True
        })
    else:
        res = json.dumps({
            'status': False
        })
    return HttpResponse(res)

# 信息查询接口

# 获取个人信息
def getUserInfo(request):
    body = getBody(request)
    res = json.dumps(getUserinfo(db,kwargs = body))
    print('res is ',res)
    return HttpResponse(res)

# 获取公司的岗位信息
def getWageInfo(request):
    res = json.dumps(getPositionInfo(db))
    print('\nwage info is',res)
    print('res is ',res)
    return HttpResponse(res)


#  部门管理接口


# 获取部门信息
def getDepartmentInfo(request):
    res = json.dumps(getDepartmentinfo(db))
    print('departmentInfo is',res)
    return HttpResponse(res)

# 获取某个部门的全部员工
def getStaffByDepartment(request):
    body = getBody(request)
    res = json.dumps(getSomeStaff(db,{'Department_id':body['department_id']}))
    print('staff in this department is ',res)
    return HttpResponse(res)

# 更改部门信息
def changeDepartmentInfo(request):
    body = getBody(request)
    print(body)
    status = updateDepartment(db,body)
    res = json.dumps({
        'status':status
    })
    return HttpResponse(res)


#  人事管理接口

# 录用员工
def hire(request):
    body = getBody(request)
    res = json.dumps({
        'status':True,
    })
    return HttpResponse(res)

def getAllStaffInfo(request):
    res = json.dumps(getAllStaff(db))
    print('\nstaff info is ',res)
    return HttpResponse(res)

# 为员工分配岗位
def distribution(request):
    res = json.dumps({
        'status': True,
    })
    return HttpResponse(res)

# 调整员工的岗位
def manage(request):
    pass