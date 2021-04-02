
import random       #importing random module
res=[1,2,3,4,5,6]
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
    
dice(res)                    #Calling a function dice
    
sh = random.randint(0,5)    #For random rolls
print(sh)

''' For generating a random dice'''

for i in range(sh):
    def random_shuffl_1(res):  
        res[1],res[2],res[3],res[4]=res[3],res[1],res[4],res[2]
        res1 = res
    random_shuffl_1(res)
    def random_shuffl_2(res):
        res[0],res[1],res[4],res[5]=res[4],res[0],res[5],res[1]
    random_shuffl_2(res)
    
dice(res)                    #Calling a function dice

def dice_down(down):
    
    ''' To roll down_wards'''
    
    down[2],down[1],down[4],down[3]=down[1],down[3],down[2],down[4]
    dice(down)
    print('down')

def dice_up(up):

    ''' To roll up_wards'''
    
    up[1],up[2],up[4],up[3]=up[2],up[4],up[3],up[1]
    dice(up)
    print('up')

def dice_left(left):

    ''' To roll left_side'''
    
    left[0],left[1],left[5],left[4]=left[1],left[5],left[4],left[0]
    dice(left)
    print('left')

def dice_right(right):

    ''' To roll Right_side'''
    
    right[4],right[5],right[1],right[0]=right[5],right[1],right[0],right[4]
    dice(right)
    print('right')

def dice_top(top):

    ''' To roll Top'''
    
    top[0],top[2],top[5],top[3]=top[2],top[5],top[3],top[0]
    dice(top)
    print('top_right')

def dice_bottom(bottom):

    ''' To roll Bottom'''
    
    bottom[0],bottom[2],bottom[5],bottom[3]=bottom[3],bottom[0],bottom[2],bottom[5]
    dice(bottom)
    print('bottom_left')
