import random

#In this case, i will generate random numbers between 1000

#constants
TOTAL=10000
START=0
STOP=1000

def lastValue():
    sum=0
    while(sum<TOTAL):
        lastValueBefore=sum
        sum=sum+random.randint(START, STOP)
    return lastValueBefore
    

print(lastValue())