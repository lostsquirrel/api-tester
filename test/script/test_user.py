# -*- coding:utf-8 -*-
'''
Created on 2015-03-18
ALTER TABLE `address`
ADD COLUMN `is_default`  int NOT NULL DEFAULT 0 COMMENT '是否为默认地址' AFTER `create_time`;
@author: lisong
'''
apiHost = 'http://115.28.134.4:8888'
apiHost = 'http://115.28.134.4'
apiHost = 'http://localhost:8888'

from base_test import doRequest

token_186 = '41d79d66bd424709bbd21b38851961c3'
token_185 = 'a62876cc28eb4215b82256a3d04a9a09'
token_x = '70d433cfc2924d7d8bd0670d815759bb'


def test_address():
    '''
    添加常用地址
    '''
    params = dict(location="成都市", detail='北大街333333', is_default=1)
    url = '%s/api/user/address' % apiHost

    doRequest(url=url, params=params, method='post', token=token_x)


def test_default_address():
    '''
   设置默认地址
    '''
    params = dict(address_id=6)
    url = '%s/api/user/address/default' % apiHost

    doRequest(url=url, params=params, method='post', token=token_185)


def test_get_default():
    '''
   设置默认地址
    '''
    params = dict()
    url = '%s/api/user/address/default' % apiHost

    doRequest(url=url, params=params, method='get', token=token_186)


def test_addresses():
    '''
    常用地址列表
    '''
    params = dict()
    url = '%s/api/user/addresses' % apiHost

    doRequest(url=url, params=params, method='get', token=token_186)


def test_checkcode():
    '''
    验证码
    '''
    params = dict(mobile='18583373989')
    url = '%s/api/user/checkcode' % apiHost

    doRequest(url=url, params=params, method='post', token=token_186)


if __name__ == '__main__':
    test_checkcode()
    # test_address()
    # test_default_address()
    # test_get_default()
    # test_addresses()
