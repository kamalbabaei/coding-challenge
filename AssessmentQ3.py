#Creating a list to store all the sequence
output = []
#creating a for loop to check all numbers from 1 to 100
for num in range(1, 101):
    #Creating a string to record the divisibility for each number
    ans_str = ""
    # Divisible by 3
    if num%3==0:
        ans_str += "Three"
    # Divisible by 5
    if num%5==0:
        ans_str += "Five"
    # Not divisible by 3 or 5 (str is empty)
    if not ans_str:
        ans_str = str(num)

    # Append the str for this number to the final output list
    output.append(ans_str)

print(output)