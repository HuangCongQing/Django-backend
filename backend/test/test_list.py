'''
Description: API https://www.byhy.net/tut/webdev/django/doc_api_v1_0/#%E5%88%97%E5%87%BA%E6%89%80%E6%9C%89%E5%AE%A2%E6%88%B7
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-08-17 03:10:28
LastEditTime: 2023-08-17 03:14:37
FilePath: /Django-backend/backend/test/test_list.py
'''
# 测试登陆
import requests, pprint
params = {
    'action': 'list_customer',
}
response = requests.get('http://localhost:8000/api/mgr/customers',
                         params==params)
pprint.pprint(response.json())



# 测试列表