text = "{:.2f}, {:.3f}, {:.4f}".format(3.1463, 5.367, 7.324324)
print(text)
#3.15, 5.367, 7.3243


word = 'happy'
list(word)
#['h', 'a', 'p', 'p', 'y']


numbers =[1,4,6]
numbers.append(2)
print(numbers)
numbers.insert(2,3)
print(numbers)
#[1, 4, 6, 2]
#[1, 4, 3, 6, 2]


sentence = "I live in Prescot"
print(sentence.upper())
print(sentence.lower())
print(sentence.swapcase())
title_sentence = sentence.title()
print(title_sentence)
changed_sentence = sentence.replace("i","+")
print(changed_sentence)
#I LIVE IN PRESCOT
#i live in prescot
#i LIVE IN pRESCOT
#I Live In Prescot
#I l+ve +n Prescot


city = "SARAJEVO"
output = f"I live in {city.capitalize()}."
print(output)
#I live in Sarajevo.


