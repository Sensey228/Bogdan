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
  erro = 1
  if next_one != "computer":
    while err == 1:
      err = 0
      erro = 1
      while erro == 1:
        try:
          kost = int(input())
          if kost < 0:
            kost_help = abs(kost)
            kost_help = kost_help - 1
          else:
            kost_help = kost - 1
          snake + [player[kost_help]]
          if kost == 0:
            kost = kost
        except ValueError:
          print("Только числовые значения")
          erro = 1
        except IndexError:
          print("Таких значений нету")
          erro = 1
        else:
          erro = 0
        try:
          stockr = random.randint(0, len(stock) - 1)
        except ValueError:
          print("В стоке не осталось костей")
          erro = 1
          if kost != 0:
            erro = 0

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
            if snake == 0:
              print("Вы проиграли :(")
              break
            else:
              print("""You can't put this piece in snake. Try again""")
              err = 1
      if len(player) >= abs(kost) and kost < 0 :
        kost = abs(kost)
        if player[kost - 1][1] == snake[0][0]:
            snake.insert(0, player.pop(kost - 1))
        elif player[kost - 1][0] == snake[0][0]:
            player[kost - 1][0], player[kost - 1][1] = player[kost - 1][1], player[kost - 1][0]
            snake.insert(0, player.pop(kost - 1))
        else:
            if snake == 0:
              print("Вы проиграли :(")
              break
            else:
              print("""You can't put this piece in snake. Try again""")
            err = 1

  
  if next_one == "computer":
    kost = input()
    while len(computer) == 0:
      weights = {
        0: 0,
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9,
        11: 10,
        12: 11,
        13: 12,
        14: 13,
        15: 14,
        16: 15,
        17: 16,
        18: 17,
        19: 18,
        20: 19,
        21: 20
      }
      for i in range(len(computer)):
        max_value = max(weights.values())
        weights[i] = sum(computer[i])
      print(weights)
      max_value = max(weights.values())
      
      rev_weights = {v: k for k, v in weights.items()}
      
      max_key = computer[rev_weights[max_value]]
    
    pilisos = False
    for i in range(len(computer)):
        if snake[-1][1] == computer[i][0]:
            snake.append(computer.pop(i))
            pilisos = True
            break
        elif snake[-1][1] == computer[i][1]:
            computer[i][0], computer[i][1] = computer[i][1], computer[i][0]
            snake.append(computer.pop(i))
            pilisos = True
            break
    if not pilisos:
      pilisos2 = False
      for i in range(len(computer)):
        if computer[i][1] == snake[0][0]:
          snake.insert(0, computer.pop(i))
          pilisos2 = True
          break
        elif computer[i][0] == snake[0][0]:
          computer[i][0], computer[i][1] = computer[i][1], computer[i][0]
          snake.insert(0, computer.pop(i))
          pilisos2 = True
          break
        if len(snake) == 0:
          print("У компьютера нету возможности ходитью. Игрок победил")
          break
        if not pilisos2:
          computer.append(stock.pop())
  if len(player) or len(computer) == 0:
    winner = 0

  if next_one == "computer":
    next_one = "player"
  else:
    next_one = "computer"
    
  if len(player) == 0:
    print("Игрок победил!")
    if len(snake) > 6:
      print(*snake[:3], '...', *snake[len(snake) - 3:], sep='')
    else:
      print(''.join(map(str, snake)))
    break
  if len(computer) == 0:
    print("Компьютер победил!")
    if len(snake) > 6:
      print(*snake[:3], '...', *snake[len(snake) - 3:], sep='')
    else:
      print(''.join(map(str, snake)))
    break