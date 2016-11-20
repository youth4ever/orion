import collections

a = [1,1,9,1,7,3,1,2,7,2,2,7,9,2,3,3,4,5,5]

counter=collections.Counter(a)
print(counter)
# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
print(counter.values())
# [4, 4, 2, 1, 2]
print(counter.keys())
# [1, 2, 3, 4, 5]
print(counter.most_common(3))
# [(1, 4), (2, 4), (3, 2)]

print(counter.items())
print(counter[9])
print(type(counter))

for i in counter:
    print(i, counter[i],end=' ')