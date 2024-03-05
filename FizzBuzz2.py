# Prints numbers 1-100, but for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”

for num in range(1, 101):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
