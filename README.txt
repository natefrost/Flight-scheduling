Personal project I worked on at Kite Systems inc. during August 2020 to learn about algorithms and linear programming.

Contains two data sets = fra.txt and nra.txt, which are sets of flights (departures and arrivals), including information about them.

Goal is to match arrivals with departures to minimize costs.

Current data sets have 1:1 ratio of arrivals to departures, but both solutions work with N:1 arrivals to departures ratios. (theres an unused variable with max pilots per departure)

SOLUTION 1:

Base solution for the problem - explores every solution using recursion and sorting at every step.
Tested to work correctly (performed on 25 flights), however takes an incredible amount of time, which goes up exponentially with every added flight.
Extremely inefficient solution, which wouldnt be able to match the flights one to each other given a whole week.

SOLUTION 2:

Makes use of linear programming - needs lpsolve and lpmaker packages installed.

Elegant solution, which takes the data sets and plots the needed variables (including prices) into a large matrix. 
lpsolve then calculates the connections between the flights on its own, and takes very little time once the matrix is used.
Infinitely more elegant and efficient than solution 1, however still has the issue of having to plot the matrix.

Given a very very large data set, this could prove to be inefficient, however usually the plan for the flights would not go the far.
(The larger of the current two data sets is for 2 months and calculates instantly).