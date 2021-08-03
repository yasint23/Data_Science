#Function:
    
def square_of_number(x):
    print(x**2)
square_of_number(4)

def square_of_number(x):
    print("Square of the number is:" + str(x**2))
square_of_number(5)

def multiply(x, y):
    print(x*y)
multiply(3,4)

def multiply(x, y=2):
    print(x*y)
multiply(3)

def streetlight(temp,wet,battery):
    return (temp*wet)/battery
streetlight(30,25,70)

x =[]
def add_list(y):
    x.append(y)
add_list("ali")
add_list("veli")
x

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
  
# increase the salary %20 percent
salary =[3000,2000,4000,6000,5000]
def new_salary(x):
    print(x*20/100 + x)
        
for i in salary:
    new_salary(i)

#Exercise: 20% increase salary less than 3000 and 10% for more than 3000;
    
salary = [1000,2000,3000,4000,5000]

def new_salary1(x):
    print(x*10/100 + x)
    
def new_salary2(x):
    print(x*20/100 + x)
    
for i in salary:
    if i >= 3000:
        new_salary1(i)
    else:
        new_salary2(i)
        
# while cycle:
number = 2  
while number < 9: 
    number += 1  
    print(number)
#3,4,5,6,7,8,9

###############################################################################
answer = 44

question = 'What number am I thinking of?  '
print ("Let's play the guessing game!")

while True:
    guess = int(input(question))

    if guess < answer:
        print('Little higher')
    elif guess > answer:
        print('Little lower')
    else:  # guess == answer
        print('Are you a MINDREADER!!!')
        break
    
##############################################################################
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
        
        
        
        
        
        
        
        
        
        
        