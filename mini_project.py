import random

def game_win(user , computer) :
    if user == computer:
      return None
    
#    Snake Vs Water
    if user == "s" and computer == "w":
      return True
    if user == "w" and computer == "s":
      return False

#    Water vs Gun
    if user == "w" and computer == "g":
      return True
    if user == "g" and computer == "w":
      return False
    
#    Gun Vs Snake
    if user == "g" and computer == "s":
      return True
    if user == "s" and computer == "g":
      return False

rand_no = random.randint(1,3)

print("Computer turn's : Snakes(s) , Water(w) , Gun(g)" )
if rand_no == 1 :
    computer = "s"
elif rand_no == 2 :
    computer = "w"
else :
    computer = "g"

user = input("your turn's : Snakes(s) , Water(w) , Gun(g) : ").lower()

result = game_win(user ,computer)
print(f"\n You chose :{user}")
print(f"\n computer chose :{computer}")

if result is None :
    print("Its Drow !")
elif (result):
    print("You Win !")
else :
    print("You Lose !")

