'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-08-16 00:22:10
LastEditTime: 2023-08-16 01:26:18
FilePath: /Django-backend/backend/common/models.py
'''
from django.db import models

# Create your models here.
class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phonenumber = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)
    
    # QQ
    qq = models.CharField(max_length=200, null=True, blank=True)


from django.contrib import admin
admin.site.register(Customer) # 超级管理管理员可访问此表