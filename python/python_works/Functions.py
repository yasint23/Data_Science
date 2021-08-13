#Function:
def square_of_number(x):
    print(x**2)
square_of_number(4)

def square_of_number(x):
    return x**2
print(square_of_number(4))
###############################################################################
def square_of_number(x):
    print("Square of the number is:" + str(x**2))
square_of_number(5)
##############################################################################
def multiply(x, y):
    print(x*y)
multiply(3,4)
###############################################################################
def multiply(x, y=2):
    print(x*y)
multiply(3)
###############################################################################
def streetlight(temp,wet,battery):
    return (temp*wet)/battery
streetlight(30,25,70)
###############################################################################
x =[]
def add_list(y):
    x.append(y)
add_list("ali")
add_list("veli")
x    
###############################################################################
sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]
for i in sample_list:
    print(f"The type of {i} is {type(i)}")
################################################################################    
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name')
last_name = input('Enter your last name')

print('Your initials are: ' \
      + get_initial(first_name) \
      + get_initial(last_name))
        
#######################################################################
def longer(a, b):
    if  len(a) >= len(b):
        return a
    else:
        return b

print(longer('Richard', 'John'))   
    
    