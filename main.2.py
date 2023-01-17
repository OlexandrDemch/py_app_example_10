import random
num = int(input('Enter the no. of random integers:'))
r_lst = []
for i in range(num):
    while new_no := random.randint(100, 999):
        if new_no in r_lst:
            new_no = random.randint(100,999)
        else:
            r_lst.append(new_no)
            break
            print(r_lst)