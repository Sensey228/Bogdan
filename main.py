import random

stock = []
for i in range(7):
  for j in range(i, 7):
    stock.append([i, j])

stock = [[i, j] for i in range(7) for j in range(i, 7)]
print(stock)
print()



player = (random.choices(stock, k=7))
print(player)
print()
comp = (random.choices(stock, k=7))
print(comp)


