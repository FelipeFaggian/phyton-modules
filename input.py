print("Tell me anything...")
anything = input()
print("Hmm... You said: '", anything, "'... Are you sure?", sep="")

anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

# Testing TypeError message.
#anything = input("Enter a number: ")
#something = anything ** 2.0
#print(anything, "to the power of 2 is", something)


anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)


leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)


leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5

#string + string
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

#string * number
#number * string
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#drawing a retangle
print("*" + " - " * 10 + "*", end="")
print(("\n|" + "   " * 10 + "|") * 5)
print("*" + " - " * 10 + "*")

#drawing a triangle
print(" " * 6 + "/\\")
print(" " * 5 + "/  \\")
print(" " * 4 + "/    \\")
print(" " * 3 + "/      \\")
print(" " * 2 + "/        \\")
print(" " * 1 + "/          \\")
print("/__ _ ____ __\\")

#number into string
#str(number)
#example
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

#input output lab
input_number1 = float(input("Insert a float number here: ")) 
input_number2 = float(input("Insert other float number here: "))
print("The addition's result of these numbers is: ", input_number1 + input_number2)
print("The subtraction's result of these numbers is: ", input_number1 - input_number2)
print("The multiplication's result of these numbers is: ", input_number1 * input_number2)
print("The division's result of these numbers is: ", input_number1 / input_number2)
print("\nThat's all, folks!")

# intermediate lab's exercise with operators and expressions
x = float(input("Enter value for x: "))
y = 1 / (x + 1 / (x + 1 / (1 / x + x)))
print("y =", y)

# period of time's measure code (with some cheating) 
initial_hour = int(input("Starting time (hours): "))
initial_mins = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))
hours_traveled = int((initial_mins + duration) / 60)
mins_traveled = (initial_mins + duration) % 60
hour_finish = int(hours_traveled + initial_hour)
if hour_finish > 24:
    print("The party has over at ", (hour_finish % 24), ":", mins_traveled, sep="")
else:
    print("The party has over at ", hour_finish, ":", mins_traveled, sep="")
    

