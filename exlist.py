# Creating a list of fruits
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)
# Accessing the first element
first_fruit = fruits[0]
print("First fruit:", first_fruit)

# Accessing the last element
last_fruit = fruits[-1]
print("Last fruit:", last_fruit)
# Changing the second element
fruits[1] = "blueberry"
print("Modified list:", fruits)
# Adding an element to the end of the list
fruits.append("elderberry")
print("List after appending:", fruits)

# Inserting an element at a specific position
fruits.insert(2, "fig")
print("List after inserting:", fruits)
# Removing a specific element by value
fruits.remove("date")
print("List after removing 'date':", fruits)

# Removing the last element using pop
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("List after popping:", fruits)

# Removing an element by index
del fruits[1]
print("List after deleting the second element:", fruits)

# Getting a sublist (slice)
sublist = fruits[1:3]
print("Sublist (from index 1 to 2):", sublist)

# Iterating through the list
for fruit in fruits:
    print("Fruit:", fruit)

# Creating a new list with list comprehension
uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", uppercase_fruits)

# Checking if an element is in the list
if "apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")

# Getting the number of elements in the list
length = len(fruits)
print("Number of fruits:", length)

# Concatenating two lists
more_fruits = ["grape", "honeydew"]
all_fruits = fruits + more_fruits
print("Combined list:", all_fruits)

# Sorting the list alphabetically
fruits.sort()
print("Sorted list:", fruits)

# Sorting the list in reverse alphabetical order
fruits.sort(reverse=True)
print("Reverse sorted list:", fruits)

# Copying a list
fruits_copy = fruits.copy()
print("Copied list:", fruits_copy)


# Removing all elements from the list
fruits.clear()
print("Cleared list:", fruits)


