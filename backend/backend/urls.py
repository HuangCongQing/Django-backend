'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-08-15 00:26:48
LastEditTime: 2023-08-16 22:49:36
FilePath: /Django-backend/backend/backend/urls.py
'''
"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# 别忘了导入 listorders 函数
from sales.views import listorders, listcustomers
from mgr.customer import dispatcher

urlpatterns = [
    path('admin/', admin.site.urls),

    # 添加如下的路由记录
    path('sales/orders/', listorders),
    path('sales/custmoers/', listcustomers),

    # 请求管理员
    path('/api/mgr/customers', dispatcher)
]
