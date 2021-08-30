'''
Link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
'''

# Program

n = int(input())
if(n == 1918):
    print("26.09.1918")
if(n < 1918):
    if(n % 4 == 0):
        print("12.09.{}".format(n))
    else:
        print("13.09.{}".format(n))
if(n > 1918):
    if(n % 4 == 0):
        if(n % 100 == 0):
            if(n % 400 == 0):
                 print("12.09.{}".format(n))
            else:
                 print("13.09.{}".format(n))
        else:
             print("12.09.{}".format(n))
    else:
         print("13.09.{}".format(n))
            
