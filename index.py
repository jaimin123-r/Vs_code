#from colorama import Fore, Back, Style

# print("Hello,World!")

'''
a=10
b=int("10")
print(a+b)
'''

# x=input("Enter The Your Name:")
# v=int(input("enter The Age"))

# print("Good Morning ! "+ x)

# if v>=18:
#     print("You Can Vote!!")
# else:
#     print("You Can't Vote!!!")

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# list = ['jaimin','Komal','Rakshita']
# print(list[0])
# print(type(list))

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# tuple = (1,'2',3,'4')
# print(tuple)
# print(type(tuple))

#Set items are unordered, unchangeable, and do not allow duplicate values.
# set = {"Jaimin","Hiral","Kano"}
# print(set)
# print(type(set))

# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# dic = {
#     "Animal":"Cow",
#     "Bird":"Sparrow",
#     "Insect":"butterfly"
# }


# x = range(1,11)
# k = int(input("enter the value:"))
# for i in range(1,11):
#    print(k," * ",i," = ",(k*i))



# print(dic)
# print(type(dic))

# jaimin = 1j
# print(jaimin)
# print(type(jaimin))
    
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# v = int(input("enter the number"))
# def greeting():
#     if v==1:
#         print("Good morning")
#     elif v==2:
#         print("Good evening")
#     else:
#         print("Good night")

# greeting()

class Car:

    def __init__(self,BrandName,price):
        self.name = BrandName
        self.price = price

Gadi = input("Enter The Brand Name")
Gadi_Bhav = int(input("Enter The Price"))

Cullinun = Car(Gadi,Gadi_Bhav)
print("compnay name is",Cullinun.name,Cullinun.price)


'''
print(Fore.YELLOW+"compnay name is")
print(Back.GREEN + 'The text with Green background')
print(Style.DIM + 'The text is DIM now')
'''

