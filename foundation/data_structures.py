# lists - ordered mutable collection of items (items could be of different data types
my_list = [1, 2, 3]

mixed_list = [1, 2, 3, "george", True, my_list, False]
print(mixed_list)
fruits_list = ["apple", "banana", "cherry"]

# indexing
print(fruits_list[0])

try:
    print(fruits_list[10])
except IndexError:
    print("You are trying to subset for an item that does not exist")
    print(f"Length of your list: {len(fruits_list)}")

# slicing
print(fruits_list[2:])
print(fruits_list[:2])
print(fruits_list[::2])
print(fruits_list[::-1])
print(fruits_list[1::2])

# list methods

fruits_list.insert(1, "guava")
print(fruits_list)

fruits_list.remove("guava")
print(fruits_list)

fruits_list.pop(2)
print(fruits_list)

fruits_list.append("mango")
print(fruits_list)

fruits_list.pop()
print(fruits_list)

apple_index = fruits_list.index("apple")
print(apple_index)

print(fruits_list.count("apple"))

fruits_list.sort()

fruits_list.reverse()

fruits_list.clear()
print(fruits_list)


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in my_numbers:
    print(f"Number {number}")


indexes = enumerate(my_numbers)
print(indexes)
print(type(indexes))

for index, number in enumerate(my_numbers):
    print(index, number)


# list comprehension
# [expression for item in iterable]

my_numbers_sq = [number**2 for number in my_numbers]
print(my_numbers_sq)

# [expression for item in iterable if condition]
my_numbers_sq = [number**2 for number in my_numbers if number % 3 == 0]
print(my_numbers_sq)

# [expression for item1 in iterable1 for item2 in iterable2]
list1 = [1, 2, 3]
list2 = [4, 5, 6]
final_list = [i * j for i in list1 for j in list2]
print(final_list)








