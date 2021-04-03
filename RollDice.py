import random       #importing random module
res=[1,2,3,4,5,6]
list_all = []
def dice(x):
    
    ''' To print Dice'''
    
    print(f'         {x[1]}       ')
    print('    +---------+')
    print('   /|        /|')
    print(f'  / |   {x[2]}   / |')
    print(' +--+------+  +')
    print(f'{x[5]}|  /      |  /',f'{x[0]}')
    print(f' | /   {x[4]}   | /')
    print(' |/        |/')
    print(' +---------+')
    print(f'    {x[3]}  ')
print('Initial position of dice')    
dice(res)                    #Calling a function dice
    
sh = random.randint(0,5)    #For random rolls


''' For generating a random dice'''

for i in range(sh):
    def random_1(res):  
        res[1],res[2],res[3],res[4]=res[3],res[1],res[4],res[2]
        res1 = res
    random_1(res)
    
    def random_2(res):
        res[0],res[1],res[4],res[5]=res[4],res[0],res[5],res[1]
    random_2(res)
print('After rolling....')    
dice(res)                    #Calling a function dice

def dice_down(down):
    
    ''' To roll down_wards'''
    
    down[2],down[1],down[4],down[3]=down[1],down[3],down[2],down[4]
    dice(down)
    r = down.copy() 
    list_all.append(r)
    print('down')

def dice_up(up):

    ''' To roll up_wards'''
    
    up[1],up[2],up[4],up[3]=up[2],up[4],up[3],up[1]
    dice(up)
    r = up.copy() 
    list_all.append(r)
    print('up')

def dice_left(left):

    ''' To roll left_side'''
    
    left[0],left[1],left[5],left[4]=left[1],left[5],left[4],left[0]
    dice(left)
    r = left.copy()  
    list_all.append(r)
    print('left')

def dice_right(right):

    ''' To roll Right_side'''
    
    right[4],right[5],right[1],right[0]=right[5],right[1],right[0],right[4]
    dice(right)
    r = right.copy() 
    list_all.append(r)
    print('right')

