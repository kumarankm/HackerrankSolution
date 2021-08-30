'''
Question link: https://www.hackerrank.com/challenges/kaprekar-numbers/problem
Sample Input

STDIN   Function
-----   --------
1       p = 1
100     q = 100
Sample Output

1 9 45 55 99

'''

#Program
p = int(input())
q = int(input())
for i in range(p, q+1):
    if i == 10 or i == 100 or i == 1000 or i == 10000:
        continue
    inn, count = 0, 0 
    sq = i**2 
    sub = str(sq)
    d = len(sub)
    if d % 2 == 0:
        a = ''
        val = 0
        for j in sub:
            a += j
            count += 1
            if count == d/2:
                val += int(a)
                a = ''
                count = 0
        if val == i:
            inn = 1
            print(i, end =' ')
            pass
            
    else:
        if d == 1 and i == sq:
            inn =1
            print(i, end =' ')
            pass
        elif d== 1:
            pass
        else:
            b, vall, visited = '', 0, 0
            for k in sub:
                b += k
                count += 1
                if count == d//2 and visited == 0:
                    vall += int(b)
                    b = ''
                    visited = 1
                    count = 0
                if count == (d//2) + 1 and visited == 1:
                    vall += int(b)
            countt, c, valll, visitedd = 0, '', 0, 0
            for g in sub:
                c += g
                countt += 1
                if countt == d//2 + 1 and visitedd == 0:
                    valll += int(c)
                    c = ''
                    visitedd = 1
                    countt = 0
                if countt == (d//2) and visitedd == 1:
                    valll += int(c)
                    inn = 1
            if vall == i or valll == i:
                inn = 1
                print(i, end= ' ')
if inn == 0:
    print('INVALID RANGE')
