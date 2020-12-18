from django.http import HttpResponse
from django.shortcuts import render
import json
import pymysql
import re
import time
import codecs

# 获取request的body部分携带的信息
def getBody(request):
    return json.loads(eval(str(request.body, encoding = "utf-8")))

# 登录函数
def login(request):
    body = getBody(request)
    # 检验登录是否能完成
    if(body['id'] == 'root' and body['password'] == '123456'):
        res = json.dumps({
            'status': True
        })
    else:
        res = json.dumps({
            'status': False
        })
    return HttpResponse(res)

# 获取个人信息
def getUserInfo(request):
    body = getBody(request)
    res = json.dumps({
        'status': True,
        'data':{
            'name':'success'
        }
    })
    return HttpResponse(res)

# 获取公司的部门信息
def getWageInfo(request):
    body = getBody(request)
    res = json.dumps({
        'status': True
    })
    return HttpResponse(res)

# 获取部门信息
def getDepartmentInfo(request):
    pass

# 更改部门信息
def changeDepartmentInfo(request):
    pass

# 录用员工
def hire(request):
    pass

# 为员工分配岗位
def distribution(request):
    pass

# 调整员工的岗位
def manage(request):
    pass