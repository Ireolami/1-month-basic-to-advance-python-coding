"This programme performs set operation"
set_a = {2,3,4,5,6,7,8,9}
set_b = {1,3,5,8,0}
"Union"
# print(set_a.union(set_b))
"interjection"
# print(set_a.intersection(set_b))
"isdisjoint"
# print(set_a.isdisjoint(set_b))
print(set_a.difference_update(set_b))