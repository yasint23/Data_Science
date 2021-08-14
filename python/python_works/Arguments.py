def who(first, last) : 
    print('Your first name is :', first)
    print('Your last name is :', last)

who('Marry', 'Bold')
######################################################################
def who(first, last) :
    print('Your first name is :', first)
    print('Your last name is :', last)

who(first='Yasin', last='Tuten')
#######################################################################
def fruiterer(*fruit) :
    print('I want to get :')
    for i in fruit :
        print('-', i)
        
fruiterer('orange', 'banana', 'melon', 'ananas')
########################################################################
def make_sentence(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for i in kwargs.values():
        result += i
    return result

print(make_sentence(a="I ", b="love ", c="Clarusway!"))


def unique_in_order(*args):
    for i in args:
        return list(dict.fromkeys(*args))
      
list = unique_in_order('AAAABBBCCDAABBB')
print(list)  


def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name')
last_name = input('Enter your last name')

print('Your initials are: ' \
      + get_initial(first_name) \
      + get_initial(last_name))
    

def texter(text1, text2, text3):
    print(text2,text3,text1)
    a = 'i'
    b = 'love'
    c = 'you'
texter(c,a,b) 
    

def texter(a,b,c):
    a = 'i'
    b = 'love'
    c = 'you'
    
texter(text1="you", text3="love", text2= "i")

###############################################################################
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
parrot(1000) 
#-- This parrot wouldn't voom if you put 1000 volts through it.
#-- Lovely plumage, the Norwegian Blue
#-- It's a stiff !
parrot(voltage=1000000, action="VOOOOM")
#-- This parrot wouldn't VOOOOM if you put 1000000 volts through it.
#-- Lovely plumage, the Norwegian Blue
#-- It's a stiff !
parrot("a million", "bereft of life", "jump")
#-- This parrot wouldn't jump if you put a million volts through it.
#-- Lovely plumage, the Norwegian Blue
#-- It's bereft of life !

def slicer(*num):
    evens=[]
    odds=[]
    for i in num:
        if i % 2 ==0:
           evens.append(i)
        else:
            odds.append(i)
            print("evens: ", evens)
            print("odds: ", odds)