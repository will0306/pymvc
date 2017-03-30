#!/usr/bin/env python
#-*- encoding: utf8 -*-
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email import Encoders
import smtplib,os




from_addr = to_addr = attach =  smtp_server = password = None
title = subject = content = ''

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def set_to_addr(kw):
    if isinstance(kw,list) == False:
        print("请传入list类型的参数")
        return False
    global to_addr
    to_addr = kw

def set_attach(kw):
    if isinstance(kw,dict) == False:
        print("请传入dict类型的参数")
        return False
    global attach
    attach = kw

def send_email():
    global from_addr, to_addr, attach, title, subject, smtp_server, password, content
    if from_addr == None :
        print('缺少发件人地址')
        return False
    if from_addr.find('@') == -1:
        print('发件人的地址有误：%s ' % from_add)
        return False
    if to_addr == None or len(to_addr) == 0:
        print('缺少收件人地址')
        return False
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg['To'] = ','.join(to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg.attach(MIMEText(content, 'plain', 'utf-8'))

    if attach != None or isinstance(attach,dict) != False:
        for i in attach:
            if os.path.exists(i) == False:
                print('%s 该文件不存在' % i)
                continue
            if attach[i] == '':
                temp = i.split('/')
                attach[i] = temp[len(temp) - 1]
            part = MIMEApplication(open(i,'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=attach[i])
            msg.attach(part)
    try:
            server = smtplib.SMTP()
            server.connect(smtp_server)
            server.login(from_addr,password)#XXX为用户名，XXXXX为密码
            server.sendmail(msg['From'], to_addr,msg.as_string())
            server.quit()
            print '发送成功'
    except Exception, e:
        print str(e)

def get_attach():
    global attach
    if attach == None or isinstance(attach,dict) == False:
        return False
    for i in attach:
        if os.path.exists(i) == False:
            print('%s 该文件不存在' % i)
            continue
        if attach[i] == '':
            temp = i.split('/')
            attach[i] = temp[len(temp) - 1]
            print(temp[len(temp) - 1])
    print(attach)
