# -*- encoding: utf-8 -*-
'''
Created on 2015-03-20

@author: lisong
'''
apiHost = 'http://115.28.134.4:8888'
apiHost = 'http://localhost:8888'
apiHost = 'http://115.28.134.4'

from base_test import doRequest
import time
token_186 = '41d79d66bd424709bbd21b38851961c3'
token_185 = 'a62876cc28eb4215b82256a3d04a9a09'
token_x = '70d433cfc2924d7d8bd0670d815759bb'

def test_add_fav():
    '''
    添加收藏
    '''
    params =dict(
                 type='2',
                 object_id=7
                 )
    url = '%s/api/user/favorite' % apiHost
    
    doRequest(url=url, params=params, method='post', token = token_x)


def test_del_fav():
    '''
    添加收藏
    '''
    params =dict(
                 type='2',
                 object_id=19
                 )
    url = '%s/api/user/favorite/delete' % apiHost
    
    doRequest(url=url, params=params, method='post', token = token_186)
    
test_del_fav()

def test_get_fav():
    '''
    添加收藏
    '''
    params =dict(
                 type='2',
                 page=1,
                 page_size = 10
                 )
    url = '%s/api/user/favorites' % apiHost
    
    doRequest(url=url, params=params, method='get', token = token_186)
if __name__ == '__main__':
    pass
    test_add_fav()
# test_get_fav()