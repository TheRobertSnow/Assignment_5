da_sum = 1
first = 1
second = 1
third = 1
n = int(input("Enter the length of the sequence: ")) # Do not change this line
for i in range(1, n + 1): # Run the number of times chosen by user
    print(da_sum)
    if i == 1:
        da_sum = first + second # 1+1
        first = da_sum
    elif i == 2:
        da_sum = first + second # 2+1
        second = da_sum
    else:# Check for the variable with lowest number and assign it to the highest number
        da_sum = first + second + third
        if second > first and third > first:
            first = da_sum
        elif first > second and third > second:
            second = da_sum
        elif first > third and second > third:
            third = da_sum
