#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from core.Kernel.module import Module
from core.Kernel.log import log
log = log('MODULE_LOG','module')

class App:
    params = {}

    def __init__(self):
        pass

    def run_before(self):
        self.getopt()
        pass

    def run(self):
        module = 'core.Module.' + self.params['m']
        module_class = self.params['c'] + '_module'
        module_method = self.params['a']
        self.module = create_object_class(module,module_class)
        self.module.params = self.params
        log.warn("start")
        try:
            func = getattr(self.module,module_method)
            try:
                func()
            except TypeError as ty_e:
                log.error(ty_e)
                pass
        except AttributeError as e:
            log.error(e)
            print(e)
            pass
        log.warn("end")

    def run_after(self):
        pass

    def getopt(self):
        params = sys.argv[1:]
        if len(params) > 0 :
            for i in params :
                p = i.split(":")
                if len(p) > 1 :
                    self.params[p[0][1:]] = p[1]

def create_object_class(module_name, class_name):
    class o: pass
    module_meta = __import__(module_name,{},{},['module']) 
    class_meta = getattr(module_meta, class_name) 
    o = class_meta()
    return o

