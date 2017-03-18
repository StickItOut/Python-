#coding:utf-8

from operator import itemgetter
from itertools import groupby

# ***************** 根据字段将记录分组 **********************
rows = [
    {'name': '张三', 'state':'山西省', 'age': 23},
    {'name': '李四', 'state':'山西省', 'age': 24},
    {'name': '张五', 'state':'山西省', 'age': 21},
    {'name': '张六', 'state':'陕西省', 'age': 26}
]

for state, messages in groupby(rows, key=itemgetter('state')):
    print '%s的人员如下:'%state
    for message in messages:
        print '姓名: %s, 年龄: %s'%(message['name'], message['age'])