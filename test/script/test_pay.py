# -*- coding:utf-8 -*-
'''
Created on 2015-03-19

@author: lisong
'''
import requests
import json

apiHost = 'http://www.mecatmeizhuang.com'
apiHost = 'http://localhost:8888'
def test_body():
    url = '%s/pay_notify/wxpay' % apiHost
    body = '''
    <xml>
   <appid><![CDATA[wx2421b1c4370ec43b]]></appid>
   <attach><![CDATA[支付测试]]></attach>
   <bank_type><![CDATA[CFT]]></bank_type>
   <fee_type><![CDATA[CNY]]></fee_type>
   <is_subscribe><![CDATA[Y]]></is_subscribe>
   <mch_id><![CDATA[10000100]]></mch_id>
   <nonce_str><![CDATA[5d2b6c2a8db53831f7eda20af46e531c]]></nonce_str>
   <openid><![CDATA[oUpF8uMEb4qRXf22hE3X68TekukE]]></openid>
   <out_trade_no><![CDATA[1409811653]]></out_trade_no>
   <result_code><![CDATA[SUCCESS]]></result_code>
   <return_code><![CDATA[SUCCESS]]></return_code>
   <sign><![CDATA[B552ED6B279343CB493C5DD0D78AB241]]></sign>
   <sub_mch_id><![CDATA[10000100]]></sub_mch_id>
   <time_end><![CDATA[20140903131540]]></time_end>
   <total_fee>1</total_fee>
   <trade_type><![CDATA[JSAPI]]></trade_type>
   <transaction_id><![CDATA[1004400740201409030005092168]]></transaction_id>
</xml>
    '''
    rep = requests.post(url, data=body)
    if rep.status_code == 200:
        try:
            data = rep.json()
            json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')).decode('unicode-escape')
        except:
            print rep.content.decode('unicode-escape')
    else :
        print "HTTP STATUS CODE: %s" % rep.status_code
        print rep.content.decode('unicode-escape')
        
def test_body2():
    url = '%s/f/' % apiHost
    body = '''
   <xml><appid><![CDATA[wx267ebd68739af0d3]]></appid>
    <bank_type><![CDATA[CFT]]></bank_type>
    <cash_fee><![CDATA[1]]></cash_fee>
    <fee_type><![CDATA[CNY]]></fee_type>
    <is_subscribe><![CDATA[N]]></is_subscribe>
    <mch_id><![CDATA[1244748802]]></mch_id>
    <nonce_str><![CDATA[ed152cab636d4e7caa045c19dd34d12b]]></nonce_str>
    <openid><![CDATA[o7ZaWuEe6zQ5avgS4m6Nt7nr4o5c]]></openid>
    <out_trade_no><![CDATA[1433424200950475]]></out_trade_no>
    <result_code><![CDATA[SUCCESS]]></result_code>
    <return_code><![CDATA[SUCCESS]]></return_code>
    <sign><![CDATA[7EDBCC9C1669E60D1C424BF6D5C89400]]></sign>
    <time_end><![CDATA[20150604212343]]></time_end>
    <total_fee>1</total_fee>
    <trade_type><![CDATA[APP]]></trade_type>
    <transaction_id><![CDATA[1008330185201506040208952456]]></transaction_id>
    </xml>
    '''.decode('utf-8')
    rep = requests.post(url, data=body)
    if rep.status_code == 200:
        try:
            data = rep.json()
            json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')).decode('unicode-escape')
        except:
            print rep.content.decode('unicode-escape')
    else :
        print "HTTP STATUS CODE: %s" % rep.status_code
        print rep.content.decode('unicode-escape')
        
def test_alipay_notify():
    url = '%s/pay_notify/alipay' % apiHost
#     url = 'http://localhost:8080/pay/notify_url.jsp'
#     url = 'http://localhost:9999/test'
    params = {'seller_email': ['329005952@qq.com'], 'sign': ['phwWlhdrAP2WiSHb4r1imM7SwY+3tZP/BRfztujogm4ThGyrLjM4EGcMBJ8+rPUXwZ6nLJVq2gLCNqMq9hEkFzstcjcUqDP+znzszfxiuUlhrTOJqDU23Jy/HaOvXa8EkkqhwlbLQlL8FJTIMyBDQ9zEnZeE/E/8BLpdrk80PqU='], 'subject': ['\xe7\xbe\x8e\xe7\x9d\xab\xe4\xba\xa7\xe5\x93\x81001'], 'is_total_fee_adjust': ['N'], 'gmt_create': ['2015-03-23 17:05:07'], 'out_trade_no': ['1427101485118137'], 'sign_type': ['RSA'], 'body': ['\xe7\xbe\x8e\xe7\x9d\xab\xe4\xba\xa7\xe5\x93\x81001'], 'price': ['0.01'], 'buyer_email': ['tang.ke@me.com'], 'discount': ['0.00'], 'trade_status': ['TRADE_SUCCESS'], 'gmt_payment': ['2015-03-23 17:05:08'], 'trade_no': ['2015032300001000170047235055'], 'seller_id': ['2088812906941947'], 'use_coupon': ['N'], 'payment_type': ['1'], 'total_fee': ['0.01'], 'notify_time': ['2015-03-23 17:19:26'], 'quantity': ['1'], 'notify_id': ['3c07ebe0825cb232ffabb95a8c46d1d92y'], 'notify_type': ['trade_status_sync'], 'buyer_id': ['2088002033090175']}
    rep = requests.post(url, data=params)
    if rep.status_code == 200:
        try:
            data = rep.json()
            json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')).decode('unicode-escape')
        except:
            print rep.content.decode('unicode-escape')
    else :
        print "HTTP STATUS CODE: %s" % rep.status_code
        print rep.content.decode('unicode-escape')
        
if __name__ == '__main__':
#     test_alipay_notify()
    pass
# test_body()
    test_body2()