#binary search
nums = input(f"Enter search numbers>")
lst=list(map(int,nums.strip().split()))

number = int(input(f'Enter your search value>'))
lst.sort()
# print(lst)
last = len(lst)-1
first = 0
is_found = False
while first<=last and is_found==False :
    mid = (first + last) // 2
    if lst[mid]==number:
        is_found = True
        print(f'number {number} found !')
        break
    elif lst[mid] < number:
        first = mid+1
    else:
        last = mid-1
if is_found==False:
    print(f'there is no {number} in set !')