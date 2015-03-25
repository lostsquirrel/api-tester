# -*- coding:utf-8 -*-
'''
Created on 2014年12月18日

@author: zhuhua
'''
from simpletor import application
from test_rsa import sign, verify

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
        
@application.RequestMapping("/test")
class Tester(application.RequestHandler):
    
    def post(self):
        self.verify()
        
    def verify(self):
        print '--------------------'
        params = self.request.arguments
        print '--------------------'
        
        result = dict()
        if params is None or len(params) <= 0:
            return result
        
        for k, v in params.iteritems():
            if k.lower() == 'sign' or k.lower() == 'sign_type':
                continue
            
            value = ','.join(v)
            if len(value.replace(',', '')) <= 0:
                continue
                
            result[k] = value
        params = result
        
        keys = params.keys()
        keys.sort()
        
        param_str = ''
        for key in keys:
            param_str += '%s=%s&' % (key, params[key])

        length = len(param_str)
        if length > 1:
            param_str = param_str[:len(param_str) - 1]
        
        content = param_str
        print content
        signx = sign(content)
        print signx
        res = verify(content, signx)
        print res