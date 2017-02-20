#!/usr/bin/env python
#!-*- encoding:utf-8 -*-
import pymysql,hashlib
from core.Kernel.log import log
log =  log('MODEL_LOG','model')

class mysqlDb(object):

    db = None;
    cursor = None;

    def db_connect(self, **kw):
        try:
            return pymysql.connect(host=kw.get('host'),port=kw.get('port'),user=kw.get('user'),password=kw.get('password'),db=kw.get('db'),charset=kw.get('charset','utf8'),autocommit=kw.get('autocommit',True))
        except Exception as e:
            log.error(e)
            return False

