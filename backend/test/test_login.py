'''
Description: 测试登陆
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-08-17 03:02:39
LastEditTime: 2023-08-17 03:17:02
FilePath: /Django-backend/backend/test/test_login.py
'''

# 测试登陆
import requests, pprint
payload = {
    'username': 'byhy',
    'password': '88888888'
}
# data不放在链接，params放在链接里面
response = requests.post('http://localhost:8000/api/mgr/signin',
                         data=payload)
pprint.pprint(response.json())