'''
Link: https://www.hackerrank.com/challenges/arrays-ds/problem
'''

# Program


def reverseArray(a):
    es = a[::-1]
    return es


if __name__ == '__main__':

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(' '.join(map(str, res)))
