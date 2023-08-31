'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-08-15 00:26:48
LastEditTime: 2023-09-01 00:53:58
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
from sales.views import listorders, listcustomers # 销售员appname
from mgr.customer import dispatcher # 管理员appname
from mgr.sign_in_out import signin, signout# 管理员appname

# 静态文件服务
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 添加如下的路由记录
    path('sales/orders/', listorders),
    path('sales/custmoers/', listcustomers),

    # 请求管理员
    path('api/mgr/customers', dispatcher), # 一个函数里面增删改查都可

    # 登陆
    path("api/mgr/signin", signin),
    path("api/mgr/signout", signout)
] +  static("/", document_root="./z_dist")
