for i in range(4, 0, -1):
    print(i)
print([1, 2][2:])
aa = [1, 2]
bb = aa.copy()
aa[0] = 5
print(bb)
print(int((1 + 4) / 2))
print(len([1, 2]))
arr = [1, 2]
arr[0:0] = [3, 5]
dict = {'a': 12}
print(dict['a'], 'b' not in dict)
print(arr)
arr = [{'a': 2}, {'b': 3, 'a': 4}]
print(arr.pop())
print([x['a'] for x in arr])
# arr[0], arr[1] = arr[1], arr[0]
print(arr)
print([1, 2] + [3, 4])
# for i in range(2, 10):
#     print(i)

cc = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
# print(cc[1])

import sys
import gc
import weakref

rubbish = {}
rub = set()
wr = weakref.ref(rub)
# wr = rub
gc.collect()
del rub
# print('wr', wr, rub)
# print('reference:', sys.getrefcount(rubbish))
# rubbish = None
# gc.collect();
# print(wr)
# print('reference:', sys.getrefcount(rubbish))
# print(rubbish)

a1, a2 = [1], [1]
print(id(a1))
print(a1 == a2)

s = set()
s.add((1, 2))
s.add((1, 2))
print(*s)
print([num for num in (5, 6)])
# -*- coding: utf-8 -*-

mystr = "banana"
myit = iter(mystr)


def examine(x: str):
    x += x
    return x * 2


examine(2)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
