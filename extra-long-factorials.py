'''
Link: https://www.hackerrank.com/challenges/extra-long-factorials/problem
'''

#Program
def extraLongFactorials(n):
    count = 1
    for i in range(1, n+1):
        count = count * i
    print(count)
        

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)

