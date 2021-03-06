import time
from BST import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#duplicates = []

#Default Algorithm for finding duplicates
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#We can Binary Search Tree to find things faster

#We are trying to find names_1 duplicates, so storing this binary tree can help check faster in simple one pass loop

#Instantiate BST
# binary_search = BinarySearchTree(names_1[0])

# #Add rest of the names, skip first one
# for name in names_1[1:]:
#     binary_search.insert(name)
# for duplicate in names_2:
#     if binary_search.contains(duplicate):
#         duplicates.append(duplicate)

duplicates = list(set(names_1).intersection(names_2))

#List will be created unordered

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
