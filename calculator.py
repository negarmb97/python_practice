import random

def addition():
    print(f'addition')
    n = float(input('enter your number>>'))
    sum=0
    t =0
    while n!=0:
        sum = sum + n
        t=+1
        n = float(input('enter another number>>'))
    print(f'your addition result is {sum}')
    return sum,t

def subtraction():
    print(f'subtraction')
    n = float(input('enter your number>>'))
    sub=0
    t=0
    while n!=0:
        sub = sub-n
        t=+1
        n = float(input('enter another number>>'))
    print(f'suntraction is {sub}')
    return sub,t

def multipition():
    print(f'multipition')
    n = float(input('enter your number>>'))
    mul=0
    t=0
    while n!=1:
        mul = mul * n
        t=+1
        n = float(input('enter another number>>'))
    print(f'multipication is {mul}')
    return mul,t

def division():
    print(f'division')
    n = float(input('enter your number>>'))
    div=0
    t=0
    while n!=1:
        div = div / n
        t=+1
        n = float(input('enter another number>>'))
        if n==0:
            print(f'ZERO is not valid !!')
            break
    print(f'division is {div}')
    return div,t


def average():
    print(f'average')
    n = float(input('enter your number>>'))
    sum=0
    t =0
    while n!=0:
        sum = sum + n
        t=+1
        n = float(input('enter another number>>'))
    avg = sum /t
    print(f'your addition result is {avg}')
    return avg,t
    
while True:
    print(f'write a for addition')
    print(f'write s for suntraction')
    print(f'write m for multiption')
    print(f'write d for division')
    print(f'write v for average')
    print(f'write q for quite')
    char = input(f'type your operation >>>>')
    match char:
        case 'a': addition()
        case 's': subtraction()
        case 'm': multipition()
        case 'd': division()
        case 'v':average()
        case 'q':break
