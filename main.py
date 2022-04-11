import random

stock = []
for i in range(7):
  for j in range(i, 7):
    stock.append([i, j])

stock = [[i, j] for i in range(7) for j in range(i, 7)]

player =[]
comp = []


while len(stock) > 21:
  x = random.randint(1, len(stock))
  player.append(stock[x])
  stock.pop(x)
while len(stock) > 14:
  x = random.randint(1, len(stock))
  comp.append(stock[x])
  stock.pop(x)

print(stock)  
print()
print(player)
print()
print(comp)


# player = (random.choices(stock, k=7))
# print(player)
# print()
# comp = (random.choices(stock, k=7))
# print(comp)


