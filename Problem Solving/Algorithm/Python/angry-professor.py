'''
Link: https://www.hackerrank.com/challenges/angry-professor/problem
'''

#Program

t = int(input())
for _ in range(t):
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    posi = int(first_multiple_input[1])
    a = list(map(int, input().rstrip().split()))
    count = 0
    for i in range(n):
        if(a[i] <= 0):
            count += 1
        else:
            pass
    if count < posi:
        print("YES")
    else:
        print("NO")
