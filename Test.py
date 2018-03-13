# import analysistool
# import unittest


# class AnalysisToolTestCase(unittest.TestCase):
#     @staticmethod
#     def test_print():
#         print("Test print passed!")
#
#     @staticmethod
#     def test_print_digits():
#         print([1, 2, 3, 4])
#
#     @staticmethod
#     def no_test():
#         print("this shouldn't be executed in test")

# print("Hello Python")

a = {1: 2}

a = 'xyzwd'
print a[::2]

res = ''
for i in range(2, 100):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime:
        res += str(i) + ' '
print res.strip()

L = [0, 1, 2, 3, 4]
L.sort()
if len(L) % 2 == 0:
    res = L[len(L) / 2] + L[len(L) / 2 - 1]
    if res % 2 == 0:
        print res / 2
    else:
        print '%.1f' % ((res) / 2.0)
else:
    print L[len(L) / 2]

a = 3
b = 5
max_cmn_div = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        max_cmn_div = max(max_cmn_div, i)
print a * b / max_cmn_div

L = [2, 8, 3, 50]
count0 = 0
count2 = 0
count5 = 0

for a in L:
    while a % 2 == 0:
        count2 += 1
        a /= 2
    while a % 5 == 0:
        count5 += 1
        a /= 5
if count2 > count5:
    print 0
else:
    print 1

a = 7

b = bin(a)
print str(bin(a)).count('1')

import this

print this.s

from this import *

print s

a = "aaaaaabbbDDDDD"

print a.lower()

print '============================================================='

a = 24
b = 36
cmn_div_count = 0

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        cmn_div_count += 1
print cmn_div_count

a = 3
b = 60


def maxcmndiv(a, b):
    max_cmn_div = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max_cmn_div = max(max_cmn_div, i)
    return max_cmn_div


atmp = a
a = min(a, b)
b = max(atmp, b)
diff = b / a
mul = {}
for i in range(1, diff + 1):
    if diff % i == 0 and maxcmndiv(diff / i, i) == 1:
        mul[min(i, diff / i) * a] = max(i, diff / i) * a
mink = b
minv = b
for k, v in mul.items():
    if k + v < mink + minv:
        mink = k
        minv = v
print "%d %d" % (k, v)

a = 'OurWorldIsFullOfLOVE'

if 'love' in a.lower():
    print 'LOVE'
else:
    print 'SINGLE'

a = 'cagy'
b = 3
print ''.join(map(lambda x: chr(ord(x) + b) if (ord(x) + b) <= 122 else chr(ord(x) + b - 26), a))

a = 'abccbadkj'
n = 6


def recursive_oj(a, n):
    for i in range(len(a) - n + 1):
        if a[i:i + n] == a[i:i + n][::-1]:
            print 'YES'
            return
    print 'NO'


recursive_oj(a, n)

st = '00:00:00'
et = '23:59:59'

s = st.split(':')
e = et.split(':')

sv = int(s[0]) * 3600 + int(s[1]) * 60 + int(s[2])
ev = int(e[0]) * 3600 + int(e[1]) * 60 + int(e[2])

print ev - sv

print '====================================='

n = 20
m = 20

offset = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]


def next_step(x, y, X, Y):
    nextpoints = []
    for os_x, os_y in offset:
        if (x + os_x) >= 0 and (x + os_x) <= X and (y + os_y) >= 0 and (y + os_y) <= Y:
            nextpoints.append((os_x + x, os_y + y))
    return nextpoints


dis = []
for i in range(n + 1):
    row = []
    for j in range(m + 1):
        row.append(-1)
    dis.append(row)
dis[0][0] = 0
explorer = list()
explorer.append([0, 0])
while len(explorer) > 0:
    x, y = explorer.pop()
    nextpoints = next_step(x, y, n, m)
    for nx, ny in nextpoints:
        if dis[nx][ny] == -1 or dis[nx][ny] > (dis[x][y] + 1):
            dis[nx][ny] = dis[x][y] + 1
            explorer.append((nx, ny))

print dis
print dis[n][m]

for i in range(n + 1):
    print '\t'.join(map(lambda x: str(x), dis[i]))

t = {'year': '2013', 'month': '9', 'day': '30', 'hour': '16', 'minute': '45', 'second': '2'}

for k, v in t.items():
    t[k] = int(v)

print "%04d-%02d-%02d %02d:%02d:%02d" % (t['year'], t['month'], t['day'], t['hour'], t['minute'], t['second'])

L = [3, 3, 2]

diff = []
for i in range(len(L) - 1):
    diff.append(L[i + 1] - L[i])
if max(diff) * min(diff) >= 0:
    if min(diff) >= 0:
        print "UP"
    else:
        print "DOWN"
else:
    print "WRONG"

n = 5
limit = [1, 3, 2, 3, 4]
cost = [2, 3, 4, 1, 1]

ok = False
for start in range(n):
    sum = 0
    for j in range(n):
        sum += limit[(start + j) % n] - cost[(start + j) % n]
        if sum < 0:
            break
    if sum >= 0:
        ok = True
        break
