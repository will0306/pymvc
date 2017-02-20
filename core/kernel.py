#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.Kernel.module import Module
from core.Kernel.app import App

class Kernel:
    def __init__(self):
        self.name = "kernel"
        self.app = App()
    
    def work(self):
        self.app.run_before()
        self.app.run()
        self.app.run_after()
