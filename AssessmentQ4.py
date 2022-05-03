# importing the necessary Library
from num2words import num2words as n2w

#Writing the function for deliberate number of ranges or numbers
def game():
    # Getting the desired range of numbers
    try:
        a, b = [int(x) for x in
                input("Please enter the start and stop of your desired range separated with a space: ").split()]

        if a > b or a < 0:
            return ('Invalid format for the range')

    except ValueError:
        return ('Invalid format for the range')

    # Getting the numbers to be printed as word (like 3 and 5 in the previous problem)
    try:
        x = [int(x) for x in
             input("Now enter the number(s) you want to see as word(s) separated with a space: ").split()]
    except:
        return ('Invalid format for the printing numbers')

    # creating the output as a list
    output = []

    for num in range(a, b + 1):
        ans_str = ""
        #If the number is divisible by any number the concatenation will happen
        for j in range(0, len(x)):
            if num % x[j] == 0:
                ans_str += n2w(x[j])
        if not ans_str:
            ans_str = str(num)
        output.append(ans_str)
    print(output)


game()
