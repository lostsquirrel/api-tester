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
token_x = '8582667fad354710a8096876ae5512c4'

def test_get_sample():
    '''
    添加收藏
    '''
    params =dict(
               
                 )
    url = '%s/api/sample/%s' % (apiHost, 35)
    
    doRequest(url=url, params=params, method='get')
    
def test_get_samples():
    '''
    添加收藏
    '''
    params =dict(
                artisan_id = 28000006,
                category_id = 1,
                order_by='create_time',
#                 id = 35,
                page = 1,
                page_size = 20
                 )
    url = '%s/api/samples' % (apiHost)
    
    doRequest(url=url, params=params, method='get')
    
# test_get_sample()
test_get_samples()
print time.time()