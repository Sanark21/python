counta = 0
countb = 0
for i in range(1,101):
    if(i%2==0):
        counta = counta +1
    if(i%2!=0):
        countb = countb +1
print(f" add{counta}")
print(f" even{countb}")
