
# num =[1,2,3,4,5,6,7,8,9,10]
# for n in num:
#     print(n)

# print("=======")

# for n in range(1,11):
#     print(n)

# for n in range(1,11,2):
#     print(n)

# for i in range(1,4):
#     for j in range(1,4):
#         print(f"i={i}, j={j}")



# while loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1  


# Task1
# for i in range(1,11):
#     if i == 7:
#         break
#     print(i)

# Task2

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)


# Task3
# import random


# even_numbers=[]
# for i in range(1,21):
#     if i % 2 == 0:
#         even_numbers.append(i)
# print(even_numbers)


# # task4
# number = input("Enter a number: ")
# digit_count = len(number)
# print("Number of digits:", digit_count)



# task5
# secret_number = random.randint(1, 10)

# guess = None

# while guess != secret_number:
#     guess = int(input("Guess a number between 1 and 10: "))
    
#     if guess < secret_number:
#         print("Too low, try again.")
#     elif guess > secret_number:
#         print("Too high, try again.")
#     else:
#         print("Correct! You guessed the number.")


# task6

# num= int(input("Enter a number: "))
# even_count=0
# odd_count=0
# for i in range(1,num+1):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"Number of even numbers: {even_count}")
# print(f"Number of odd numbers: {odd_count}")


# task7
# n=5
# for i in range(1,n+1):
#     spaces = " " * (n - i)
#     print(spaces + "*" * i)


#task8
sub=["Math", "Science", "English"]
marks=[]
for s in sub:
    num=int(input(f"Enter marks for {s}: "))
    marks.append(num)
avg=sum(marks)/len(marks)

if marks[0] >= 40 and marks[1] >= 40 and marks[2] >= 40:
    print("passed")
    print(f"Average Marks: {avg}")
    if avg >= 40:
        if avg >= 80:
            print("Grade: A")
        elif avg >= 60:
            print("Grade: B")
        else:
            print("Grade: C")
    if avg>=70:
        print("SCHOLARSHIP")
else:
    print("failed")