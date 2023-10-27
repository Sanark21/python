name_string =input("please enter names and separated by comma and space \n")
name = name_string.split(",")
lenth = len(name)

import random
choose_random = random.randint( 0, lenth -1)
select = name[choose_random]
print(f"{select} is buy a meal today")