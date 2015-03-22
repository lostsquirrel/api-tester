# -*- encoding: utf-8 -*-
'''
Created on 2015-03-12

@author: lisong
'''
apiHost = 'http://192.168.19.244:10003/api/api'
apiHost = 'http://115.28.134.4:8888'
apiHost = 'http://localhost:8888'

from base_test import doRequest
token_186 = '41d79d66bd424709bbd21b38851961c3'
token_185 = 'a62876cc28eb4215b82256a3d04a9a09'
token_x = '0548f185654440138b53f4de467c7010'


def testApptStatus():
    '''
    查看手艺人详情
    '''
    artisan_id = '28000006'
    params =dict()
    url = '%s/api/artisan/%s' % (apiHost, artisan_id)
    
    doRequest(url=url, params=params, method='get')
    
testApptStatus()