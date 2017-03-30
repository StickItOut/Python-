#coding:utf-8

import re

test_string = '<img src="//gtd.alicdn.com/sns_logo/i6/TB1EjxDKXXXXXXhaXXXSutbFXXX.jpg_60x60.jpg" alt="" width="60" height="60">'
prog = re.compile('<img src="(\S+)".*>', re.I)
print prog.findall(test_string)
