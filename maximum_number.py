running = True
max_int = 0
while running: # While running is not False
    user_in = int(input("Input a number: "))
    if user_in < 0:
        running = False
    elif user_in%2==0: # if user input is an even number and not a negative number
        if user_in > max_int:    # If user input is bigger than current maximum even number
            max_int = user_in
print("The maximum is", max_int)
