# animals=['dog','pig']
# animals.insert(2,'cat')
# animals.pop(2)
# animals.remove('pig')
# print(animals)


# numbers=[1,2,3,4,5,[6,7,8,9]]

# print (numbers[5][2])

# print("=======")

# for num in numbers:
#     if isinstance(num,list):
#         for n in num:
#             print(n)
#     else:
#         print(num)

# print("=======")

# for num in numbers:
#     print(num)


# members=("John")
# print(type(members))

# members=("John","Jane","Jack")
# print(type(members))

# members[1]="Doe" 
# print(members)




# employees=['Alice','Bob','Charlie']
# employees_new=[]
# for emp in employees:
#     employees_new.append(emp)
# print(employees_new)

# employees_new2=[emp for emp in employees if "B" in emp ]
# print(employees_new2)



# task1

# numbers=[1,2,3,4,5]
# reverse_numbers=[]
# for num in range(len(numbers)-1,-1,-1):
#     reverse_numbers.append(numbers[num])
# print(reverse_numbers)

# numbers.reverse()
# print(numbers)


# task2

# numbers=[1,2,3,4,5]
# maxvalue=numbers[0]
# minvalue=numbers[0]
# for num in numbers:
#     if num > maxvalue:
#         maxvalue=num
#     if num < minvalue:
#         minvalue=num        
# print(maxvalue)
# print(minvalue)

# print(max(numbers))
# print(min(numbers))



# task3

# lst = [10, 20, 30, 40, 50]

# print("First:", lst[0])
# print("Last:", lst[-1])


# first = next(iter(lst))
# last = next(reversed(lst))

# print("First:", first)
# print("Last:", last)


# task4

# lst.append(60)
# print(lst)

# lst +=[70]
# print(lst)


# task5
# count=5
# lst=[]
# for i in range(count):
#     num=int(input("Enter a number: "))
#     lst.append(num)
# print(sorted(lst))


# task6
count=5
lst=[]
pass_count=0
fail_count=0
for i in range(count):
    marks=int(input("Enter a Marks: "))
    lst.append(marks)

turple=tuple(lst)
for mark in turple:
    if mark >=50:
        print("Pass")
        pass_count+=1
    else:
        print("Fail")
        fail_count+=1

total_marks=sum(turple)
avg=total_marks/len(turple)

print(f"Pass Count: {pass_count}")
print(f"Fail Count: {fail_count}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {avg}")