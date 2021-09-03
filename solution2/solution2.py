
from lpsolve55 import *
from lp_maker import *
import lp_solve
import array as arr
import numpy as np
# -*- coding: utf-8 -*-

from constraint import *

from datetime import datetime
import copy

c1 = 1
c2 = 500

datalist = []

with open('C:/Users/kawai/OneDrive/Desktop/aiofioaf/fra.txt') as f:
    for line in f:
        split = line.strip().split(' ')

        del split[0]
        if split != []:
            del split[2]
            datalist.append(split)
        

for flight in datalist:
        
    x = '\"'
    
    for i in range(len(flight)):
        
        firstindex = flight[i].find(x)
        lastindex = flight[i].rfind(x)
        
        newinf = (flight[i][firstindex+1:lastindex])
        flight[i] = newinf
        

class Flight:
    def __init__(self, time, location, specific, ID, flightNo):
        self.time = time
        self.l = location
        self.t = specific
        self.id = ID
        self.no = flightNo
        self.crewseats = 1
    
    
    
def convert_time(x):
    split = x.split('-')
    p = split[2].split('T')
    q = p[1].split(':')
    split[2] = p[0]
    split.append(q[0])
    split.append(q[1])
    
    return datetime(int(split[0]), int(split[1]), int(split[2]), int(split[3]), int(split[4]))

flightlist = []



def create_flight(x, y):

    y = Flight(convert_time(x[0]), x[1], x[3], x[4], x[2])
    flightlist.append(y)
    

    

for i in range(len(datalist)):
    z = "flight" + str(i+1)
    
    create_flight(datalist[i], z)
    


def display_flight(f):
    
    display = {f.id:[f.time, f.l, f.t, f.no]}
    return display

arrivals = []
departures = []

for flight in flightlist:
    if flight.t == "Arrival":
        arrivals.append(flight)
    else:
        departures.append(flight)
        
arrcopy = [i for i in arrivals]

def flight_price(x, y):
    price = 0
    if x.t == "Arrival":
        x, y = y, x
    timediff = time_diff(x, y)
    price += timediff * c1 #price of hotel in frankfurt
    if x.l != y.l:
        price += c2
    return price

def time_diff(x, y):
    
    difference = x.time - y.time
    realdiff = (difference.days*24*60) + (difference.seconds/60)
    return int(realdiff) #returns diff in minutes

comblist = []

for dep in departures:
    for arr in arrivals:
        timediff = time_diff(dep, arr)
        if (timediff > 660 and timediff < 10080):               
            comblist.append((arr, dep)) 


#for pair in comblist:
    #print(pair[0].id, pair[1].id)
    

flightarray = []

for i in range(2,len(departures)):
    x = []
    for pair in comblist:
        if departures[i] in pair:
            
            x.append(1)
        else:
            x.append(0)
    flightarray.append(x)


for j in range(len(arrivals)):
    y = []
    for pair in comblist:
        if arrivals[j] in pair:
            y.append(1)
        else:
            y.append(0)
    flightarray.append(y)


cost_arr = [flight_price(i[0], i[1]) for i in comblist]

flightarray.append(cost_arr)


fl = np.array(flightarray)

#print(fl)

m = len(comblist)

n = len(flightarray)

f = cost_arr
a = []

splitlist = [[] for i in range(len(departures) - 2)]

z = 0
curr = comblist[0][1]
for i in comblist:
    if i[1] == curr:
        splitlist[z].append(i)
    else:
        curr = i[1]
        z += 1
        splitlist[z].append(i)
#print(splitlist)


curr2 = 0

for i in splitlist:
    x = [0 for flight in cost_arr]
    for duo in i:
        x[curr2] = 1
        curr2 += 1
    a.append(x)

for i in arrivals:
    x = [0 for pair in comblist]
    for pair in range(len(comblist)):
        if i in comblist[pair]:
            x[pair] = 1
    a.append(x)

b = [1 for i in a]
e = [0 for i in b]

lp = lp_maker(f, a, b, e, None, None, None, None, 1)

lpsolve('solve', lp)

lpsolve('get_objective', lp)

flightchoice = (lpsolve('get_variables', lp)[0])

lens = 0
total_price = 0
for i in range(len(flightchoice)):
    if flightchoice[i] > 0:
        arrival = comblist[i][0]
        dep = comblist[i][1]
        total_price += flight_price(arrival, dep)
        print(arrival.l + " "+ str(arrival.time) + " - " +   str(dep.time) + " " + dep.l)
        lens += 1
    
print(total_price)

print(lens)