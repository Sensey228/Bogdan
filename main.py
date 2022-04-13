from time import perf_counter
num = int(input())
num = num 
time = 1000000000
for i in range(1, num):
  if num % i == 0:
    print(i)
print(num)
x = perf_counter()
print(x)