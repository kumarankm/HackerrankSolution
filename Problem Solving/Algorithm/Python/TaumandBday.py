'''
Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy  black gifts and  white gifts.

The cost of each black gift is  units.
The cost of every white gift is  units.
The cost to convert a black gift into white gift or vice versa is  units.
Determine the minimum cost of Diksha's gifts.

Sample Input

STDIN   Function
-----   --------
5       t = 5
10 10   b = 10, w = 10
1 1 1   bc = 1, wc = 1, z = 1
5 9     b = 5, w = 5
2 3 4   bc = 2, wc = 3, z = 4
3 6     b = 3, w = 6
9 1 1   bc = 9, wc = 1, z = 1
7 7     b = 7, w = 7
4 2 1   bc = 4, wc = 2, z = 1
3 3     b = 3, w = 3
1 9 2   bc = 1, wc = 9, z = 2

Sample Output

20
37
12
35
12

Question link: https://www.hackerrank.com/challenges/taum-and-bday/problem
'''

#Program
t = int(input())
for _ in range(t):
    first = list(map(int, input().rstrip().split()))
    b = int(first[0])
    w = int(first[1])
    second = list(map(int, input().rstrip().split()))
    bc = int(second[0])
    wc = int(second[1])
    z = int(second[2])
    cost = 0
    if abs(bc - wc) <= z:
        cost += (bc * b)
        cost += (wc * w)
    else:
        if(wc < bc):
            cost += b * (wc + z)
            cost += w * wc
        else:
            cost += b * bc
            cost += w * (bc + z)
    print(cost)
