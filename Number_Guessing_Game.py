import random
Computer_number=random.randrange(1,101)
User_Input=int(input("Enter Your Number:-"))
if User_Input>Computer_number:
    print("Computer Number",Computer_number)
    print("User Won The Game")
elif User_Input<Computer_number:
    print("Computer Number" ,Computer_number)
    print("Computer Won THe Game")
else:
    print("Computer Number",Computer_number)
    print("Tie Game")