# -*- encoding: utf-8 -*-
'''
Created on 2015-03-12

@author: lisong
'''
apiHost = 'http://115.28.134.4:8888'
apiHost = 'http://115.28.134.4'
apiHost = 'http://localhost:8888'
apiHost = 'http://115.28.134.4'

from base_test import doRequest
token_186 = '41d79d66bd424709bbd21b38851961c3'
token_185 = 'a62876cc28eb4215b82256a3d04a9a09'
token_x = '99de5b9fbc2947b6a1de1557ba84d9c3'


def testApptStatus():
    '''
    查看手艺人详情
    '''
    artisan_id = '28000006'
    params =dict()
    url = '%s/api/artisan/%s' % (apiHost, artisan_id)
    
    doRequest(url=url, params=params, method='get')
    
<<<<<<< HEAD
def test_mecat():
    '''
    我的大咖
=======
def test_my_artisan():
    '''
    查看手艺人详情
>>>>>>> c8c43509cb2c3336cea3c2b9f223cd68d4d6bf1e
    '''
    params =dict()
    url = '%s/api/my_mecat' % (apiHost)
    
<<<<<<< HEAD
    doRequest(url=url, params=params, method='get', token=token_185)
    
def test_my_artisans():
    params =dict()
    url = '%s/api/artisans' % (apiHost)
    
    doRequest(url=url, params=params, method='get', token='')
    
def test_remove_mecat():
    params =dict(artisan_id=28000006)
    url = '%s/api/my_mecat/delete' % (apiHost)
    
    doRequest(url=url, params=params, method='post', token=token_185)
    
# testApptStatus()
test_mecat()
# test_remove_mecat()
# test_my_artisans()
=======
    doRequest(url=url, params=params, method='get', token='db5fd4825b7944f29fa39d5922a3a5e9')
    
    
# testApptStatus()
test_my_artisan()
>>>>>>> c8c43509cb2c3336cea3c2b9f223cd68d4d6bf1e
