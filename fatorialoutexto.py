import math
x=input()
if x.isnumeric():
  y=int(x)
  print(math.factorial(y))
elif x=="ufabc":
  print("minha universidade")
else:
  print(x)