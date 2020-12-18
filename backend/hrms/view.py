from django.http import HttpResponse
from django.shortcuts import render
import json
import pymysql
import re
import time
import codecs


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
