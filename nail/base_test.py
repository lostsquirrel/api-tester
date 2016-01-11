# -*- coding:utf-8 -*-
import requests
import json

class DataWapper(dict):
	__getattr__ = dict.__getitem__
	__setattr__ = dict.__setitem__

def xx (data) :
	print 'Data :' 
	print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')).decode('unicode-escape')
		
def doRequest(url, params, method, dataHandler=xx, token='', files = None):
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
		rep = requests.post(url, data=params,headers=headers, files = files)
	print rep.url
	
	if rep.status_code == 200:
		print rep.content
		# dataHandler(rep.json())
	else :
		print "HTTP STATUS CODE: %s" % rep.status_code
		print rep.content.decode('unicode-escape')
	
if __name__ == '__main__':
	pass
