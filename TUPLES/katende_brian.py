# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Iterating over a tuple
for item in my_tuple:
    print(item)  # Output: 1, 2, 3


# Tuple unpacking
x, y, z = my_tuple
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3

# Tuple with a single element
single_tuple = (4,)  # Note the trailing comma
print(single_tuple)  # Output: (4,)

# Tuple concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4)


# Checking if an element exists in a tuple
print(2 in my_tuple)  # Output: True
print(6 in my_tuple)  # Output: False

# Getting the length of a tuple
print(len(my_tuple))  # Output: 5
