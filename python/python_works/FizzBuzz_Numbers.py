def fizz_buzz_numbers(n):
    while n < 100:
        if n % 3 == 0 and n % 5 == 0:
            print("Fizz Buzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
        break
fizz_buzz_numbers(23)        

#Console:
#fizz_buzz_numbers(30)        
#Fizz Buzz

#fizz_buzz_numbers(9)        
#Fizz

#fizz_buzz_numbers(20)        
#Buzz

#fizz_buzz_numbers(23)        
#23