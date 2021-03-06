# 20CE015  AYUSH DABHI

# A: Write a Python program to add member(s) in a set and clear a set
set = {'H', 'e', 'l', 'l', 'o'}
set.add('!')
print("Letters: ", set)
print("Set after clear: ", set.clear())

# B: Write a Python program to remove an item from a set if it is present in the set.
set = {'H', 'e', 'l', 'l', 'o'}
set.remove('o')
print("Letters: ", set)

# C: Write a Python program to create an intersection, Union, difference of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Union of A and B: ", set1.union(set2))
print("Intersection of A and B: ", set1.intersection(set2))
print("Difference of A and B: ", set1.difference(set2), set2.difference(set1))

# D: Write a Python program to find maximum and the minimum value in a set.
set = {100, 200, 300, 400, 500}
print("Minimum value: ", min(set))
print("Maximum value: ", max(set))


# E: Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
def findcommon(items):
    tracker = {}
    for item in items:
        if item not in tracker.keys():
            tracker[item] = 0
        tracker[item] = tracker[item] + 1
    maxitem = None
    max = -1
    for key in tracker.keys():
        if (tracker[key]) > max:
            max = tracker[key]
            maxitem = key
    return maxitem


l1 = [1, 2, 3, 2, 3, 2, 4, 5, 6]
tuple1 = ("apple", "banana", "apple", "mango")

print("Common in List: ", findcommon(l1))
print("Common in Tuple: ", findcommon(tuple1))








