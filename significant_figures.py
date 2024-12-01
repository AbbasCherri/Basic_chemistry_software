def sig_fig():
    num = input('Enter the desired number: ').strip()
    if not num: # validate input
        print('Invalid input. Please enter a number.')
    if 'x' in num and '10^' in num: # check for scientific notation in the format 'number x 10^number'
        base, _ = num.lower().split('x')  # split at 'x' to isolate the base part
        num = base.strip()  # use only the base part for counting significant figures
    l = list(num) # convert the number to a list of characters
    count = 0
    non_zero_started = False  # to indicate when significant digits start
    decimal_point = False  # to track the presence of a decimal point
    n = len(l)
    for i in range(n): # loop through the number to count significant figures
        if l[i] == '.':
            decimal_point = True  # mark the presence of a decimal point
        elif l[i] != '0' and l[i] != '.':
            count += 1  # count non-zero digits
            non_zero_started = True  # significant figures start
        elif l[i] == '0' and non_zero_started:
            count += 1  # count zeros only if they are significant
    if not decimal_point: # handle trailing zeros in whole numbers without a decimal point
        while l and l[-1] == '0':
            l.pop()  # remove trailing zeros
            count -= 1  # adjust count
    try:
        num = float(num)
        flag = True
    except ValueError:
        print('Input a number.')
        flag = False
    if flag == True:
        if count == 1: # print the result
            print(f'There is {count} significant figure in {num}')
        else:
            print(f'There are {count} significant figures in {num}')
sig_fig()