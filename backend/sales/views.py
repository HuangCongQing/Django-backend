'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-08-15 00:31:44
LastEditTime: 2023-08-16 22:08:38
FilePath: /Django-backend/backend/sales/views.py
'''
from django.shortcuts import render
from django.http import HttpResponse
# 导入 Customer 对象定义
from  common.models import  Customer  # 数据库定义

# Create your views here.

def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")


# 
def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values() # 数据库名字


    # 检查url中是否有参数phonenumber
    ph =  request.GET.get('phonenumber',None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    # 定义返回字符串
    retStr = ''
    for customer in  qs:
        for name,value in customer.items():
            retStr += f'{name} : {value} | '

        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)