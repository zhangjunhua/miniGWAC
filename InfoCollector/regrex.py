import re

print(re.match(r'hello','hello world hello!').group())

m=re.search(r'\[.*\]','dkdjf[kdjf]f')
if m:
    print(m.group())
else:
    print('match failed!')


