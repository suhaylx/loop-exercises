sum = 0 

for i in range(1,11):
  sum +=i
print(sum)


for i, o in enumerate("Hellloooo"):
  print(i, o)


for i, number in enumerate(list(range(100))):
  if number == 50:
    print(f"intex of {number} is ", i)