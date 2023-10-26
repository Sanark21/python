print("welcome to the love calculator1")
name1 = input()
name2 = input()
combine = name1 + name2
lowercase = combine.lower()
checkt = lowercase.count("t")
checkr = lowercase.count("r")
checku = lowercase.count("u")
checke = lowercase.count("e")
firstnumber = checkt + checkr + checku + checke
checkl = lowercase.count("l")
checko = lowercase.count("o")
checkv = lowercase.count("v")
checke = lowercase.count("e")
secondnumber = checkl + checko + checkv + checke
score = int(str(firstnumber) + str(secondnumber))
if (score < 10) or (score > 90):
    print(f"your score is {score}, you are like coke and mentos")
elif (score <=40) and (score >=50):
    print(f"your score is {score}, you are  alright")
else:
    print(f"your score is {score}")       

