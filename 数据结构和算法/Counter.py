#coding:utf-8
"""
实现collections中的Counter的一些妙用

案例:
    A 仓库中的货物
    B 仓库中的货物
    结果: 计算仓库中各物品的数量, 以及总和和差额

"""

from collections import Counter

A = Counter(['apple', 'banana', 'pear', 'banana', 'banana', 'pear', 'pear', 'pear', 'peach'])
B = Counter(['apple', 'apple', 'banana', 'pear', 'banana', 'banana', 'pear', 'pear', 'pear'])

#A、B仓库中的货物存量
print 'A'
for a in A:
    print "%s : %s个"%(a, A[a])

print 'B'
for b in B:
    print "%s : %s个"%(b, B[b])

#货物总量
print 'A + B'
a_add_b = A + B
for a_b in a_add_b:
    print "%s : %s个"%(a_b, a_add_b[a_b])

#货物差
print 'A - B'
a_diff_b = A - B
for a_b in a_diff_b:
    print "%s : %s个" % (a_b, a_diff_b[a_b])