if ok:
    print start
else:
    print -1

diff = 1
L_sorted = sorted(L)
for i in range(len(L_sorted) - 1):
    diff = min(diff, L_sorted[i + 1] - L_sorted[i])
if diff == 0:
    print "YES"
else:
    print "NO"

a = 1
b = 2
c = 3

L = sorted([a, b, c])
if L[0] + L[1] > L[2]:
    print "YES"
else:
    print "NO"

h = [0.9, 1.2, 1.22, 1.1, 1.6, 0.99]
up = False
cnt = 0
for i in range(len(h) - 1):
    if h[i + 1] > h[i]:
        up = True
    elif h[i + 1] < h[i] and up:
        up = False
        cnt += 1
print cnt

L = sorted([a, b, c])
if L[0] + L[1] > L[2]:
    if L[0] ** 2 + L[1] ** 2 > L[2] ** 2:
        print 'R'
    elif L[0] ** 2 + L[1] ** 2 == L[2] ** 2:
        print 'Z'
    else:
        print 'D'
else:
    print "W"

# 5652318

a = 5
n = 9
div = 20132013

binNum = bin(n)[:1:-1]
result = 1
mul = a
for i in binNum:
    if i == '1':
        result = (result * mul) % div
    mul = (mul * mul) % div
print result

div = 20132013
result = 1
i = 0
while i < n:
    result = (result * a) % div
    i = i + 1
print result

a = 1
b = 6
x = 1
y = 4

a = a % b

remain = []
quotient = []
while a not in remain:
    remain.append(a)
    a = a * 10
    quotient.append(a / b)
    a = a % b
loopstart = remain.index(a)

result = ''
for i in range(x, y + 1):
    if ((i - 1) < loopstart):
        result += str(quotient[i - 1])
    else:
        result += str(quotient[(i - 1 - loopstart) % (len(quotient) - loopstart) + loopstart])
print result

L = [2, -3, 3, 50, -1, -3, 7]
maxsum = 0
maxStart = 0
maxEnd = 0

cur_sum = 0
cur_start = 0
cur_end = 0
for i, v in enumerate(L):
    cur_sum += v
    if cur_sum <= 0:
        cur_sum = 0
        cur_start = i + 1
        cur_end = i + 1
    else:
        if maxsum < cur_sum:
            maxsum = cur_sum
            maxStart = cur_start
            maxEnd = i
print maxsum

print maxsum, L[maxStart:maxEnd + 1]

L = [2, -3, 3, 50]
max0 = 0
max1 = max(0, L[0])
for i in range(1, len(L)):
    maxv = max(max0 + L[i], max1)
    max0 = max1
    max1 = maxv
print max1

a = 3
b = 4

print "%.3f" % ((a ** 2 + b ** 2 + 0.0) ** 0.5)

n = 10

primes = [2, 3, 5]
for i in range(6, 10001):
    prime = True
    for v in primes:
        if i % v == 0:
            prime = False
    if prime:
        primes.append(i)
cnt = 0
for v in primes:
    if 2 * v < n:
        if (n - v) in primes:
            cnt += 1
print cnt

n = 4

if n <= 2:
    print 1
else:
    a = 1
    b = 1
    for i in range(n - 2):
        b += a
        a = b - a
        a %= 20132013
        b %= 20132013
    print b

a = 1
b = 1
for i in range(n - 2):
    b += a
    a = b - a
print b

w = [1, 2]
n = [2, 1]

maxw = 0
for W, N in zip(w, n):
    maxw += W * N
a = set([maxw])
for i in range(len(n)):
    tmp_a = a.copy()
    for j in range(1, n[i] + 1):
        for v in tmp_a:
            a.add(v - j * w[i])
print len(a)

a = 10
b = 10

lose = False
if (a + b) % 3 == 0:
    if abs(a - b) == 0 or abs(a - b) == 1:
        lose = True
if lose:
    print 'Loose'
else:
    print 'Win'

a = 10
b = 10

if a < b:
    a, b = b, a

m = [(0, 0)]  #
for i in range(1, a + 1):
    for j in range(i + 1):
        for x in m:
            if (i - x[0]) == (j - x[1]) or i == x[0] or j == x[1]:  # win
                break
            else:
                if (i,j) not in m:
                    m.append((i, j))
print m
print "Loose" if (a, b) in m else "Win"


n=2
n=n-1
a=[[1]]
for i in range(n):
    a.append([1])
    for j in range(i):
        a[i+1].append(a[i][j]+a[i][j+1])
    a[i+1].append(1)
for b in a:
    print " ".join(map(lambda x:str(x),b))



w=[2,5,11]
n=9
weights=[0]
for i in range(1,n+1):
    if i in w:
        weights.append(1)
    else:
        weightable=False
        for we in w:
            if i-we>0 and weights[i-we]==1:
                weightable=True
        if weightable:
            weights.append(1)
        else:
            weights.append(0)
if weights[n]==1:
    print "Yes"
else:
    print "No"













