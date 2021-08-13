#Exercise1:
def sansur(sansurlu,sesli):
    n=0
    for i in sansurlu:
        if i =="*":
          sansurlu=sansurlu.replace("*",sesli[n],1)
          n +=1
    return sansurlu
    print(sansur("pyth*n", "o")) 
    print(sansur("*r*b*m* p*rk *tt*m","aaaiaei"))

#Exercise:
def kelime_cift_mi(cumle):
    kucuk="abcçdefgğhıijklmnoöprsştuüvyz"
    toplam=0
    for i in cumle.lower():
        if i in kucuk:
            toplam += kucuk.index(i) + 1
        if toplam % 2 == 0:
            return True
        else:
            return False
print(kelime_cift_mi("Bilgisayar")) 

#Exercise:
def computepay(h,r):    
    if h > 40:
        p = 40*r + (h-40) * r/2
    else:
        p = h*r
    return p
computepay(45,10.50)
        
#Exercise:
def factoriel(num):
  result = 1
  for i in range(1,num+1):
    result *= i
  return result

factoriel(5)

#Exercise:
def count_down(n,string):
    result=''
    for i in range(n,0,-1):
        result += str(i) + '*'
    result += string.upper() + '!'
    return result 
count_down(4,"come")

#Exercise:
def besides(list):
    for i in list:
        if list.index('Arif') == list.index('Raife')+1 or list.index('Arif') == list.index('Raife')-1:
            return True
        else:
            return False
print(besides(['Arif','Raife','Nihal']))
print(besides(['Arif','Nihal','Raife']))
            
#Exercise:
def multiply_add(list):
    result = 0
    for i in range(len(list)):
        result += i*list[i]
    return result
print(multiply_add([1,2,3,4,5,6,7,8,9,10]))
    
#Exercise:
def letter_number(sentence):
    l=0
    n=0
    o=0
    for i in sentence:
        if i.isalpha():
            l += 1
        elif i.isdigit():
            n += 1
        else:
            o += 1
    return f"Letters: {l}, numbers: {n}, and others: {o}"
print(letter_number("10'a kadar saysam ve sonrasında hayat bayram olsa."))
    
#Exercise:
def max_min_num(string):
    liste = list(map(int, string.split()))
    return f"{max(liste)} {min(liste)}"
print(max_min_num("3 2 4 6 -1 12"))    
        
#Exercise:
def reverse(sentence):
    liste = sentence.split()
    new = ''
    for i in liste:
        if len(i) >= 5:
            new += i [::-1] + ' '
        else:
            new += i + ' '
    return new.strip()
print(reverse("If I could be a data scientist:)"))         
            
#Exercise:

def non_rep_int(list):  
    new_list =[]
    for i in list:
        new_list = list.count(i)
        if new_list == 1:
            return i
  
print(non_rep_int([6, 1, 3, 3, 3, 6, 6]))
          
#Exercise:
l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')      
#Exercise:           
input_list = [1, 2, 2, 5, 8, 4, 4, 8]

l1 = []
count = 0
  
for i in input_list:
    if i not in l1:
        count += 1
        l1.append(i)
  
print("No of unique items are:", count)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






