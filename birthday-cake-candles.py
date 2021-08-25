'''
Link - https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''

#Program
n = int(input().strip())
print
height = [int(height_temp) for height_temp in input().strip().split(' ')]

print(height.count(max(height)))
