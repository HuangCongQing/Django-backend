<!--
 * @Description: 
 * @Author: HCQ
 * @Company(School): UCAS
 * @Email: 1756260160@qq.com
 * @Date: 2023-08-14 22:29:39
 * @LastEditTime: 2023-09-01 00:56:59
 * @FilePath: /Django-backend/README.md
-->
# Django-backend
Django web服务端(后端)开发学习

* Docs： https://www.yuque.com/huangzhongqing/gyafdp/swbheg2peprxn5yr



## 安装
```shell
# 安装
pip install django==3.2.19

# 查看版本
python -m django --version
```

## 安装
```shell

# 1 创建工程
django-admin startproject backend(工程名)


# 2 创建项目app
## 我们就进入项目根目录，执行下面的命令。
python manage.py startapp sales(appname)

```

## 运行
```shell
# 创建数据库& 同步数据库
python manage.py migrate

# 启动
python manage.py runserver 0.0.0.0:8000
python manage.py runserver 127.0.0.1:8000
```

## demo1
* video: https://www.bilibili.com/video/BV1AE41117Up/
* docs: https://www.yuque.com/huangzhongqing/gyafdp/qa49l7eq128x35ov

```shell

# 1 创建工程
django-admin startproject backend(工程名)


# 2 创建项目app
## 我们就进入项目根目录，执行下面的命令。
python manage.py startapp sales(appname) # 销售员
python manage.py startapp mgr(appname) # 管理员

```

### 测试API代码
* [backend/test](backend/test)