age = int(input("How old are you?: "))

chronic = input("Do you have chronic disease?: Y/N:")

immune=input("Is your immune system too weak?: Y/N :")

if age>=75 and chronic=="Y" and immune=="Y":

    print("There is a risk of death")

else:

    print("There is no risk of death")