'''
LCM of two and three numbers
'''

# LCM of two numbers:
a = int(input('Enter a first number: '))
b = int(input('Enter a second number: '))
maz = max(a,b)
min = min(a,b)
count = 1
while True:
    if (maz * count) % min == 0:
        print('Lcm', maz * count)
        break
    count += 1


# LCM of three numbers:
a = int(input('Enter a first number: '))
b = int(input('Enter a second number: '))
c = int(input('Enter a third number: '))
dum = [a, b, c]
maz = max(a, b, c)
dum.remove(maz)
min1 = dum[0]
min2 = dum[1]
count = 1
while True:
    if (maz * count) % min1 == 0 and (maz * count) % min2 == 0 :
        print('Lcm', maz * count)
        break
    count += 1
