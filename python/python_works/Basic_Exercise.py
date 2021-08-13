i=0
while i <= 10:
    print(i)
    i +=1
    

for row in range(1,6):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")

sum1 = 0
n = int(input("Please enter number "))
for i in range(1, n + 1, 1):
    sum1 += i
print("Sum is: ", sum1)


n = int(input("Enter number"))
i=0
while i < 10:
    i +=1
    print(n*i)
    

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if (i > 150):
        break
    if(i % 5 == 0):
        print(i)


number = input("Enter number")
k = 0
for i in number:
    k += 1
print(k)

n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()

i=-10
while i < 0:
    print(i)
    i +=1
    
for i in range(5):
    print(i)
else:
    print("Done")

start = 25
end = 50

for n in range(25,50):
    for i in range(2,int(end/2)+1):
        if n % i != 0:
            print(f"Prime numbers between {start} and {end} are")
        return n
            
n1= int(input("Enter number1"))
n2= int(input("Enter number2"))

if n1*n2 >1000:
    print(n1+n2)
else:
    print(n1*n2)
  

def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
        previousNum = i

print("Printing current and previous number sum in a given range(10)")
sumNum(10)    
   

def display_even_letter(letter):
    for i in range(0,len(letter)-1, 2):
        print(letter[i])
        
letter = "pynative" 
display_even_letter(letter)
      

def removeChars(str, n):
  return str[n:]

print(removeChars("pynative", 4))

def givenlist(liste):
    a= liste[0]
    b= liste[-1]
    if (a == b):
        return True
    else:
        return False

liste = [10, 20, 30, 40, 50]
print("result is", givenlist(liste))


def div_five(list):
    for i in list:
        if i % 5 == 0:
            print(i)
list = [10, 20, 33, 46, 55]
div_five(list)
    

str = "Emma is good developer. Emma is a writer"
number_rep = str.count("Emma")
print("Emma repeat",number_rep,"times")
            

count = 4
string = "* * * * *"
list1 = string.split(" ")
for i in range(1, 6):
    print("".join(list1))
    list1.pop(count)
    count -= 1

for i in range(1,10) :
    print(str(i) * i)
        



































