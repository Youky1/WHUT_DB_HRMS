from django.http import HttpResponse
from django.shortcuts import render
import json
from . import helper

# 获取request的body部分携带的信息
def getBody(request):
    return eval(str(request.body, encoding = "utf-8"))

def getTest(request):
    if(request.method == 'GET'):
        data = json.dumps({
            'name':'youky',
            'age':'21'
        })
        return HttpResponse(data)

def postTest(request):
    if(request.method == 'POST'):
        data = json.dumps({
            'status': 'OK',
            'data': 'post test successfully'
        })
        return HttpResponse(data)

# 登录函数
def login(request):
    body = getBody(request)
    # 检验登录是否能完成
    
    res = json.dumps({
        'status': True
    })
    return HttpResponse(res)

# 注册检验：检查该ID是否已被HR授权
def signupTest(request):
    body = getBody(request)
    # 检验账号是否授权

    res = json.dumps({
        'status': True
    })
    return HttpResponse(res)

# 注册函数
def signup(request):
    body = getBody(request)
    res = json.dumps({
        'status': True
    })
    return HttpResponse(res)




