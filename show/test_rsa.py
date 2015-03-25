# -*- coding:utf-8 -*-
'''
Created on 2015-03-24

@author: lisong
'''
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

private_key_pem = '/home/lisong/test_rsa.pem'
public_key_pem = '/home/lisong/test_rsa.pem.pub'

public_key = RSA.importKey(open(public_key_pem).read()) 
private_key = RSA.importKey(open(private_key_pem).read())

def sign(content):
    try:
        signer = PKCS1_v1_5.new(private_key)
        signed = signer.sign(SHA.new(content))
        signed = base64.b64encode(signed)
        return signed
    except Exception, e:
        print e
        return None
    
def verify(content, sign):
    try:
        signn = base64.b64decode(sign)
        verifier = PKCS1_v1_5.new(public_key)
        print type(bytes(content))
        if verifier.verify(SHA.new(content), signn): 
            return True
    except Exception, e:
        print e
    return False

if __name__ == '__main__':
    content = 'a=国家翩翩公子的&b=456'
    signx = sign(content)
    print signx
    res = verify(content, signx)
    print res