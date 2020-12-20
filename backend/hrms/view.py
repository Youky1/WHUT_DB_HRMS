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

# 获取个人信息+
def getUserInfo(request):
    body = getBody(request)
    res = json.dumps(getUserinfo(db,kwargs = body))
    print('res is ',res)
    return HttpResponse(res)

# 获取公司的岗位信息
def getWageInfo(request):
    res = json.dumps(getPositionInfo(db))
    print('res is ',res)
    return HttpResponse(res)


#  部门管理接口

# 获取部门信息
def getDepartmentInfo(request):
    res = json.dumps({
        'status': True,
        'data':[{'id':'1','name':'技术部门','managerId':'001','affairs':'技术'},
                {'id':'2','name':'宣传部门','managerId':'002','affairs':'技术'},
                {'id':'3','name':'管理部门','managerId':'003','affairs':'技术'},
                {'id':'4','name':'组织部门','managerId':'004','affairs':'技术'},]
    })
    return HttpResponse(res)

# 更改部门信息
def changeDepartmentInfo(request):
    pass


#  人事管理接口

# 录用员工
def hire(request):
    body = getBody(request)
    res = json.dumps({
        'status':True,
    })
    return HttpResponse(res)

def getAllStaffInfo(request):
    res = json.dumps({
        'status':True,
        'data':[{
            'id':'01',
            'name':'youky',
            'sex':'男',
            'phone':'15623687738',
            'email':'youkyf@qq.com',
            'department':'jsj1803',
            'position':'student',
            'hireDate':'2018.9',
            'experience':[{'description':'小学啊实打实大所大所','grade':90},{'description':'中学','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90}]
        },{
            'id':'02',
            'name':'youky',
            'sex':'男',
            'phone':'15623687738',
            'email':'youkyf@qq.com',
            'department':'jsj1803',
            'position':'student',
            'hireDate':'2018.9',
            'experience':[{'description':'小学','grade':90},{'description':'中学','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90}]
        },{
            'id':'03',
            'name':'youky',
            'sex':'男',
            'phone':'15623687738',
            'email':'youkyf@qq.com',
            'department':'jsj1803',
            'position':'student',
            'hireDate':'2018.9',
            'experience':[{'description':'小学','grade':90},{'description':'中学','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90},{'description':'高中','grade':90}]
        }]
    })
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