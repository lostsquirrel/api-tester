# -*- coding:utf-8 -*-
'''
Created on 2015-03-19

@author: lisong
'''
import requests
import json

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
        
test_body()