# Prints numbers 1-100, but for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”
# For numbers which are multiples of both three and five print “FizzBuzz”

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

