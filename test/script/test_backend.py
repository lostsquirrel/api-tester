# -*- coding:utf-8 -*-
'''
Created on 2015-03-25

@author: lisong
'''

from base_test import doRequest

apiHost = 'http://115.28.134.4:8888'
apiHost = 'http://localhost:8888'
apiHost = 'http://115.28.134.4'
token_186 = '41d79d66bd424709bbd21b38851961c3'
token_185 = 'a62876cc28eb4215b82256a3d04a9a09'
token_x = '70d433cfc2924d7d8bd0670d815759bb'

def test_banner():
    '''
    添加常用地址
    '''
    params =dict()
    url = '%s/api/banners' % apiHost
    doRequest(url=url, params=params, method='get')
    
if __name__ == '__main__':
    test_banner()
    pass