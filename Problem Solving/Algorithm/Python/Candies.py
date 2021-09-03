'''
Link: https://www.hackerrank.com/challenges/candies/problem
'''
#Program
def candies(n, arr):
    c=[] 
    for _ in range(n): 
        c.append(1) 
    for i in range(n-1): 
        j=i+1 
        if arr[j]>arr[i]: 
            c[j]=c[i]+1 
    for i in range(n-1,0,-1): 
        j=i-1 
        if arr[j]>arr[i]: 
            if c[j]<=c[i]: 
                c[j] = c[i]+1 
    return sum(c)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    print(result)
