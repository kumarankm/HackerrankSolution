'''
Link: https://www.hackerrank.com/challenges/bon-appetit/problem
'''

#Program
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())

tot = sum(bill)
ref = tot - bill[k]
ann = ref//2
if(ann == b):
    print("Bon Appetit")
else:
    print(b - ann)
