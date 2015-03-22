# -*- coding:utf-8 -*-
'''
Created on 2015-02-10

@author: lisong
'''
apiHost = 'http://115.28.134.4'
apiHost = 'http://localhost:8888'

from base_test import doRequest
from random import Random

token_186 = '41d79d66bd424709bbd21b38851961c3'
token_185 = 'a62876cc28eb4215b82256a3d04a9a09'

def random_rank():
    x = int(Random().random() * 6) 
    if x > 5:
        x = 5
    return x

def count_rating(total_rank):
    rating = 0
    if total_rank <= 5:
        rating = 2
    if total_rank <=10:
        rating = 1

    return rating

def test_add():
    
    order_nos = (

        (4,1426921372398030, 31, token_185),
        )
    for order_no in order_nos:
        communication_rank = random_rank()
        content = order_no[0]
        object_id = order_no[2]
        professional_rank = random_rank()
        punctual_rank = random_rank()
        rating = count_rating(communication_rank+professional_rank+punctual_rank)
        
        params =dict(communication_rank=communication_rank,
                     content=content,
                     object_id=object_id,   
                     professional_rank=professional_rank,
                     punctual_rank=punctual_rank,
                     rating=rating,
                     order_no=order_no[1],
                     )
        files =  [('file', ('foo.jpg', open('/home/lisong/Pictures/th.jpeg', 'rb'), 'image/jpeg')),
                  ('file', ('bar.jpg', open('/home/lisong/Pictures/%s.jpeg' % str(order_no[1] % 9), 'rb'), 'image/jpg'))]
        url = '%s/api/evaluate/add' % apiHost
        
        doRequest(url=url, params=params, method='post', token = order_no[3], files = files)

# test_add()


def test_edit():
    
    order_nos = (

        (3,1426087758781223, 28, token_186),
        )
    for order_no in order_nos:
        communication_rank = random_rank()
        content = u'你从哪里来'.encode('utf-8')
        professional_rank = random_rank()
        punctual_rank = random_rank()
        rating = count_rating(communication_rank+professional_rank+punctual_rank)
        
        params =dict(communication_rank=communication_rank,
                     content='update%s' % content,
                     professional_rank=professional_rank,
                     punctual_rank=punctual_rank,
                     rating=rating,
                     order_no=order_no[1],
                     )
        files =  [('file', ('foo.jpg', open('/home/lisong/Pictures/th.jpeg', 'rb'), 'image/jpeg')),
                  ('file', ('bar.jpg', open('/home/lisong/Pictures/%s.jpeg' % str(order_no[1] % 7), 'rb'), 'image/jpg'))]
        url = '%s/api/evaluate/edit' % apiHost
        
        doRequest(url=url, params=params, method='post', token = order_no[3], files = files)
        
test_edit()

def get_evaluates():
    
    params =dict(sample_id=28,
             
                 )
    url = '%s/api/evaluates' % apiHost
    
    doRequest(url=url, params=params, method='get')
    
# get_evaluates()

if __name__ == '__main__':
    # java -Dsolr.solr.home=/home/lisong/git-repos/python/nail/solr -jar start.jar
    pass
    # get_evaluates()