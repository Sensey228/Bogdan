from random import shuffle, randint


def give(full):
    stock = full[:]
    pgive = []
    cgive = []
    start = 0
    while [5, 5] not in stock[:14] and [6, 6] not in stock[:14]:
        shuffle(stock)
    for double in [[6, 6], [5, 5]]:
        if double in stock[:14]:
            snake = [stock.pop(stock.index(double))]
    pgive = stock[:6]
    cgive = stock[6:13]
    if randint(0, 1):
        pgive, cgive = cgive, pgive
    if len(cgive) < len(pgive):
        start = 1
    stock = stock[13:]
    return stock, pgive, cgive, snake, start

def game():
    while True:
        print('Stock pieces:', len(stock))
        print('Computer pieces:', len(cgive))
        if len(snake) > 7:
            print(*snake[:3], '...', *snake[len(snake) - 3:], sep='')
        else:
            print(*snake, sep='')
        print('Your pieces:')
        for i, piece in enumerate(pgive, start=1):
            print(i, piece)
        if snake[0][0] == snake[-1][1] and sum(snake, []).count(snake[0][0]) == 8 and len(snake) != 1:
            print("""Status: The game is over. It's a draw!""")
            break
        elif len(pgive) == 0:
            print('Status: The game is over. You won')
            break
        elif len(cgive) == 0:
            print('Status: The game is over. The computer won')
            break
        else:
            turn()

def player_d():
    try:
        num = int(input())
    except ValueError:
        print('Invalid input. Please try again.')
        player_d()
    else:
        if num > 0:
            if num > len(pgive):
                print('No piece. Please try again.')
                player_d()
            else:
                if pgive[num - 1][0] == snake[-1][1]:
                    snake.append(pgive.pop(num - 1))
                elif pgive[num - 1][1] == snake[-1][1]:
                    pgive[num - 1][0], pgive[num - 1][1] = pgive[num - 1][1], pgive[num - 1][0]
                    snake.append(pgive.pop(num - 1))
                else:
                    print("""You can't put this piece in snake. Try again""")
                    player_d()
        elif num == 0:
            pgive.append(stock.pop())
        else:
            num = abs(num)
            if num > len(pgive):
                print('No piece. Please try again.')
                player_d()
            else:
                if pgive[num - 1][1] == snake[0][0]:
                    snake.insert(0, pgive.pop(num - 1))
                elif pgive[num - 1][0] == snake[0][0]:
                    pgive[num - 1][0], pgive[num - 1][1] = pgive[num - 1][1], pgive[num - 1][0]
                    snake.insert(0, pgive.pop(num - 1))
                else:
                    print("""You can't put this piece in snake. Try again""")
                    player_d()

def computer_d():
    enter = input()
    if enter != '':
        print('Invalid input. Please try again.')
        computer_d()
    else:
        flag = False
        for i in range(len(cgive)):
            if snake[-1][1] == cgive[i][0]:
                snake.append(cgive.pop(i))
                flag = True
                break
            elif snake[-1][1] == cgive[i][1]:
                cgive[i][0], cgive[i][1] = cgive[i][1], cgive[i][0]
                snake.append(cgive.pop(i))
                flag = True
                break
        if not flag:
            flag2 = False
            for i in range(len(cgive)):
                if cgive[i][1] == snake[0][0]:
                    snake.insert(0, cgive.pop(i))
                    flag2 = True
                    break
                elif cgive[i][0] == snake[0][0]:
                    cgive[i][0], cgive[i][1] = cgive[i][1], cgive[i][0]
                    snake.insert(0, cgive.pop(i))
                    flag2 = True
                    break
            if not flag2:
                cgive.append(stock.pop())

def turn():
    global start
    if start:
        print("""Status: It's your turn to make a move. Enter your command""")
        start -= 1
        player_d()
    else:
        print('Status: Computer is about to make a move. Press Enter to continue')
        start += 1
        computer_d()

full = [[i, j] for i in range(7) for j in range(i, 7)]
stock, pgive, cgive, snake, start = give(full)
game()


# from time import perf_counter

# def get_primes(n):
#   primes = [2, 3]
#   for i in range(5, n + 1):
#     if i % 6 in (1, 5):
#       prime = True
#       for j in range(2, int(i ** 0.5) + 1):
#         if not i % j:
#           prime = False
#           break
#       if prime:
#         primes.append(i)
#   return primes


# n = 100_000
# start = perf_counter()
# primes = get_primes(n)
# print(perf_counter() - start)
# print(primes)


# def get_prime_divs(n):
#   res = []
#   for i in range(2, int(n ** 0.5) + 1):
#     while not n % i:
#       if not i in res:
#         res.append(i)
#       n //= i
#     if n < i:
#       break
#   if n > 1:
#      res.append(n)
#   return res

# n = 999_999_999
# start = perf_counter()
# print(get_prime_divs(n))
# print(perf_counter() - start)