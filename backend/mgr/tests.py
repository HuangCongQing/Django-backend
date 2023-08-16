'''
Description: 测试
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-08-16 22:35:59
LastEditTime: 2023-08-17 02:58:58
FilePath: /Django-backend/backend/mgr/tests.py
'''
from django.test import TestCase

# Create your tests here.

# 测试登陆
import requests, pprint
payload = {
    'username': 'byhy',
    'password': '88888888'
}
response = requests.post('http://localhost/api/mgr/signin',
                         data=payload)
pprint.pprint(response.json())