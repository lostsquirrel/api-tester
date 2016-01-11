# -*- encoding: utf-8 -*-
'''
Created on 2015-03-19

@author: lisong
'''
apiHost = 'http://115.28.134.4:8888'
apiHost = 'http://115.28.134.4'
apiHost = 'http://localhost:8888'

from base_test import doRequest
import time
token_186 = '41d79d66bd424709bbd21b38851961c3'
token_185 = 'a62876cc28eb4215b82256a3d04a9a09'
token_x = '8582667fad354710a8096876ae5512c4'

def test_wxpay_signture():
    '''
    微信支付签名
    '''
    params =dict(
                 spbill_create_ip='221.3.133.229',
                 order_no='1434117126171844',
                sign_on_server=True
                 )
    url = '%s/api/wxpay/signture' % apiHost
    
    doRequest(url=url, params=params, method='get', token = token_186)
    
test_wxpay_signture()
print time.time()