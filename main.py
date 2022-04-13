a, b = (int(i) for i in input().split())
pod = b
det = a
k = 1
while k > 0:
  if pod - det > 0:
    pod = pod - det
  else:
    print(det - pod)
    k = 0