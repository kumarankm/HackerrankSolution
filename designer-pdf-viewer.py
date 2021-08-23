'''
Link: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
'''

#Program
hh = list(map(int, input().rstrip().split()))
word = input()
alpha = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

maxx = 0
for i in range(len(word)):
    a = alpha.index(str(word[i]))
    if(hh[a] > maxx):
        maxx = hh[a]
print(maxx * len(word))
