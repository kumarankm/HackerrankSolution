'''
Link: https://www.hackerrank.com/challenges/picking-numbers/problem
'''
# Program
n = int(input().strip())
a = list(map(int, input().rstrip().split()))
a.sort()
maxx = 0
for i in range(n):
    count = 0
    for j in range(i,n):
        if abs(a[i]-a[j]) <= 1:
            count += 1
    if(count > maxx):
        maxx = count
print(maxx)
        
