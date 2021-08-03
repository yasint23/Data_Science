while []:
    print("while")
    print("outside of while")

######################################################################
age = input("Enter your age in correct format: ")
while not age.isdigit():
    print("You entered incorrect! Write correct format.")
    age = input("Enter your age in correct format: ")
    print("Your age is: ")
    
##############################################################################
answer = 33
question = 'What a two-digit number am I thinking of?'
print("Let's play the guessing game!")

while True:
    guess = int(input(question))
if guess < answer:
    print('Little higher')
elif guess > answer:
    print('little lower')
else: #guess == answer
    print('Are you mindreader!') 
break

#####################################################
sentence = input("give me a sentence")
words = sentence.split()
i = 0
longest = 0

while i < len(words):
    if len(words[i]) > longest:
        longest = len(words[i])
    i += 1
print("the length of the longest word is : ", longest)

################################################################################
names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]
for i in names:
    print("hello", i)
################################################################################
numbers = []

for i in range(1,6):
    numbers.append(i)
    print(numbers)

##################################################################################
number = int(input("Tell a number between 1 to 10."))

for i in range(11):
    print('{}x{} = '.format(number, i), number*i)

####################################################################################
for i in range(1,10):
    print(str(i) * i)    

#################################################################################
evens = []
odds = []

for i in range(1,10):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
        
print(evens) 
print(odds)
        

















