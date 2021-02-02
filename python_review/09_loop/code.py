number = 7

while True:
    user_input = input("Would you like to play? y/n ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

print("Thanks for playing!")

friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")

grades = [35, 67, 98, 100, 100]
# total = 0
# amount = len(grades)

# for grade in grades:
#     total += grade 


# grade_average = total / amount

# print(grade_average)

total = sum(grades)
amount = len(grades)

grade_average = total / amount

print(grade_average)