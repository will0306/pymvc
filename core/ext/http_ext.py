#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import httplib,urllib,json

class http_client:

    client = None
    response = None
    headers = None

    def __init__(self, **kw):
        if len(kw) == 0:
            return False
        if 'host' not in kw:
            print("http_client 缺少host")
            return False
        host = kw['host']
        port = kw.get('port',80)
        timeout = kw.get('timeout',30)

        try:
            self.client = httplib.HTTPConnection(host, port, timeout)
        except Exception, e:
            print e
        finally:
            if self.client:
                self.client.close()

    
    def post(self,api,**kw):
        try:
            params = urllib.urlencode(kw)
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                     
            self.client.request("POST", api, params, headers)
                 
            self.response = self.client.getresponse()

            data = json.loads(self.response.read())
            data['status'] = self.response.status
            data['reason'] = self.response.reason
            return data
        except Exception, e:
            print e
        finally:
            if self.client:
                self.client.close()
    
    def get(self,api):
        try:
            self.client.request('GET', api)
            
            #response是HTTPResponse对象
            self.response = self.client.getresponse()
            data = json.loads(self.response.read())
            data['status'] = self.response.status
            data['reason'] = self.response.reason
            return data
        except Exception, e:
            print e
        finally:
            if self.client:
                self.client.close()

    def __del__(self):
        if self.client:
            self.client.close()
