# -*- coding:utf-8 -*-
'''
Created on 2015-02-06

@author: lisong
'''
apiHost = 'http://192.168.19.244:10003/api/api'
apiHost = 'http://localhost:8888'

from base_test import doRequest

token_186 = '41d79d66bd424709bbd21b38851961c3'
token_185 = 'a62876cc28eb4215b82256a3d04a9a09'

def testApptStatus():
    '''
    查看手艺人预约状态
    '''
    artisan_id = '28000009'
    appt_date = "2015-02-07"
    params =dict(artisan_id=artisan_id,appt_date=appt_date)
    url = '%s/appointment/status' % apiHost
    
    doRequest(url=url, params=params, method='get')
    
# testApptStatus()
def testCreateTrade():
    '''
    创建订单
    @param sample_id: 样品ID
    @param address: 服务地址
    @param appt_date: 预约日期 格式 2000-01-01
    @param appt_hour: 预约时间
    @param remark: 用户备注
    '''
    sample_id = '23'
    address = '火卫23'
    appt_date = "2015-02-6"
    appt_hour = 12
    remark = 'plkj'
    params =dict(sample_id = sample_id,address=address, appt_date = appt_date,
                 appt_hour = appt_hour, remark = remark)
    url = '%s/trade/create' % apiHost
    
    doRequest(url=url, params=params, method='post', token = token_186)
    
# testCreateTrade()

def testOrders():
    '''
    用户订单列表
    @param status: 订单状态（不选为全部）
    @param page: 
    @param page_size: 
    '''
    status = None
    page = None
    page_size = None
    params =dict(status = status, page = page,  page_size = page_size)
    url = '%s/orders' % apiHost
    
    doRequest(url=url, params=params, method='get', token = token_186)
testOrders()
if __name__ == '__main__':
    pass