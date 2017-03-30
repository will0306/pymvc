#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd, xlwt

def decorator(**kw):
    def _deco(func):
        def __deco(self):
            if self.tables == None:
                return False
            return func(self,**kw)
        return __deco
    return _deco

class xls:

    instance = None
    worker = None
    tables = None
    table = None
    index = 0

    def __init__(self, **kw):
        self.worker = xlwt.Workbook()
        pass

    def read(self, filename):
        self.instance = xlrd.open_workbook(filename)
        self.tables = self.instance.sheets()
        return self

    def set_default_table(self, sheet_num = 0):
        if self.tables == None:
            return False
        if len(self.tables) <= sheet_num:
            return False
        self.table = self.tables[sheet_num]
        self.index = 0
        return True

    @decorator()
    def get_count_table(self):
        return len(self.tables)

    def get_count_line(self, sheet_num = 0):
        if self.tables == None:
            return False
        if len(self.tables) <= sheet_num:
            return False
        return self.tables[sheet_num].nrows

    @decorator()
    def get_row(self):
        if self.table == None:
            self.table = self.tables[0]
        if self.table.nrows <= self.index :
            return False
        index = self.index
        self.index = self.index + 1
        return self.table.row_values(index)

    def add_sheet(self, sheet_name):
        try:
           setattr(self,sheet_name,self.worker.add_sheet(sheet_name,cell_overwrite_ok=True))
           return True
        except Exception as e:
            print(e)
            return False



    def save(self, filename):
        self.worker.save(filename)
        pass

if __name__ == "__main__":
    xls_i  = xls()
    xls_i.add_sheet('test')
    xls_i.test.write(0,0,123)
    xls_i.test.write(1,1,123)
    xls_i.add_sheet('test1')
    print(xls_i.save('test.xls'))
    '''
    #读取
    xls_i.read('t.xlsx')
    for i in range(xls_i.get_count_line()):
        print(xls_i.get_row())
    xls_i.set_default_table(1)
    for i in range(xls_i.get_count_line()):
        print(xls_i.get_row())
    '''
