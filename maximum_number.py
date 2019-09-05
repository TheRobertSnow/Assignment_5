running = True
max_int = 0
while running: # While running is not False
    num_int = int(input("Input a number: "))
    if num_int < 0:
        running = False
    elif num_int > max_int:    # If user input is bigger than current maximum even number
        max_int = num_int
print("The maximum is", max_int)
