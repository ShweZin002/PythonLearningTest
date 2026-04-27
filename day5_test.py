
# person={"name":"John","age":30,"city":"New York"}


# print(person.keys())
# print(person.values())
# print(person)

# person["age"]=31
# person["hair_color"]="brown"

# for (k,v) in person.items():
#     print(f"{k}: {v}")

# person.pop("age")
# print(person)

# del person["city"]
# print(person)


# colors={"red","green","blue"}
# print(colors)
# colors.add("yellow")
# print(colors)
# colors.remove("green")
# print(colors)
# colors.discard("purple")
# print(colors)

# numbers={1,3,4,5,8,2 }
# print(numbers)


# employees = {
#     "emp1": {"name": "John", "age": 30, "started_working_at": "2023"},
#     "emp2": {"name": "Alice", "age": 25, "started_working_at": "2022"},
#     "emp3": {"name": "Bob", "age": 35, "started_working_at": "2020"}
# }

# sorted_employees = sorted(employees.values(), key=lambda x: x["started_working_at"])

# print(sorted_employees)

# task 1
text = "apple banna apple banna orange grape orange apple"

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

# task 2
list= [1, 2, 3, 4, 5,3,4,2]
unique_list = (set(list))
print(unique_list)

# task 3
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)    
print(common)

# task 4
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
new_list = (set(list1) | set(list2))
print(new_list)

# task 5
text = "hello world"

unique_chars = set(text)

print("Unique characters:", unique_chars)
print("Count:", len(unique_chars))
print("changes from main branch")