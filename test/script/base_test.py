# -*- coding:utf-8 -*-
import requests
import json
# import sys
# default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
# 	reload(sys)
# 	sys.setdefaultencoding(default_encoding)

class DataWapper(dict):
	__getattr__ = dict.__getitem__
	__setattr__ = dict.__setitem__

def xx (data) :
	print 'Data :' 
	print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
		
def doRequest(url, params, method, dataHandler=xx, token=''):
	'''
	Parameters:
		url  - 请求url
		params - 请求参数
		method - 请求方式 GET/POST
		dataHandler - 处理返回结果的方法
		token - 如果接口需要token则传入，如果不需要则不传
	'''
	headers = dict()
	if len(token) > 0:
		headers['Authorization']='%s' % token
	rep = None
	print headers
	if (method.lower() == 'get') :
		rep = requests.get(url, params=params,headers=headers)
	elif method.lower() == 'post' :
# 		headers['ContentType']="application/x-www-form-urlencoded;charset=utf-8"
		rep = requests.post(url, data=params,headers=headers)
        # requests.
	print rep.url
	
	if rep.status_code == 200:
		# print rep.encoding
		# for x in rep.iter_content():
		# 	print x
		
		dataHandler(rep.json())
# 		if page.status:
# 			if page.data != None:
# 				dataHandler(page.data)
# 			print "Message: %s" % page.messages
# 		else :
# 			print "Error Message: %s" % page.messages
	else :
		print "HTTP STATUS CODE: %s" % rep.status_code
		print rep.content
		# print dir(rep)

	
if __name__ == '__main__':
	pass
	
# 	url = 'http://localhost/api/api/evaluate/addShopReview'
# 	url = 'http://192.168.19.244:10003/api/api/evaluate/addShopReview'
# 	params = dict(orderNo='20140616105135761658',content='python requests authentication token',anonymous=False)
# 	headers = dict(Authorization='Bearer 3c3e390ce9d8062e2ffb69aa0b8b4ab1')
# 	headers = dict()
# 	resp = requests.post(url, data=params, headers=headers)
# 	doRequest(url=url, params=params, method='post', token='Bearer 3c3e390ce9d8062e2ffb69aa0b8b4ab1')
# 	print dir(resp)
# 	print resp.status_code
# 	print resp.text
# 	print resp.content
# 	print resp.urlcategory