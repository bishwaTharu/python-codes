 # intersection
 # To find out which members attended both events
a = set([1,2,3,4])
b = set([1,2,5,6,7])
 # a intersection b
print(a.intersection(b))
 # b intersection a
print(b.intersection(a))
# symmetric difference
""" returns a set that contains all items from both set
, but not the items that are present in both sets """
# To find out which members attended only one of the events
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
# difference operator in sets
# To find out which members attended only one event and not the other
print(a.difference(b))
print(b.difference(a))
# union operator in python 
# To receive a list of all participants
print(a.union(b))
print(b.union(a))