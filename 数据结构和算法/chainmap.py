#coding:utf-8

from collections import ChainMap

a = {'x': 1, 'y': 3}
b = {'y': 1, 'z': 3}

c = ChainMap(a, b)

print c['y']
print c.values()