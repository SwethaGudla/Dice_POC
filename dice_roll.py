'''importing rolldice module'''
import roll_dice
i=0
COUNT=0#initializing count
while True:
    roll = input("Enter your choice(d/u/l/r/q): ").lower() #Pick your choice
    if roll == 'd':
        roll_dice.dice_down(roll_dice.res)
        COUNT+=1
    elif roll == 'u':
        roll_dice.dice_up(roll_dice.res)
        COUNT+=1
    elif roll == 'l':
        roll_dice.dice_left(roll_dice.res)
        COUNT+=1
    elif roll == 'r':
        roll_dice.dice_right(roll_dice.res)
        COUNT+=1
    elif roll == 'q':#To quit
        print("number of times dices roll: ",COUNT)
        for i in roll_dice.list_all:
            roll_dice.dice(i)#To return latest position of a dice
        print("latest position of dice")
        roll_dice.dice(i)
        print('Thanks for Participation,Visit Again!!!')
        break
    else:
        print('Invalid move\nPlease Make Correct Choice!!! ')
