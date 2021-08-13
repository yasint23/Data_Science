s = float(input("Enter score"))
if 0.0 <= s <= 1.0:
    if 0.9 <= s:
        print("Score A")
    elif 0.8 <= s:
        print("Score B")
    elif 0.7 <= s:
        print("Score C")
    elif 0.6 <= s:
        print("Score D")
    elif s < 0.6: 
        print("Score E")
    else:
        print("Error")
        
def yazi(string):
    if string.upper() == string or string.lower() == string:
        return True
    else:
        return False
    yazi("Yasin")

def num_div(n):
    numbers =[]
    for i in range(1, n+1):
        if n % i == 0:
            numbers.append(i)
    return numbers
num_div(12)
 
  
def remove_letter(sentence):
    sesli = 'aeiou'
    new = ''
    for i in sentence:
        if i not in sesli:
            new += i
    return new
remove_letter("he will be going to new course")
    
def make_century(year):
    return f"{(year // 100) +1}.century"
make_century(1738)


def individual(liste):
    list=[]
    s = ""
    for i in liste:
        s += str(i)
    for j in set(s):
        if s.count(j) == 1:
            list.append(int(j))
    return list 
individual([2,2,3,11,3,6,5])
     
    
def cıkar(kelime):
  yeni = ''
  for i in range(len(kelime)-1):
    if kelime[i] != kelime [i+1] :
      yeni += kelime[i]
  yeni += kelime[-1]
  return yeni
print(cıkar("mmmeeerrhhhaaabbbaaa"))

def tree(height):
    for i in range(1,2*height,2):
        print((i*"#").center(2*height-1))
tree(7)














