flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers)
count2 = 0

while count1>0 :
    print(flowers[count2])
    count1 -= 1
    count2 += 1 
##############################################################################
if b > max:
    max = a
    max = b
    print(max)

###############################################################################
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for day in range(len(weekdays)):
    
    print('Day', day+1, ':', weekdays[day])
##############################################################################   
sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]
for i in sample_list:
      print("The type of", i+1 + "is", type(sample_list[i])   
   
    
a =[1,2,3,4]
b =[2,3,4,5]
import numpy as np
a =np.array(a)
b =np.array(b)
a*b   #array([ 2,  6, 12, 20])    
##############################################################################   
list1 =[1,2,3,4,5]
for i in list1:
    print(i + 10)   #11,12,13,14,15 
    
    
list(map(lambda x: x+10, list1))  #11,12,13,14,15  
###############################################################################
list2 =[1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x % 2 == 0, list2)) #[2, 4, 6, 8, 10]
###############################################################################
a = 10
b = "2"

a / b

try:
    print(a/b)
except TypeError:
    print("Number and string problem") 
##############################################################################
from functools import reduce
a = [1,2,3,4]
reduce(lambda a,b: a*b, a)   #24

###############################################################################
liste = [1,2,3,4,5]
A = []
for i in liste:
    A.append(i**2)
print(A)

list(map(lambda x: x**2, liste))    
###############################################################################
def sum(a,b):
    return a+b 
sum(4,3)

new_sum = lambda a,b: a + b 
new_sum(8,3)

mixed_list = [('b',3),('a',8),('d',12),('c',1)]
sorted(mixed_list, key =lambda x: x[1]) #[('c', 1), ('b', 3), ('a', 8), ('d', 12)]
##############################################################################    
    
    