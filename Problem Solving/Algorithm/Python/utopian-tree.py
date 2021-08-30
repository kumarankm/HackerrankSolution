'''
Link: https://www.hackerrank.com/challenges/utopian-tree/problem
'''
# Program
t = int(input().strip())
for t_itr in range(t):
    initre = 1
    count = 0
    n = int(input().strip())
    if(n == 0):
        print("1")
        continue
    H = 1
    for i in range(1,n+1):
        if(i % 2 != 0):
            H = H * 2
        if(i % 2 == 0):
            H = H + 1
    print(H)
