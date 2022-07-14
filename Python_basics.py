#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("hello")


# In[3]:


print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /____|")


# In[4]:


print(" /____|")
print("     /|")
print("    / |")
print("   /  |")
print("  /   |")


# In[8]:


char_name = "John"
char_age = "35"
print ("The man name is " + char_name + " and his age is " + char_age)


# In[9]:


#Basic Data types:
#String, - ""needed
#Numbers, decimals - "" not needed
#boolean - True/False


# In[31]:


phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3]) #index function
print(phrase.index("Acad")) #index function
print(phrase.replace("Giraffe","Elephant"))


# In[51]:


#Working with numbers:
print(3*(4+5))
print (10%3) #modulus - gives remainder as output
my_num = - 5
print(my_num)
print(str(my_num) + " my fav number")
print(abs(my_num))
print(pow(3,2)) #power function - needs 2 parameters - first number = the bottom number and the second number is the power number.
print(max(4,6)) #max function
print(min(4,6)) #min function
print(round(3.4))#round function


# In[52]:


from math import * #allows us to do many more math functions


# In[58]:


num = -5
print(floor(3.7)) #floor function - chops off the decimal point
print(ceil(3.7)) #ceil function - rounds up to highest number of that decimal irrespective of wht is after the decimal
print(sqrt(36))
print(int(sqrt(36)))


# In[61]:


#Getting Input from User:
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hi " +name+ " ! You are of "+age)


# In[65]:


#Building a basic calculator:
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
results = num1 +num2
print(results)
#Here the output is 12, because by default Input fucntion gives ut String value
#Inorder for this to work correctly, we need to convert these num1 and num2 to integers
#we have 2 ways
#FIRST:
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
results = int(num1) +int(num2)
print(results)
#This is a problem, if the input value is a decimal.
#Second: - Lets user input any number they want
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
results = float(num1) +float(num2)
print(results)


# In[66]:


#Mad Libs Game:
color = input("Please enter a color: ")
plural_noun = input("Please enter a plural_noun: ")
celeb = input("Please enter a celebrity: ")
print("Roses are " +color)
print(plural_noun + " are blue")
print("I love " +celeb)


# # DATA STRUCTURE - LISTS:
# List are Mutable - can modify

# In[74]:


friends = ["Kevin","Karen","Jim","Oscar","Toby"]
print(friends)
print(friends[1])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends[1] = "Mike"
print(friends)


# In[92]:


#List Functions:
nums = [4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Oscar","Jim","Toby"]
print(friends)
friends.extend(nums) #adds 2 lists
print(friends)
friends.append("Creed") #Append always adds an item to the end of list
print(friends)
friends.insert(1,"Kelly") #insert function adds an item at any mentioned position.
print(friends)
friends.remove("Karen")#remove an item from list
print(friends)
friends.pop() #removes the last item in the list
print(friends)
print(friends.index('Kevin'))#gives the index of the item in the list
print(friends.count("Jim"))#count of no. of times an item is in a list
#print(friends.sort()) #sorts in alphabetical order
print(nums.sort())
print(nums.reverse())
nums.reverse()
print(nums)
friends2 = friends.copy()
print(friends2)
friends.clear() #removes all the items in the list
print(friends)


# # DATA STRUCTURE - TUPELS:
# Tuples are immutable - cannot be changed

# In[94]:


cordinates =(4,5)
print(cordinates)
print(cordinates[0])


# In[96]:


cordinates =[(4,6),(6,7),(80,34)]
print(cordinates)
print(cordinates[0])


# # FUNCTIONS

# In[99]:


def sayhi():
    print("Hello user")

sayhi()


# In[104]:


#giving parameters
def sayhi(name):
    print("Hello " + name)
    
sayhi("Mike")

def sayhi(name, age):
    print("Hello " + name +" You are "+str(age))
    
sayhi("Mike", 35)


# # RETURN STATEMENT

# In[107]:


def cube(num):
    return num*num*num
    
print(cube(3))


# In[108]:


def cube(num):
    return num*num*num

result = cube(4)
print(result)


# # IF STATEMENTS

# In[120]:


is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a not male, but you are tall")
else:
    print("You are not a male nor tall nor both")


# In[122]:


def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2 >= num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(222,3,4))


# # BUILDING A BETTER CALCULATOR:

# In[125]:


num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)

else:
    print("Error")


# # DICTIONARY:

# In[127]:


monthcon = {
    "Jan":"January",
    "Feb":"Febuary",
    "Mar":"March",
    "Apr":"April"
}


# In[136]:


print(monthcon["Feb"])
print(monthcon.get("Mar"))
print(monthcon.get("Dec"))
print(monthcon.get("Dec" , "Not a valid key"))


# # WHILE LOOP

# In[138]:


i = 1
while i <=10:
    print(i)
    i+=1
print("DONE")


# # BUILDING A GUESSING GAME:

# In[147]:


secret_word = "Python"
guess = ''
guess_count =0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess word: ")
        guess_count +=1
    else:
        out_of_guesses = True
    
if out_of_guesses:
    print("You Lose!")
else:
    print("You win!")


# # FOR LOOP:

# In[148]:


for letter in "Python":
    print(letter)


# In[151]:


friends = ["Jim", "Karen","Kevin"]
for index in range(10):
    print(index)


# In[152]:


for index in range(3,10):
    print(index)


# In[158]:


friends = ["Jim", "Karen","Kevin"]
len(friends)
for index in range(len(friends)):
    print(friends[index])
  


# In[160]:


for index in range(5):
    if index ==0:
        print("first")
    else:
        print("not")


# # EXPONENT FUNCTION:

# In[161]:


print(2**3)


# In[163]:


def raise_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_power(3,4))


# # 2D LISTS & NESTED LOOPS

# In[165]:


num_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(num_grid)


# In[166]:


print(num_grid[0][0])


# In[167]:


print(num_grid[2][1])


# In[168]:


for row in num_grid:
    print(row)


# In[169]:


for row in num_grid:
    for col in row:
        print(col)


# # BUILD A TRANSLATOR

# In[174]:


def trans(phrase):
    translation = ''
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    for letter in phrase:
        if letter in vowels:
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation +letter
    return translation

print(trans(input("Enter a phrase")))


# # TRY /EXCEPT:

# In[176]:


try:
    num = int(input("ENter a number: "))
    print(num)
except:
    print("invalid input")


# In[181]:


try:
    value =10/0
    num = int(input("ENter a number: "))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")


# # READING FILES

# In[ ]:


#variable = open("filename","mode") #mode = r,w(it just overwrites everything in a file),a(append to the existing file),r+
#variable.close()
#always check if the file is readable -> variable.readable(). it will give True if readable, if not it will be False.
#variable.read() - to read the whole file
#variable.readline() -to read the first line of the file. 
#variable.readlines() - reads whole file and put it in an array
#for va in variable.readlines(): print(va)
#to create a webpage - open("index.html","w")


# # MODULES & PIP

# In[183]:


#import file_nameof the module
import docx


# In[ ]:




