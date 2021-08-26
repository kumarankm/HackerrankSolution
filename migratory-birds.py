'''
Link: https://www.hackerrank.com/challenges/migratory-birds/problem
'''

# Program
arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
arr.sort()
t1, t2, t3, t4, t5 = 1, 2, 3, 4, 5
c1, c2, c3, c4, c5 = 0, 0, 0, 0, 0
for i in range(len(arr)):
    if(arr[i] == t1):
        c1 += 1
    if(arr[i] == t2):
        c2 += 1
    if(arr[i] == t3):
        c3 += 1
    if(arr[i] == t4):
        c4 += 1
    if(arr[i] == t5):
        c5 += 1
a = [c1,c2,c3,c4,c5]
ma = max(a)
print(a.index(ma)+1)
