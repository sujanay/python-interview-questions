from collections import OrderedDict
import tensorflow as tf

mylist = [('sujan', 1), ('ram', 2), ('haris',3), ('bam', 4)]
print('mylist:', mylist)

# create dictionary from list of tuples
# method-1
dict1 = {}
for name, score in mylist:
    dict1[name] = score

print(dict1)

# method-2
dict2 = dict(mylist)

print(dict2)

# ordered dict
od = OrderedDict(mylist)

print(od)