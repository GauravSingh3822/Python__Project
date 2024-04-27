import random

lst = ["Rock", "Paper", "Scissor"]
while True:
    Computer_Count = 0
    User_Count = 0
    User_Choice = int(input('''
Game Start.....
1 Yes
2 No | Exit

         '''))
    if User_Choice == 1:
        for i in range(1, 6):
            User_Input = int(input('''
1 Rock 
2 Scissor
3 Paper

            '''))
            if User_Input == 1:
                User_Choice = "Rock"
            elif User_Input == 2:
                User_Choice = "Scissor"
            elif User_Input == 3:
                User_Choice = "Paper"
            Computer_Choice = random.choice(lst)
            if Computer_Choice == User_Choice:
                print("Computer Choice:-", Computer_Choice)
                print("User Choice:-", User_Choice)
                print("Game Draw")
                Computer_Count = Computer_Count + 1
                User_Count = User_Count + 1
            elif (User_Choice == "Rock" and Computer_Choice == "Scissor") or (
                    User_Choice == "Paper" and Computer_Choice == "Rock") or (
                    User_Choice == "Scissor" and Computer_Choice == " Paper"):
                print("Computer Choice:-", Computer_Choice)
                print("User Choice:-", User_Choice)
                print("You Win")
                User_Count = User_Count + 1
            else:
                print("Computer Choice:-", Computer_Choice)
                print("User Choice:-", User_Choice)
                print("Computer Win")
                Computer_Count = Computer_Count + 1
        if User_Count == Computer_Count:
            print("Final Game Draw....")
            print("User Score", User_Count)
            print("Computer Score", Computer_Count)
        elif User_Count > Computer_Count:
            print("User Won The Game....")
            print("User Score", User_Count)
            print("Computer Score", Computer_Count)
        else:
            print("Computer Won The Game....")
            print("User Score", User_Count)
            print("Computer Score", Computer_Count)
    else:
        break;