# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:25:22 2020

@author: personal
"""

def mean(lst):
    summ = 0
    for i in lst:
        summ += i
    return summ / n

def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def median(lst, n):
    lst_copy = lst.copy()
    sort(lst_copy)
    #print(lst_copy)
    if(n%2 == 0): # n is Even 
        x = lst_copy[n//2 - 1]
        y = lst_copy[n//2]
        return (x + y)/2
    else :  # n is Odd
        return lst_copy[n//2]

def mode(lst):
    freq = {}
    for i in lst :
        if(i in freq):
            freq[i] += 1
        else:
            freq[i] = 1           
    #print(freq)
    maximum = max(freq.values())
    mode = {}
    for i in freq:
        if(freq[i] == maximum):
            mode[i] = maximum
    
    return mode

def midrange(lst):
    lst_copy = lst.copy()
    sort(lst_copy)
    return (lst_copy[0]+lst_copy[-1]) / 2

def quartiles(lst):
    q2 = median(lst, n)
    
    lst_copy = lst.copy()
    sort(lst_copy)
    
    if(n%2 == 0): # n is Even     
        #lb = 0
        #ub = n//2 - 2
        lst_left = lst_copy[0: n//2 - 1]
        q1 = median(lst_left, n//2 - 1)
        
        #lb = n//2 + 1
        #ub = n
        lst_right = lst_copy[n//2 + 1:]
        q3 = median(lst_right, n//2 - 1)
    else :  # n is Odd
        lst_left = lst_copy[0: n//2]
        q1 = median(lst_left, n//2)
        
        lst_right = lst_copy[n//2 + 1:]
        q3 = median(lst_right, n//2)
        
    return q1, q2, q3

def standdev(lst):
    x = sum(lst) / n
    summ = 0
    for i in lst:
        summ += (i - x) ** 2
    return summ / n

f = open("data.txt", "r")

lst = []
for ele in f.readlines():
    lst.append(ele.split())

lst.pop()
#print(lst)

age = []
for ele in lst:
    age.append(int(ele[-1]))
#print(age)
    
n = len(age)
#print(n)

# Mean
mean = mean(age)
print("Mean : ",mean)

# Median
med = median(age, n)
print("Median : ",med)

# Mode
mode = mode(age)
print("Mode : ",end='')
for i in mode:
    print(i, end=' ')
print()

# Midrange
midrange = midrange(age)
print("Midrange : ",midrange)

# Quartiles
q1, q2, q3 = quartiles(age)
print("Quartiles : ",q1,q2,q3)

# IQR (Inter Quartile Range)
iqr = q3 - q1
print("IQR : ",iqr)

# Outlier
print("Outlier = ",1.5 * iqr)

# Standard Deviation
sd = standdev(age)
print("Standard Deviation : ",sd)

# Variance
import math
var = math.sqrt(sd)
print("Variance : ",var)









