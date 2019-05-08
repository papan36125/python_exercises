# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Set Union
# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

print(A.union(B))

print(B.union(A))
# Set Intersection
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)
print(A.intersection(B))

# use intersection function on B
print(B.intersection(A))
# Set difference
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)

# use difference function on A
print(A.difference(B))
# use - operator on B
print(B - A)
# use difference function on B
print(B.difference(A))

# Symmetric difference
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)
# use symmetric_difference function on A
print(A.symmetric_difference(B))

# use symmetric_difference function on B
print(B.symmetric_difference(A))
