
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# country=input("Enter your country: ")
# print(f"Your name is {name}, you are {age} years old, and you are from {country}.")
# print("Your name is"+name+"age is"+str(age)+"country is"+country)
# print("Name is",name,"age is",age,"country is",country)

# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")


# num=input("Enter a number: ")
# if not num.isdigit():
#     print("Invalid input.")
# elif int(num)%2==0:
#     print(f"{num} is an even number.")  
# else:
#     print(f"{num} is an odd number.")   


marks=input("Enter your marks: ")
if not marks.isdigit():
    print("Invalid input.")
elif int(marks) >=40:
    print("You passed the exam.")
else:
    print("You failed the exam.")           