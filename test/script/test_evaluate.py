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
    x = int(Random().random() * 6) + 3 
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
    communication_rank = random_rank()
    content = '1423536316378362'# get_eva# get_evaluates()luates()
    object_id = 28
    professional_rank = random_rank()
    punctual_rank = random_rank()
    rating = count_rating(communication_rank+professional_rank+punctual_rank)
    order_no = '1423536316378362'
    params =dict(communication_rank=communication_rank,
                 content=content,
                 object_id=object_id,   
                 professional_rank=professional_rank,
                 punctual_rank=punctual_rank,
                 rating=rating,
                 order_no=order_no,
                 )
    files =  [('file', ('foo.png', open('/home/lisong/Pictures/logoquan13963635007.PNG', 'rb'), 'image/png')),
              ('file', ('bar.jpg', open('/home/lisong/Pictures/Funny-Linux-Wallpapers-16.jpg', 'rb'), 'image/jpg'))]
    url = '%s/api/evaluate/add' % apiHost
    
    doRequest(url=url, params=params, method='post', token = token_186, files = files)

test_add()

def get_evaluates():
    
    params =dict(sample_id=28,
             
                 )
    url = '%s/api/evaluates' % apiHost
    
    doRequest(url=url, params=params, method='get')
    
get_evaluates()

if __name__ == '__main__':
    # java -Dsolr.solr.home=/home/lisong/git-repos/python/nail/solr -jar start.jar
    pass
    # get_evaluates()