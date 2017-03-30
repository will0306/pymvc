#!/usr/bin/env python
# -*- encoding: utf8 -*-
import paramiko

user = password = port = server = None

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connect():
    global ssh, user, password, port, server
    if user == None or user == '':
        print('缺少用户名')
        return False
    if password == None :
        print('缺少密码')
        return False
    if server == None :
        print('缺少要链接的服务器ip')
        return False
    if port == None:
        port = 22
    try:
        ssh.connect(server, int(port), user, password)
        return True
    except Exception, e:
        print str(e)
        ssh.close()
        return False

def exec_cmd(cmd):
    if cmd == '':
        return ''
    try:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        return stdout.read()
    except Exception, e:
        print str(e)
        ssh.close()
        return False
    
def ssh_close(self):
    ssh.close()

