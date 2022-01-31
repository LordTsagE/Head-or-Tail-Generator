#Write your code below this line 👇
#Hint: Remember to import the random module first
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
a = random.randint(0, 1)
if a == 1:
  print("Head")
elif a == 0:
  print("Tail")












