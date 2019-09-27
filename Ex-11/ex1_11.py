print("How old are you?", end = " ")
age = input()
print("How tall are you", end = ' ')
height = input()
print("How much do you weight?", end = " ")
weight = input()
res = "So, you're {} years old, {} tall and {} heavy."
print(res.format(age,height,weight))
