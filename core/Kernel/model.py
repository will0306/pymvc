#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.Config import config_db
from core.Kernel.db import mysqlDb
from core.Kernel.log import log
log =  log('MODEL_LOG','Model')
class Model(object):

    db_connect = 'default'
    db = None;
    db_instance = None
    db_cursor = None
    db_table = None


    def __init__(self):
        if hasattr(config_db, self.db_connect):
            config_params = getattr(config_db, self.db_connect)
            if self.db == None :
                self.db = mysqlDb()
            self.db_instance = self.db.db_connect(**config_params)
            self.db_cursor = self.db_instance.cursor()
            log.info(config_params['host'] + ':connect database')
        else:
            log.error("There is no " + db_connect + " db's config ")

    # @query            查询
    # @sql              string          sql语句
    def query(self, sql):
        log.info(sql)
        result = self.execute(sql)
        return self.db_cursor.fetchall()

    '''
    # @select           查询
    # @field            string          字段名
    # @limit            string          条数
    # @where            dict            条件
    # @return           mixed
    def select(self, field, limit = 0, **where):
        if self.db_table == None:
            return None
        sql = 'select ' + field + ' from ' + self.db_table
        where_sql = ''
        limit_sql = ''
        if len(where) >0 :
            where_sql = ' where ' + self.__where(**where)
        if limit > 0 :
            limit_sql = ' limit ' + str(limit);
        self.execute(sql + where_sql + limit_sql)
        print(sql + where_sql + limit_sql)
        return self.db_cursor.fetchall()
    '''
    # @insert           插入
    # @kw               dict            数据列表
    # @return           mixed
    def insert(self, **kw):
        if len(kw) == 0:
            return False
        field_list = []
        value_list = []
        for i in kw :
           field_list.append(i)
           value_list.append(kw[i])
        tag = '%s,' * len(field_list)
        tag = tag[:len(tag) - 1]
        fields = ','.join(field_list)
        values = tuple(value_list)
        sql = 'insert into ' + self.db_table + '(' + fields + ') values(' + tag + ')'
        if getattr(config_db,'debug') and config_db.debug == True:
            log.info(sql)
            log.info(values)
        try :
            self.db_cursor.execute(sql,values)
            return self.db_instance.insert_id()
        except Exception as e:
            print(e)
            return False

    # @insert_many      插入多条
    # @params           list            字段列表
    # @kw               tuple           数据列表
    # @return           mixed
    def insert_many(self,params, *kw):
        if len(kw) == 0 or len(params) == 0:
            return False
        tag = '%s,' * len(params)
        tag = tag[:len(tag) - 1]
        fields = ','.join(params)
        sql = 'insert into ' + self.db_table + '(' + fields + ') values(' + tag + ')'
        try :
            if getattr(config_db,'debug') and config_db.debug == True:
                log.info(sql)
                log.info(kw)
            self.db_cursor.executemany(sql,list(kw))
            return True
        except Exception as e:
            log.error(e)
            log.error(sql)
            log.error(kw)
            return False

    def execute(self, sql):
        try:
            if getattr(config_db,'debug') and config_db.debug == True:
                log.info(sql)
            return self.db_cursor.execute(sql)
        except Exception as e:
            log.error(e)
            return False

    # @transaction              批量执行事务
    # @kw       list            执行的sql语句
    def transaction(self, *kw):
        if len(kw) > 0:
            try:
                self.db_instance.begin()
                for i in kw:
                    self.execute(i)
                    #self.db_cursor.execute(i)
                self.db_instance.commit()
                return True
            except Exception as e:
                log.error(e)
                self.db_instance.rollback()
                return False
    '''
    def update(self, **kw):
        where_params = kw.get('where',None)
        if where_params is None :
             return False
        if len(kw) <= 0 :
            return None
        kw.pop('where')
        field_list = []
        value_list = []
        for i in kw :
            field_list.append(i)
            value_list.append(kw[i])
        fields = ' = %s,'.join(field_list) + ' = %s'
        sql = 'update ' + self.db_table + ' set ' + fields + ' where ' + self.__where(**where_params)
        return self.db_cursor.execute(sql, tuple(value_list))

    def __where(self, **kw):
        if len(kw) > 0:
            list = []
            for i in kw:
                list.append(str(i) + '= "' + str(kw[i]) + '"')
            return ' and '.join(list)
        return None
    '''
    def __del__(self):
        if hasattr(self.db_cursor,'close'):
            self.db_cursor.close()
        if hasattr(self.db_instance,'close'):
            self.db_instance.close()
        print('数据库连接已经关闭')
