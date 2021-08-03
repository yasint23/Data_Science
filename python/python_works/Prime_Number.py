num = int(input("Enter number: "))

if num > 1:
  
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
  
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is not a prime number")
    
#####################################################################################
saved_amount = int(input('Please enter your saved amount: '))
ps4_price = 200
if saved_amount <= ps4_price/2:
    print("You must save more, keep saving!")
elif saved_amount > ps4_price/2:
    print("You saved more than half, keep saving!")
else:
    print("Yippee! You can buy your PS4")
    


def calculator(a,b,opr):
    if opr == "+":
        print(a + b)
    elif opr == "-":
        print(a - b)
    elif opr == "/":
        print( a / b)
    elif opr == "*":
        print(a * b)
    else:
        print("Enter valid argument")
    
    
def absolute_value(num):
    """This function gives absolute value 
of the entered number."""
    if num >= 0 :
        return num
    else:
        return -num
  
    
    
    
    
    
    
    
    
    
    