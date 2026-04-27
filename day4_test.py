
# num=[2,4,6,1,3,5,7,9,8,10]


# def prime_number(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return n*2

# result = list(map(prime_number, num))
# print(result)


# def even_number(n):
#     if n % 2 == 0:
#         return n**2
#     else:
#         return None
    
# result_map = list(map(even_number, num))
# print(result_map)

# result_filter=list(filter(even_number, num))
# print(result_filter)

# newNum = [n**2 for n in num if n % 2 == 0]
# print(newNum)



# Game_Testing
import random

print("Welcome to the game!")
amount = int(input("Enter the amount: "))
ask=input("Do you want to play the game? (y/n) ").strip().lower()
while ask == "y":
    if amount < 1000:
        print("1000 is required to play the game.")
        status = input("Do you want to play the game again? (y/n) ").strip().lower()
        if status == "y":
            amount = int(input("Enter the amount: "))
            continue
        print("Thank you for playing the game!")
        break
    amount-=1000
    num = random.randint(1, 10)
    guess_number = int(input("Guess a number between 1 and 10: "))

   
    if guess_number < 1 or guess_number > 10:
        print("Please guess a number between 1 and 10.")
        continue

    elif guess_number == num:
            amount += 10000
            print(f"Congratulations! your amount is multiplied to {amount}.")
    else:
            print(f"Sorry, the correct number was {num}. Your amount is {amount}.")

    status = input("Do you want to play the game again? (y/n) ").strip().lower()
    if status != "y":
        print("Thank you for playing the game!")
        break
