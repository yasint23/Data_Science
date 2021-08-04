#If_elif_else:
    
limit = 5000 
shop = input("Enter the name of shop: ")
income = int(input("Enter the income: "))

if income > limit:
    print("Congratulations: " + shop + " You got bonus.")
elif income < limit:
    print("Warning! You have less income:" + str(income))
else:
    print("Keep following!")
    
#######################################################################    
# for cycle:
students = ["ali","veli","fatma","ayse"]
for i in students:
    print(i)
##############################################################################
number = int(input('Please enter a number: '))
i=-1
while i < (number-1): 
    i +=1
    print(i**2)
##############################################################################       
a =[1,2,3,4]
b =[2,3,4,5]

ab =[]
for i in (range(0,len(a))):
    ab.append(a[i]*b[i])
ab   #[2,6,12,20]
##############################################################################        
# while cycle:
number = 2  
while number < 9: 
    number += 1  
    print(number)  #3,4,5,6,7,8,9
###############################################################################
iterable = [1, 2, 3, 4]

def square_of_iterable(x):
    print(x**2)
    
for i in iterable:
    square_of_iterable(i)
    
##############################################################################
times = int(input("How many times should I say 'I love you'"))

for i in range(times):
    print('I love you')        
        

##############################################################################
n = int(input("Tell us a number between 1-10"))
    
for i in range(11):
    print('{}x{} = '.format(n, i), n*i)    
        
##############################################################################        
text = ['one','two','three','four','five']
numbers = [1, 2, 3, 4, 5]
for x, y in zip(text, numbers):
    print(x, ':', y)   

###############################################################################     
print(*range(5,25,2))
#5 7 9 11 13 15 17 19 21 23

##############################################################################
who = ['I am ', 'You are ']
mood = ['happy', 'confident']
for i in who:
    for ii in mood:
        print(i + ii)
        
        
        
        
        
        
        
        
        
        
        