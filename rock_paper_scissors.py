import random
import time

pc_counter = 0
user_counter = 0
choices = ['R','P','S']
while 1<2:
    user = str(input('enter your choice between R P S >'))
    user = user.upper()
    print(user)
    if not user in choices:
        print('f{your choice should be in R,P,S honey}')
        continue

    # if not re.match('sSrRpP',user):
    #     print('f{your choice should be in R,P,S}')
    #     continue

    pc = random.choice(choices)
    print(f'pc choice is {pc}')
    if user.upper() == pc :
        print('{TIE! try again}')
    elif user.upper()=='R' and pc =='P' : 
        print('{LOSS BABY}')
        pc_counter = pc_counter +1
    elif user.upper()=='P' and pc=='S' :
        print('{LOSS BABY}')
        pc_counter = pc_counter +1
    elif user.upper()=='S' and pc=='R' :
        print('{LOSS BABY}')
        pc_counter = pc_counter +1
    else :
        print('{WIN BABY}')
        user_counter = user_counter +1
    if user_counter == 3 :
        print('{user wins}')
        time.sleep(10)
        break
    elif pc_counter == 3 : 
        print('{pc wins}')
        time.sleep(10)
        break
    else :
        continue



def get_winner_for_each_step(user,pc,pc_counter,user_counter):
    results={'RP':'c' ,'PS':'c' ,'SR':'c' ,'PP':'t','RR':'t','SS':'t','PR':'u','SP':'u','RS':'u'}
    choice = user+pc
    winner = results[choice]
    match winner :
        case 'u':
            user_counter = user_counter+1,
        case 'c':
            pc_counter = pc_counter+1,

    return count_winner_round(pc_counter,user_counter)

def count_winner_round(pc_counter,user_counter):
    times = {'pc_counter':3,'user_counter':3}

