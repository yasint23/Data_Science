num = int(input("Enter a number: "))

order = len(str(num))

sum = 0

result = num
while result > 0:
   digit = result % 10
   sum += digit ** order
   result //= 10

if num == sum:
   print(num,"is an Armstrong number")
   
elif num != sum:
     print(num,"is not an Armstrong number")
    
else:
   print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    
######################################################################################
while True :
    number = input("enter a positive integer number : ")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, " is invalid entry. Enter valid input.!")
    elif int(number) >= 0 :
        for i in range(digits) :
            summ = summ + int(number[i]) ** digits
        if summ == int(number) :
            print(number, "is an Armstrong Number.")
            break
        else :
            print(number, "is not an Armstrong Number. Sorry.")
            break
  
