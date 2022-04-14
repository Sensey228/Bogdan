from random import randint, shuffle
import random

stock = [[i, j] for i in range(7) for j in range (i, 7)]
doubles = stock[:-4:-2]
on_hands = 7

while not any ([double in stock[:on_hands * 2] for double in doubles]):
  shuffle(stock)

for double in doubles:
  if double in stock[ :on_hands * 2]:
    snake = stock.pop(stock.index(double))
    break

computer, player = stock[:on_hands - 1], stock[on_hands - 1:on_hands * 2 -1]
if randint(1, 2) == 2:
  player, computer = computer, player

stock = stock[on_hands * 2 -1:]

next_one = 'computer' if len(computer) > len(player) else ' player'

print('   Stock pieces: {}\n\
Computer pieces: {}\n\
  Player pieces: {}\n\
   Domino snake: [{}]\n\
         Status: {}'.\
            format(stock, computer, player, snake, next_one))

snake = [snake]
winner = 0
snake2 = [[ ]]
while winner == 0:
  
  print(100 * "=")
  print("Stock size:", len(stock))
  print("Computer pieces:", len(computer))
  print(' '.join(map(str, snake)))
  print()
  print("Your pices:")
  
  for i in range(len(player)):
    print(i+1,":",player[i])
    print()
  if (next_one) == "computer":
    print("Status: Computer is about to make a move. Press Enter to continue...")
  else:
    print("Status: It's your turn to make a move. Enter your command.")
  erro = 1
  err = 1
  if next_one != "computer":
    while err == 1:
      try:
        kost = int(input())
      except ValueError:
        print("Только числовые значения")
      else:
        err = 0
    
    if kost == 0:
      stockr = random.randint(0, len(stock))
      player.append(stock[stockr])
    if kost > 0:
      while erro == 1:
          try:
            kost = kost - 1
            snake = snake + [player[kost]]
          except IndexError:
            print("Таких значений нет")
            kost = int(input())
          else:
            erro = 0
      player.pop(kost)
      print(' '.join(map(str, snake)))
    if kost < 0:
      kost = kost * -1
      kost = kost - 1
      snake = [player[kost]] + snake
      player.pop(kost)
      print(' '.join(map(str, snake)))

  if next_one == "computer":
    kost = input()
    comp_rev = len(computer) * -1
    kost = random.randint(comp_rev, len(computer))
    if kost == 0:
      stockr = random.randint(0, len(stock))
      computer.append(stock[stockr])
    if kost > 0:
      kost = kost - 1
      snake = snake + [computer[kost]]
      computer.pop(kost)
      print(' '.join(map(str, snake)))
      
    if kost < 0:
      kost = kost * -1
      kost = kost - 1
      snake = [computer[kost]] + snake
      computer.pop(kost)
      print(' '.join(map(str, snake)))
  if len(player) or len(computer) == 0:
    winner = 0

  if next_one == "computer":
    next_one = "player"
  else:
    next_one = "computer"
  # if len(snake) >= 7:
  #   for i in range(3):
  #     snake2 = snake2 + snake[i]
  #   for i in range(3):
  #     snake2 = snake2 + snake[len(snake) - 4 + i]
  # print(' '.join(map(str, snake2)))
if len(player) == 0:
  print("Игрок победил!")
if len(computer) == 0:
  print("Компьютер победил!")
  