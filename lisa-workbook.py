'''
Url: https://www.hackerrank.com/challenges/lisa-workbook/problem
'''

#Program
def workbook(n, k, arr):
    page = 1
    count = 0
    kk = k
    for j in range(n):
        i = 1
        while(i <= k):
            if i == page:
                count += 1
            if i == k:
                k = k + kk
                page += 1
            if i == arr[j]:
                k = kk
                page += 1
                if arr[j] % kk == 0:
                    page -= 1
                break
            i += 1
    return count
            

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(result)
