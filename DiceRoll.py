import roll_dice as r       #importing RollDice module  
COUNT = 0             #initializing count 
while True:
    roll = input("Enter your choice(d/u/l/r): ").lower() #Pick your choice
    if roll == 'down' or roll == 'd':
        r.dice_down(r.res)
        COUNT+=1
    elif roll == 'up'or roll =='u':
        r.dice_up(r.res)
        COUNT+=1
    elif roll == 'left'or roll =='l':
        r.dice_left(r.res)
        COUNT+=1
    elif roll == 'right'or roll =='r':
        r.dice_right(r.res)
        COUNT+=1
    elif roll == 'quit'or roll =='q':       #To quit
        print('\n')
        print("number of times dices roll: ",COUNT) 
        for i in r.list_all:
            r.dice(i)#To return all position of a dice
        print("latest position of dice")
        r.dice(r.res)
        print('Thanks for Participation, Visit Again!!!')
        break
    else:
        print('Invalid move\nPlease Make Correct Choice!!! ')








