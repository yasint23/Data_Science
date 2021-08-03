#Find the most frequent number and number of repeat in list.
seq = [1,7,3,4,3,0,3,6,3]
a= max(seq, key=seq.count)
b= seq.count(a)
print("Most frequent number is {} and {} times repeated".format(a,b))
              

#Comfortable words:###############################################################
left = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
right = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}
word = input("Enter a word: ")   
print((set(word) & left) !=set() and (set(word) & right) !=set())

#List remove
list =[3,5,6,9,12,24,33,50,88]
for i in list:
    if i%2 == 0:
        list.remove(i)
        print(list)  
        
#Exercise:###################################################################
name="yasin"
user = input("Enter user name: ")
if user == name:
    print("Hello," + user + "! The password is : W@12")
else:
    print("Hello," + user + "! See you later.")
    
#Exercise:####################################################################
age = int(input("How old are you?: "))

chronic = input("Do you have chronic disease?: Y/N:")

immune=input("Is your immune system too weak?: Y/N :")

if age>=75 and chronic=="Y" and immune=="Y":

    print("There is a risk of death")

else:

    print("There is no risk of death")
    
##########isArmstrong Number Exercise(need fix): #############################

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

   
#Exercise: Check Prime Number
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