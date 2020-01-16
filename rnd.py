import random

array = ['a','b','c','d',' ','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',' ',' ',' ',' ']
newArray=[]


#for loop
for n in range(999):
    randomNumber = random.choice(array)
    newArray.append(randomNumber)

print("".join(newArray))