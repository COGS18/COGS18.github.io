# ^ You can ignore this line - it is used to help check your code

# YOUR CODE HERE
if check_1 and check_2:
    outcome = 'BOTH'
elif check_1 and not check_2:
    outcome = 'ONE'
elif not check_1 and check_2:
    outcome = 'TWO'
else:
    outcome = 'NEITHER'