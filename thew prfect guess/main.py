import random
n =  random.randint(1,100)
a =-1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("guess the number :"))
    if (a > n):
        print("lower number please")
    else:
        print ("higher number")    

print (f"you have guessed the {n} in {guesses}    attempt ")        