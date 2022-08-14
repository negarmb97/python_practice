import random
import re
import time

down_limit = int(input('Enter star number >'))
up_limit = int(input('Enter star number >'))
if down_limit>up_limit :
    down_limit,up_limit = up_limit,down_limit
origin_num = random.randint(down_limit,up_limit)
for i in range(0,3):
    num = int(input(f'Enter your number between {down_limit} , {up_limit} >'))
    if num == origin_num:
        print('damn yes!')
        break
    elif num!= origin_num and i<2:
        print('you have one more chance')
    i+=1
if num != origin_num :
    print(f'loser the number was {origin_num}')
time.sleep(10)