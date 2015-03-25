# -*- coding:utf-8 -*-
'''
Created on 2015-02-06

@author: lisong
'''
apiHost = 'http://115.28.134.4:8888'
apiHost = 'http://115.28.134.4'
apiHost = 'http://localhost:8888'

from base_test import doRequest
import time
token_186 = '41d79d66bd424709bbd21b38851961c3'
token_185 = 'a62876cc28eb4215b82256a3d04a9a09'
token_x = '038d9fc5e3f147e0a97470b952c9b529'
def testApptStatus():
    '''
    查看手艺人预约状态
    '''
    artisan_id = '28000009'
    appt_date = "2015-02-07"
    params =dict(artisan_id=artisan_id,appt_date=appt_date)
    url = '%s/api/appointment/status' % apiHost
    
    doRequest(url=url, params=params, method='get')
    
def testCreateTrade():
    '''
    创建订单
    @param sample_id: 样品ID
    @param address: 服务地址
    @param appt_date: 预约日期 格式 2000-01-01
    @param appt_hour: 预约时间
    @param remark: 用户备注
    '''
    sample_id = '34'
    address = '火卫34'
    appt_date = "2015-06-12"
    appt_hour = 21
    remark = time.time()
    params =dict(sample_id = sample_id, address=address, appt_date = appt_date,
                 appt_hour = appt_hour, remark = remark)
    url = '%s/api/trade/create' % apiHost
    
    doRequest(url=url, params=params, method='post', token = token_186)
    

def testOrder():
    '''
    用户订单列表
    @param status: 订单状态（不选为全部）
    @param page: 
    @param page_size: 
    '''
    order_no = '1425914744823651'
    with_log = True
    params =dict(order_no = order_no, with_log = with_log)
    url = '%s/api/order' % apiHost
    token = 'f8b765e977a14435994086f592a0ded4'
    doRequest(url=url, params=params, method='get', token = token)
    

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
    

def testUserTrade():
    '''
    用户交易操作 接口：
    @param order_no: 订单号
    @param action: arrived, 用户确认手艺人已经到达; finish, 用户确认交易结束, cancel, 用户取消交易
    @param price: 实际费用（可选）
    '''
    order_nos = (
#     (3,1430061211099479, token_186),
#     (3,1430142354129508, token_186),
    (8,1430056965738700, "f47429f9cc8347a085e9f009022a62bd"),

        )
    for order_no in order_nos:
        action = 'finish'
#         price = 3.14
        price = None
        params =dict(order_no = order_no[1], action = action,  price = price)
        url = '%s/api/user/trade' % apiHost
        doRequest(url=url, params=params, method='post', token = order_no[2])



def testRemoteTrade():
    '''
    支付回调地址（remote）：（怎么保证安全性）
    @param user_id:   用户ID
    @param order_no: 订单号
    '''
    order_nos = (
        (3,1430142354129508),

        )
    for order_no in order_nos:
        user_id = order_no[0]
        params =dict(order_no = order_no[1], user_id = user_id)
        url = '%s/remote/trade' % apiHost
        print doRequest(url=url, params=params, method='post')

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
    testCreateTrade()
#     testOrder()
#     testOrders()
#     testRemoteTrade()
#     testUserTrade()
    # testDeleteOrder()