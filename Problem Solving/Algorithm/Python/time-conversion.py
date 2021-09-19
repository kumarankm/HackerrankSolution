'''
Link: https://www.hackerrank.com/challenges/time-conversion/submissions/code/219159363
'''

#Program
import re
n = input()
li = n.split(':')
a = li[len(li)-1]
if 'PM' in a:
    li[0]=str(int(li[0])+ 12)
    if(li[0] == str(24)):
        li[0] = str(12)
elif 'AM' in a:
    if(li[0]==str(12)):
        li[0] = str(0) + str(0)
else:
    pass
ll = ':'.join((li))
print(re.sub('[A-Z a-z]','',ll))
