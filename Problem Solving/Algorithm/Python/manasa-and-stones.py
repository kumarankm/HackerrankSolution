'''
Url: https://www.hackerrank.com/challenges/manasa-and-stones/problem
'''

#Program

def stones(n, a, b):
    nn = n - 1
    ac = nn
    bc = 0
    st = []
    for i in range(n):
        last = (a * ac) + (b * bc)
        st.append(last)
        ac -= 1
        bc += 1
    s = set(st)
    fin = list(s)
    fin.sort()
    return fin
          
if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        print(' '.join(map(str, result)))
