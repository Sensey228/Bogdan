import random

my_list = []
list = []
for i in range(100):
  x = random.randint(0, 10000)
  my_list.append(x)

for i in range(100):
  if my_list[i] % 5 == 0:
    list.append(my_list[i])
print(list)