from random import random
from datetime import datetime

def populate_list():
    newlist = []
    for i in range(100):
        x = random() * 10000
        x = int(round(x))
        newlist.append(x)
    return newlist

def bubblesort(x):
    for j in range(len(x) - 1):
        swapped = False
        for i in range(len(x) - 1 - j):
            if x[i] > x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
                swapped = True
        if not swapped:
            return x
        
x = populate_list()
print x

begintime = datetime.now()
print bubblesort(x)
endtime = datetime.now()

print 'time elapsed: {0}'.format(endtime - begintime)
