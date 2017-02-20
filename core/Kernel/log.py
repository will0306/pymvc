#!/usr/bin/env python2.7  
# -*- coding:utf-8 -*-  
import logging, logging.handlers, logging.config
from core.Config import config_log as C

class log:  
    def __init__ (self, config, name):
        try:
            conf = getattr(C, config)
            self.LOG_INFO = logging.getLogger(name+'_info')
            self.LOG_INFO.setLevel(logging.DEBUG) 
            self.LOG_WARN = logging.getLogger(name+'_warn')
            self.LOG_WARN.setLevel(logging.INFO)
            self.LOG_ERROR = logging.getLogger(name+'_error')
            self.LOG_ERROR.setLevel(logging.WARN)
            self.LOG_CONSOLE = logging.getLogger(name+'_console')
            self.LOG_CONSOLE.setLevel(logging.DEBUG)
            info_hander = logging.handlers.RotatingFileHandler(conf['filename'],"a", 0, 1)
            ch = logging.StreamHandler()
            if 'info' in conf and 'filename' in conf['info']:
                info_hander = logging.handlers.RotatingFileHandler(conf['info']['filename'],"a", 0, 1)
            info_hander.setFormatter(logging.Formatter(conf['format']) )  
            ch.setFormatter(logging.Formatter(conf['format']))
            self.LOG_INFO.addHandler(info_hander)
            self.LOG_INFO.addHandler(ch)

            error_hander = logging.handlers.RotatingFileHandler(conf['filename'],"a", 0, 1)
            if 'error' in conf and 'filename' in conf['error']:
                error_hander = logging.handlers.RotatingFileHandler(conf['error']['filename'],"a", 0, 1)
            error_hander.setFormatter(logging.Formatter(conf['format']) )  
            self.LOG_ERROR.addHandler(error_hander)
            self.LOG_ERROR.addHandler(ch)

            warn_hander = logging.handlers.RotatingFileHandler(conf['filename'],"a", 0, 1)
            if 'warn' in conf and 'filename' in conf['warn']:
                warn_hander = logging.handlers.RotatingFileHandler(conf['warn']['filename'],"a", 0, 1)
            warn_hander.setFormatter(logging.Formatter(conf['format']) )
            self.LOG_WARN.addHandler(warn_hander)
            self.LOG_WARN.addHandler(ch)

        except Exception as e:
            print(e)

    def error(self, msg):
        if self.LOG_ERROR is not None:
            self.LOG_ERROR.error(msg)

    def info(self, msg):
        if self.LOG_INFO is not None:
            self.LOG_INFO.info(msg)

    def warn(self, msg):
        if self.LOG_WARN is not None:
            self.LOG_WARN.warn(msg)

