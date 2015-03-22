# -*- coding:utf-8 -*-
'''
Created on 2015-02-06

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
def testApptStatus():
    '''
    查看手艺人预约状态
    '''
    artisan_id = '28000009'
    appt_date = "2015-02-07"
    params =dict(artisan_id=artisan_id,appt_date=appt_date)
    url = '%s/api/appointment/status' % apiHost
    
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
    sample_id = '31'
    address = '火卫31'
    appt_date = "2015-03-23"
    appt_hour = 14
    remark = time.time()
    params =dict(sample_id = sample_id, address=address, appt_date = appt_date,
                 appt_hour = appt_hour, remark = remark)
    url = '%s/api/trade/create' % apiHost
    
    doRequest(url=url, params=params, method='post', token = token_185)
    
# testCreateTrade()

def testOrder():
    '''
    用户订单列表
    @param status: 订单状态（不选为全部）
    @param page: 
    @param page_size: 
    '''
    order_no = '1425868441183706'
    with_log = True
    params =dict(order_no = order_no, with_log = with_log)
    url = '%s/api/order' % apiHost
    
    doRequest(url=url, params=params, method='get', token = token_x)
    
# testOrder()

def testOrders():
    '''
    用户订单列表
    @param status: 订单状态（不选为全部）
    @param page: 
    @param page_size: 
    '''
    status = 'unfinished'
    status = 'other'
    status = 'finished'
    status = 'wait_pay'
    page = None
    page_size = None
    params =dict(status = status, page = page,  page_size = page_size)
    url = '%s/api/orders' % apiHost
    
    doRequest(url=url, params=params, method='get', token = token_186)
    
# testOrders()

def testUserTrade():
    '''
    用户交易操作 接口：
    @param order_no: 订单号
    @param action: arrived, 用户确认手艺人已经到达; finish, 用户确认交易结束, cancel, 用户取消交易
    @param price: 实际费用（可选）
    '''
    order_nos = (
      (3,1426929219882431, '38e24253ff6e49bfb798f153ee596eba'),

        )
    for order_no in order_nos:
        action = 'arrived'
        price = 3.14
        price = None
        params =dict(order_no = order_no[1], action = action,  price = price)
        url = '%s/api/user/trade' % apiHost
        doRequest(url=url, params=params, method='post', token = order_no[2])

testUserTrade()

def testRemoteTrade():
    '''
    支付回调地址（remote）：（怎么保证安全性）
    @param user_id:   用户ID
    @param order_no: 订单号
    '''
    order_nos = (
        (3,1426929219882431),

        )
    for order_no in order_nos:
        user_id = order_no[0]
        params =dict(order_no = order_no[1], user_id = user_id)
        url = '%s/remote/trade' % apiHost
        print doRequest(url=url, params=params, method='post')
# testRemoteTrade()

def testDeleteOrder():
    
    order_ids = (
        '1',
        )
    for order_id in order_ids:
        user_id = '4'
        params =dict(order_id = order_id)
        url = '%s/api/order/delete' % apiHost
        doRequest(url=url, params=params, method='post', token = token_186)
        
if __name__ == '__main__':
    pass
    # testApptStatus()
#     testCreateTrade()
#     testOrders()
    # testRemoteTrade()
    # testUserTrade()
    # testDeleteOrder()