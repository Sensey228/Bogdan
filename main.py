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
while winner == 0:

  print(100 * "=")
  print("Stock size:", len(stock))
  print("Computer pieces:", len(computer))
  snake2 = []
  snake1 = 0
  if len(snake) > 6:
    print(*snake[:3], '...', *snake[len(snake) - 3:], sep='')
  else:
    print(''.join(map(str, snake)))
  print()
  print("Your pices:")
  
  for i in range(len(player)):
    print(i+1,":",player[i])
    print()
  if (next_one) == "computer":
    print("Status: Computer is about to make a move. Press Enter to continue...")
  else:
    print("Status: It's your turn to make a move. Enter your command.")
    
  err = 1
  if next_one != "computer":
    while err == 1:
      try:
        kost = int(input())
        if kost < 0:
          kost_help = abs(kost)
          kost_help = kost_help - 1
        else:
          kost_help = kost - 1
        snake + [player[kost_help]]
      except ValueError:
        print("Только числовые значения")
      except IndexError:
        print("Таких значений нету")
      else:
        err = 0
      try:
        stockr = random.randint(0, len(stock) - 1)
      except ValueError:
        print("В стоке не осталось костей")
        err = 1
        if kost != 0:
          err = 0

      if kost == 0:
        stockr = random.randint(0, len(stock) - 1)
        player.append(stock[stockr])
        stock.pop(stockr)
        err = 0
      if kost > 0 and kost <= len(player):
        if player[kost - 1][0] == snake[-1][1]:
            snake.append(player.pop(kost - 1))
        elif player[kost - 1][1] == snake[-1][1]:
            player[kost - 1][0], player[kost - 1][1] = player[kost - 1][1], player[kost - 1][0]
            snake.append(player.pop(kost - 1))
        else:
            print("""You can't put this piece in snake. Try again""")
            err = 1
      if len(player) >= abs(kost) and kost < 0 :
        if player[kost - 1][1] == snake[0][0]:
            snake.insert(0, player.pop(kost - 1))
        elif player[kost - 1][0] == snake[0][0]:
            player[kost - 1][0], player[kost - 1][1] = player[kost - 1][1], player[kost - 1][0]
            snake.insert(0, player.pop(kost - 1))
        else:
            print("""You can't put this piece in snake. Try again1""")
            err = 1
  if next_one == "computer":
    kost = input()
    comp_rev = len(computer) * -1
    kost = random.randint(comp_rev, len(computer))
    while err == 1:
      try:
        stockr = random.randint(0, len(stock) - 1)
      except ValueError:
        kost = random.randint(comp_rev, len(computer))
        err = 1
      else:
        err = 0
        
    if kost == 0:
      stockr = random.randint(0, len(stock) - 1)
      computer.append(stock[stockr])
      stock.pop(stockr)
    if kost > 0:
      kost = kost - 1
      snake = snake + [computer[kost]]
      computer.pop(kost)
      
    if kost < 0:
      kost = kost * -1
      kost = kost - 1
      snake = [computer[kost]] + snake
      computer.pop(kost)
  if len(player) or len(computer) == 0:
    winner = 0

  if next_one == "computer":
    next_one = "player"
  else:
    next_one = "computer"
    
  if len(player) == 0:
    print("Игрок победил!")
    break
  if len(computer) == 0:
    print("Компьютер победил!")
    break