a, b, c = (int(i) for i in input().split())
k = 0
d = 0
while k < c:
  k = k + b
  d = d+1
print(a*d)