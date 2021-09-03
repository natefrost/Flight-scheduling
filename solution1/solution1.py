
# -*- coding: utf-8 -*-
    
from datetime import datetime
import copy

#base variables = c1 = price per time in hotel, c2 = price for transport between two airports
c1 = 1
c2 = 500

datalist = []

with open('fra.txt') as f:
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
    

"""
testflight = departures[-3]
print (testflight.time, testflight.id)         
for i in arrivals:
    if time_diff(testflight, i) < 0:
        pass
    else:
        print(i.time)
        print(flight_price(testflight, i))




departures.reverse()
"""

  

smalldeps = []

for a in range(16):
    
    smalldeps.append(departures[a])



def solution(total, deps, arrs, count, flightdict = {}):
    

    if len(deps) == 0:
        return (total, flightdict) 
    else:
        
        curr = deps[0]
    
        available = []
            
        for arr in arrs:
            
            timediff = time_diff(curr, arr)
            if (timediff > 660 and timediff < 10080):               
                available.append(arr)   
                
        solutions = []
        
        if available != []: #### ----------------------------
            
            for arr in available:
                permtot = flight_price(curr, arr) + total
                arrcopy = [i for i in arrs]
                fdcopy = copy.deepcopy(flightdict)  
                fdcopy[arr] = curr
                arrcopy.remove(arr)
                
                x = solution(permtot, deps[1:], arrcopy, count, fdcopy)
                
                solutions.append(x)
            
            sortlutions=sorted(solutions, key=lambda x:x[0])
            
            #print(sortlutions)
            
            return sortlutions[0]
        else:
            
        
            if len(deps) != 1:
                return solution(total, deps[1:], arrs, count, flightdict)
            else:
                return solution(total + 99999999, deps[1:], arrs, count, flightdict)
    
    
#print(solution(0, smalldeps, arrivals, {}))

y = 0

x = (solution(0, smalldeps, arrivals, y,{}))

for key in x[1]:
    
    print(key.l + " " + key.no + " " + str(key.time) + " - " + str(x[1][key].time) + " " + x[1][key].no + " " + x[1][key].l)

print("Min total price is " + str(x[0]))



            
            
            
            

            
            
            
            
    
    
    
    
        
        
    
    
    
    
    



"""


VN0031 = datetime(2019, 6, 3, 4, 40)

VN0030 = datetime(2019, 6, 3, 12, 35)

difference = VN0031 - VN0030

realdiff = (difference.days*24*60) + (difference.seconds/60)

print(realdiff)
"""


