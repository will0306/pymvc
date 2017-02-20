#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.Kernel.module import Module
from core.Config.config_db import default
from core.Config import config_db
from core.Model.test import test_model
from core.Kernel.log import log
class test_module(Module):
    def __init__(self):
        super(test_module, self).__init__()
        self.name = 'test'
        pass

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
