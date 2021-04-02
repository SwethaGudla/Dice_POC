import RollDice as r       #importing RollDice module
        
count=0             #initializing count 
while True:
    roll = input("Enter your choice(d/u/l/r/q): ").lower() #Pick your choice
    
    
    if roll == 'd':
        r.dice_down(r.res)
        count+=1
    elif roll == 'u':
        r.dice_up(r.res)
        count+=1
    elif roll == 'l':
        r.dice_left(r.res)
        count+=1
    elif roll == 'r':
        r.dice_right(r.res)
        count+=1
    elif roll == 'q':       #To quit
        print('\n')
        print("number of times dices roll: ",count)
        r.dice(r.res)       #To return latest position of a dice
        print('Thanks for Participation, Visit Again!!!')
        break
    else:
        print('Invalid move\nPlease Make Correct Choice!!! ')







