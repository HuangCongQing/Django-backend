'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-08-15 00:31:44
LastEditTime: 2023-08-15 00:32:37
FilePath: /Django-backend/backend/sales/views.py
'''
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")