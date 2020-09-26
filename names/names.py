import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# list comprehension reduced the runtime to 2.982466697692871 seconds
# [duplicates.append(n1) for n1 in names_1 for n2 in names_2 if n1 == n2]

# BST reduced the runtime to 0.11080193519592285 seconds
list1 = BSTNode(names_1[0])
next(iter(names_1))

[list1.insert(name) for name in names_1]
[duplicates.append(name) for name in names_2 if list1.contains(name)]

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
