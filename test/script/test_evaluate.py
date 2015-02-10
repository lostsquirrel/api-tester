# -*- coding:utf-8 -*-
'''
Created on 2015-02-10

@author: lisong
'''
apiHost = 'http://localhost:8888'

from base_test import doRequest
from random import Random

token_186 = '41d79d66bd424709bbd21b38851961c3'
token_185 = 'a62876cc28eb4215b82256a3d04a9a09'

def random_rank():
    return int(Random().random() * 6)

def count_rating(total_rank):
    rating = 0
    if total_rank <= 5:
        rating = 2
    if total_rank <=10:
        rating = 1

    return rating

def testAdd():
    communication_rank = random_rank()
    content = 'drgdfg'
    image = (
        '/img/af7762b2aafc3e53077aa0a461b6c7cf.jpg',
        '/img/af7762b2aafc3e53077aa0a461b6c7cf.jpg',
        '/img/af7762b2aafc3e53077aa0a461b6c7cf.jpg')
    object_id = 28
    professional_rank = random_rank()
    punctual_rank = random_rank()
    rating = count_rating(communication_rank+professional_rank+punctual_rank)
    order_no = '1423536311402114'
    params =dict(communication_rank=communication_rank,
                 content=content,
                 image=image,
                 object_id=object_id,
                 professional_rank=professional_rank,
                 punctual_rank=punctual_rank,
                 rating=rating,
                 order_no=order_no,
                 )
    url = '%s/api/evaluate/add' % apiHost
    
    doRequest(url=url, params=params, method='post', token = token_186)

def get_evaluates():
    
    params =dict(sample_id=28,
             
                 )
    url = '%s/api/evaluates' % apiHost
    
    doRequest(url=url, params=params, method='get')
if __name__ == '__main__':
    # java -Dsolr.solr.home=/home/lisong/git-repos/python/nail/solr -jar start.jar
    testAdd() 
    # get_evaluates()