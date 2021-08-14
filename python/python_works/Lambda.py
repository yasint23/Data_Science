print((lambda x: x**2)(2))

print((lambda x,y: (x+y)/2)(3,5))

(lambda x: x[::-1])("ali")

for x in (3,4,5,6,7,9):
    print(x,":",(lambda x: "odd" if x % 2 != 0 else "even")(x))
    
numbers =[1,3,4,5,6,9]    
a=map(lambda x: x**3,numbers)
print(list(a))

nums1 = [9,6,7,4]
nums2 = [3,6,5,8] 
mean= map(lambda x,y: (x + y)/2, nums1,nums2)
print(list(mean))

word = ["ali veli deli", "mehmet aga kuzeni", "cemilin-bacisi"]
list(map(len, word))

first_ten = [0,1,2,3,4,5,6,7,8,9]
even = filter(lambda x: x % 2 == 0, first_ten)
print('Even numbers are:', list(even))

words = ["apple", "swim", "clock", "me", "kiwi", "banana"]
liste = filter(lambda x: len(x) < 5, words)
print(list(liste))

for i in filter (lambda x: len(x)<5,words):
    print(i)
    
vowels=['a','e','i','o','u']
first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

filtered_vowels = filter(lambda x: x in vowels, first_ten)
print(* filtered_vowels)


words1 = ["you", "much","hard"]
words2 = ["i","you","he"]
words3 = ["love","ate","works"]

sentence = map(lambda x,y,z: x + " " + y + " " + z, words2,words3,words1)
for i in sentence:
    print(i)

def modular_function(n):
    return lambda x: x ** n

power_of_3 = modular_function(3)
print(power_of_3(5))

print((lambda x: x**3)(5))


multiply = lambda x: x * 4
add = lambda x, y: x + y
print(add(multiply(10), 5))

square = lambda x: x**2
print(square(5))

number_list=[1, 2, 3, 4, 5]

result= list(map(lambda x: x**2, number_list))
print(result)


number_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result= list(filter(lambda x: x % 2 != 0, number_list)) 
print(result)


































