
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







