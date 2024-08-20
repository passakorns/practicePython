# Creating a dictionary with some initial key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)

# Accessing a value by its key
name = person["name"]
print("Name:", name)

# Using the get method to access a value (returns None if key doesn't exist)
age = person.get("age")
print("Age:", age)

# Trying to access a key that doesn't exist using get (returns None)
salary = person.get("salary")
print("Salary:", salary)

# Changing the value of an existing key
person["age"] = 31
print("Updated age:", person["age"])

# Adding a new key-value pair
person["email"] = "alice@example.com"
print("Updated dictionary:", person)

# Removing a key-value pair using del
del person["city"]
print("Dictionary after deletion:", person)

# Removing a key-value pair using pop (also returns the removed value)
email = person.pop("email")
print("Popped email:", email)
print("Dictionary after popping:", person)

# Looping through the keys
for key in person:
    print("Key:", key)

# Looping through the values
for value in person.values():
    print("Value:", value)

# Looping through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")


# Checking if a key is in the dictionary
if "name" in person:
    print("Name is in the dictionary.")
else:
    print("Name is not in the dictionary.")



# Getting the number of key-value pairs in the dictionary
length = len(person)
print("Number of key-value pairs:", length)


# Merging two dictionaries using the update method
additional_info = {"city": "Boston", "phone": "123-456-7890"}
person.update(additional_info)
print("Merged dictionary:", person)

# Creating a new dictionary using comprehension
squared_numbers = {x: x*x for x in range(5)}
print("Squared numbers:", squared_numbers)


# Creating a copy of a dictionary
person_copy = person.copy()
print("Copied dictionary:", person_copy)


# Removing all key-value pairs from the dictionary
person.clear()
print("Cleared dictionary:", person)

# Creating a dictionary with nested dictionaries
employees = {
    "employee1": {"name": "John", "age": 25, "department": "HR"},
    "employee2": {"name": "Jane", "age": 29, "department": "Finance"}
}
print("Employees dictionary:", employees)

# Accessing values in a nested dictionary
employee1_name = employees["employee1"]["name"]
print("Employee1's name:", employee1_name)
