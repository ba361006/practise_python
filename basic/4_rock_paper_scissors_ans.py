import random

test_round = 0
youwin = 0
comwin = 0
fair = 0
while(test_round < 3):
    computer_choice = random.randrange(0,3)
    your_choice = int(input("Please Input [0:paper, 1:scissors, 2:rock] : "))
    print(f"Your choice: {your_choice}, Computer's choice: {computer_choice}")

    if (your_choice >= 3):
        print("Please Input 0,1 or 2")
        exit
        
    elif (computer_choice==your_choice):
        print("Nobody Win")
        test_round = test_round + 1
        fair = fair + 1

    elif (computer_choice==0 and your_choice==2) or (computer_choice==1 and your_choice==0) or (computer_choice==2 and your_choice==1):
        print("You Lose")
        test_round = test_round + 1
        comwin = comwin +1
    else:
        print("You Win")
        test_round = test_round + 1

        youwin = youwin +1


print("You Win : ",youwin)
print("Com Win : ",comwin)
print("Nobody Win : ",fair)