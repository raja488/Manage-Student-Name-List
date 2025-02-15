number=int(input("please enter a number from 1 to 20 "))
if(number<=20 and number>0):
    for i in range(1,21):
        print(f"{number}*{i}={number*i}")
else:
    print(" ERROR , please enter a number from 1 to 20 ")