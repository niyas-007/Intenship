"""--- PART 1: BASICS & INITIALIZATION ---"""

"""1. Create a tuple containing five different data types (int, float, string, list, boolean)"""

# a=(10,10.50,"Apple",[10,20,30],True)
# print(a)

"""2. Write a script to check the type of a tuple with a single element. Show the difference 
between (5) and (5,)."""

# a = (5)
# print("a =", a)
# print("Type of a:", type(a))

# b = (5,)
# print("\nb =", b)
# print("Type of b:", type(b))

"""3. Access the last element of a tuple without knowing its length."""

# num=(10,20,30,40,50,60,70,80)
# print(num[-1])

"""4. Access the second to last element of a tuple using negative indexing"""

# num=(10,20,30,40,50,60,70,80)
# print(num[-2])

"""5. Given nested_tuple = ("Python", [10, 20, 30], (5, 15, 25)), print the number 20."""

# nested_tuple = ("Python", [10, 20, 30], (5, 15, 25))
# print(nested_tuple[1][1])

"""6. Check if the element 'Sreeraj' exists in a tuple using a membership operator."""

# names=("sreeraj","shakir","jasil","yaseen","najad")
# print("sreeraj" in names)

"""7. Find the memory size of a list vs. a tuple with the same elements using the sys module."""

import sys
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)

print("List:", list_example)
print("Size of list:", sys.getsizeof(list_example), "bytes")

print("\nTuple:", tuple_example)
print("Size of tuple:", sys.getsizeof(tuple_example), "bytes")
