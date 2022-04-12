import random
dubl = 0
while dubl != 1:

  stock = []
  for i in range(7):
    for j in range(i, 7):
      stock.append([i, j])
  stock = [[i, j] for i in range(7) for j in range(i, 7)]

  player =[]
  comp = []

  i = 0
  for i in range(7):
    x = random.randint(1, len(stock)-1)
    player.append(stock[x])
    stock.pop(x)
    
  for i in range(7):
    x = random.randint(1, len(stock)-1)
    comp.append(stock[x])
    stock.pop(x)

  status_p = 0
  status_c = 0

  for i in range(7):
    summa = sum(player[i])
    if summa == 10:
      status_p = 1
    elif summa == 12:
      status_p = 2
    print(status_p)

  print()
  for i in range(7):
    summa = sum(comp[i])
    if summa == 10:
      status_c = 1
    elif summa == 12:
      status_c = 2
    print(status_c)
  if status_c and status_p == 0:
    dubl = 1
snake = 0

if status_c or status_p == 1:
  snake = [[5, 5]]
if status_c or status_p == 2:
  snake = [[6, 6]]
if status_p > status_c:
  status = "player"
if status_p < status_c:
  status = "computer"
  
print("Stock pieces:", stock)
print("Computer pieces:", comp)
print("Player pieces:", player)
print("Domino snake:", snake)
print("Status:", status)



# player = (random.choices(stock, k=7))
# print(player)
# print()
# comp = (random.choices(stock, k=7))
# print(comp)


