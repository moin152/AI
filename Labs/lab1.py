print("Hello")
txt=input("Enter Your Name: ")
if txt=="Moin Yaqoob":
 print(txt)
 print(type(txt))

'''count=0
while count<=3:
    print("Hi")
    count=count+1

print ("list iteration")
l= ["ggeks","for","geeks"]
for i in l:
    print(i)
for index in range(len(l)):
    print(index)
for letter in 'geeksforgeeks':
    if letter=='e'or letter=='s' :
      break
    print ('Current letter :', letter)
    var=10
    '''
def my_fun():
        print("Moin")

my_fun()


#input statement

name=input("I told you my name. Let's tells yours too to go further: ")

#2 statements in same line 

print("So, I'm Moin");print("And you are",name)

#indentation with if statement

gender=input("Now tell me your Gender. Press G for girl and B for boy: ")
if gender=='B':
    print("So you are a boy")
elif gender=='G':
    print("So you are a girl")
else:
    print("Wrong choice. Anyways Let's go further")

#use type() function

print("Type of", name,"is",type(name))
print("And that of",gender,"is",type(gender))
print("Type of None is",type(None))
print("And that of True is",type(True))
print("And finally type of 1+2j is",type(1+2j))
print("Type of",1,"is",type(1))
print("And that of",2.3,"is",type(2.3))

#Strings

print("Moin in double quotations")
print('Moin in single quotes')
print("Moin's Birthday is in May")
print('But he has "Something Important" to do')

#Special Characters

print("You know we can go on next line in same statement with \\n Let's try it.\nOh we are on next line.")
print("Let's try \\t.\tAfter using \\t we are here.")
print("Same is true for \\,\',\"")

#String indices

str="Moin"
print(str+"\'s 2nd index is",str[2],"and its -3rd index is",str[-3])

#List

print("Let's make a list of fav colors with ratings in next index of names")
li=["Pink",5,"Purple",4.5,"Grey",4.2,"Black",4]

print(li)

#List Indices

print(li[0],"color has rating",li[1])
print("and color",li[-2],"has rating",li[-1])

#List slice

li2=li[0:3]
print("Sliced list from index 0 to 2 is" ,li2)
print("Sliced list from 2 to -2 is",li[2:-1])
print("Copy of original list with slicing is",li[:])

print("And here Lab1 ends.\nThank you!")


