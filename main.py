time = int(input())

for1 = time // 17
for2 = time // 13

if time % 17 != 0:
  for1 = time // 17 + 1
  
if time % 13 != 0:
  for2 = time // 13 + 1

k = for1 + for2
for i in range(for1):
  for b in range(for2):
      if 13 * b == 17 * i:
        k = k - 1
print(k)


