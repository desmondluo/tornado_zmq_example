#-*- coding: utf-8 -*-
import json
sockets = set()
hosts = dict()
items = dict()
tasks = set()
http_service = ()

def deal_host(shosts):
    global hosts
    push = False
    for key in shosts:
        if (hosts.has_key(key) and hosts[key] == shosts[key]):
            continue
        else:
            push = True
        hosts[key] = shosts[key]
    if (push):
        return
    return

def deal_item(sitems):
    global items
    for key in sitems:
        items[key] =sitems[key]
    return True

def set_http(http):
    global http_service
    http_service = http

def http_to_zabbix(msg):
    global http_service
    http_service.send_to_zabbix(msg)

def http_to_zlogger(task):
    global http_service
    http_service.send_to_zlogger(task)

def add_task(task):
    global tasks
    task = json.dumps(task)
    tasks.add(task)

def delete_task(task):
    global tasks
    task = json.dumps(task)
    if task in tasks:
        tasks.remove(task)

def len_task():
    global tasks
    return len(tasks)

