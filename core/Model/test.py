#!-*- encoding: utf8 -*-
from core.Kernel.model import Model
class test_model(Model):

    def __init__(self):
        super(test_model,self).__init__()
        self.db_table = 't1'

    def test(self):
        print(123)

