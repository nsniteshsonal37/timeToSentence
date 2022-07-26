from runner import out
import re

regex= '^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'
x="01:30"
res=re.match(regex,x)
if(res):
    print("YES")
else:
    print('NO!')
print(out(x))