number = int(input("Enter a number less than 25\n"))
if number <= 25:
    while number in range(number,25+1):
        print("Inside the loop, my variable is", number)
        number = number + 1
else:
    print("Error")
