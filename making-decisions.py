#a==b (Is a equal to b?)

#2 == 2. (Python can convert and realize that's is a True equal)

#equality
var = 0  # Assigning 0 to var
print(var == 0)
var = 1  # Assigning 1 to var
print(var == 0)

#inequality
var = 0  # Assigning 0 to var
print(var != 0)
var = 1  # Assigning 1 to var
print(var != 0)

#black_sheep > white_sheep  # Greater than

# centigrade_outside ≥ 0.0  # Greater than or equal to

#current_velocity_mph < 85  # Less than
#current_velocity_mph ≤ 85  # Less than or equal to

#answer = number_of_lions >= number_of_lionesses

#Priority	Operator	
#1	+, -	unary
#2	**	
#3	*, /, //, %	
#4	+, -	binary
#5	<, <=, >, >=	
#6	==, !=

#if blocks for sure
n = int(input("Insert the value of  'n': "))
if(n >= 100):
    print("True")
else:
    print("False")


#if true_or_not:
#    do_this_if_true

#analogy about the follow-up of indent commands
#if the_weather_is_good:
#    go_for_a_walk()
#have_lunch()
    

#conditional
if sheep_counter >= 120: # Evaluate a test expression
    sleep_and_dream() # Execute if test expression is True

#indented and not indented
if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
feed_the_sheepdogs()

#two alternatives
if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false

#Plan A, B and General
if the_weather_is_good:
    go_for_a_walk()
else:
    go_to_a_theater()
have_lunch()

#no limits for alternatives and choices
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

#elif 
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

#the largest number
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
# Print the result
print("The larger number is:", larger_number)

#resuming just one-line instruction 
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2
# Print the result
print("The larger number is:", larger_number)

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

#strategy to logical comparison
# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1
# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2
# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3
# Print the result
print("The largest number is:", largest_number)

# a python function that do the work above more objectively
# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
largest_number = max(number1, number2, number3)
# Print the result.
print("The largest number is:", largest_number)

# or the opposite
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
lowest_number = min(number1, number2, number3)
# Print the result.
print("The lowest number is:", lowest_number)

#a pseudocode to explain loop
largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02
