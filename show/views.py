# -*- coding:utf-8 -*-
'''
Created on 2014年12月18日

@author: zhuhua
'''
from simpletor import application


#######  USER ##################################
@application.RequestMapping("/base")
class Register(application.RequestHandler):
    '''注册'''
    def get(self):
        
        self.render("base.html", model="abc", worder="worker_a.js")
    def post(self):
        mobile = self.get_argument('mobile', strip=True)
        password = self.get_argument('password', strip=True)
        checkcode = self.get_argument('checkcode', strip=True)
        
        if not checkcode == '111111':
            raise application.AppError('验证码错误')
        
