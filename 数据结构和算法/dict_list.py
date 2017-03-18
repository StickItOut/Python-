#coding:utf-8

from operator import itemgetter

dict_list_test = [
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 3, 'b': 6, 'c': 3},
    {'a': 4, 'b': 3, 'c': 2},
    {'a': 2, 'b': 5, 'c': 6},
    {'a': 2, 'b': 4, 'c': 6},
    {'a': 2, 'b': 6, 'c': 6}
]
result_list1 = sorted(dict_list_test, key=itemgetter('a'), reverse=True)
result_list2 = sorted(dict_list_test, key=lambda s: s['a'], reverse=True)
result_list3 = sorted(dict_list_test, key=lambda s: (s['a'], s['b']), reverse=True)
print result_list1
print result_list2
print result_list3

