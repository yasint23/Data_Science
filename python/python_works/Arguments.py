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