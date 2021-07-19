'''
Question link: https://www.hackerrank.com/challenges/equality-in-a-array/problem
'''

#Program

n = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()
com, dum, visited, val = 0, 0, 0, 1
count = []
for i in range(1, n):
    if arr[i-1] == arr[i]:
        val += 1
        com = arr[i]
    else:
        count.append(val)
        val = 1
count.append(val)
ma = max(count)
for j in range(len(count)):
    if(count[j] != ma):
        dum += count[j]
    elif(visited == 1):
        dum += count[j]
    else:
        visited = 1
print(dum)
