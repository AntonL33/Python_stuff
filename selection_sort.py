from random import random
from datetime import datetime

def populate_list(size):
    newlist = []
    for i in range(size):
        x = random() * 10000
        x = int(round(x))
        newlist.append(x)
    return newlist

def selection_sort(x):
    sorted = []
    for j in range(len(x) - 1):
        min = x[j]
        for i in range(j, len(x)):
            if x[i] < min:
                min = x[i]
        x.remove(min)
        x.insert(j, min)

x = populate_list(100)
print x
print '-----'
begintime = datetime.now()
selection_sort(x)
endtime = datetime.now()
print x
print 'time elapsed: {0}'.format(endtime - begintime)
