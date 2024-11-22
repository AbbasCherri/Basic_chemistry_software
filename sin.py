x = int(input()) #the number we are extracting the digits from
z= x #replica
y = x #another replica
count = 0
intended_sum = int(input()) #the sum of any two digits
condition = False 
while x>0:
    y=z
    digit = x%10 #check the digit in the beginning
    count = count +1 #increment the count by one so that it does not take duplicates
    count_2 = 1 # same concept
    while y>0:
        if count == count_2:
            count_2 = count_2 + 1
        else:
           digit_1 = y%10
           if digit_1 + digit == intended_sum:
              condition = True
              break 
        y =y//10
    x=x//10
    if (z//10)>0:
       if digit_1 + digit == intended_sum:
           break
if condition:
    print("True")
else:
    print("False")
