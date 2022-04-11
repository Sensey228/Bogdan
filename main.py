
# 0 — 15,527: 0% tax

# 15,528 — 42,707: 15% tax

# 42,708 — 132,406: 25% tax

# 132,407 and more: 28% tax

# The tax for 99999 is 25%. That is 25000 dollars!

num = int(input())
if num <= 15527:
  k = (0)
elif num >= 15528 and num <= 42707:
  k = int(0,15)

g = num * k
proz = k * 100
print("The tax for", num,"is",proz ,". That is",g,"dollars")