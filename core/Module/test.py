#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.Kernel.module import Module
from core.Config.config_db import default
from core.Config import config_db
from core.Model.test.test import test_model
from core.Kernel.log import log
from core.ext.http_ext import http_client
from core.ext.xls import xls
from core.ext import email_ext as em


def decorator(**args):
    def _deco(func):
        def __deco(self):
            print("装饰器")
            self.i = args
            func(self)
            print("装饰器")
        return __deco
    return _deco

class test_module(Module):
    def __init__(self):
        super(test_module, self).__init__()
        self.name = 'test'
        pass

    @decorator()
    def test(self):
        t = test_model()
        if hasattr(config_db,'default') :
            print('test')
        else :
            print(123)
        #print(t.insert(t1=1,t2=10,title='bbq'))
        #print(t.insert_many(['t1','t2','title'],(1,2,'title1'),(2,3,'title2')))
        #print(t.select('*',id=7,title="mini",limit=1))
        #print(t.update(t1=2,t2=1,where={'id':7,'title':'mini'}))
        print('end')


    def test_http(self):
        http_client_instance = http_client(host='192.168.33.11');
        #data = http_client_instance.post('/api.php',name="linyue",age=26)
        data = http_client_instance.get('/api.php?name=linyue')
        print(data)


    def test_xls(self):
        xls_i = xls()
        xls_i.add_sheet('test')
        xls_i.test.write(0,0,123)
        xls_i.test.write(1,1,123)
        xls_i.add_sheet('test1')
        print(xls_i.save('/tmp/test1.xls'))

    def test_email(self):
        em.from_addr = 'XXXX@qq.com'
        em.subject = 'this is a test email'
        em.password = 'XXXXX'
        em.to_addr = ['XXXX@qq.com', 'XXXX@qq.com']
        em.smtp_server = 'smtp.qq.com'
        #em.set_attach({'/tmp/t.csv':'','/tmp/t.xlsx':'','/tmp/t':''})
        em.send_email()
