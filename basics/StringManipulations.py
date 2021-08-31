#Find a Substring of a given String
str = "Selenium"
#Extract Substring from position 2 to position 5
substr = str[1]+str[2]+str[3]+str[4]
print(substr)

substr = str[1:5]
print(substr)

#Print last 2 chars from the string
str = "Company"
print(len(str))
lastindex = len(str)-1
print("1: ",str[lastindex-1:lastindex+1])
print("2: ", str[-2:])
print("3: ", str[lastindex-1:])

#Verify whether the word is part of string
str = "This is a Python Workshop"
word = "shop"
print("1: ", str.__contains__(word))
print("2: ", word in str)
if "shop" in str:
    print("3: ", "True")
print(str.find(word))
if str.find(word) != -1:
    print("4: ", "True")

#Remove Whitespace from string beginning and end
str = "   Hello World   "
print("1: ",str.strip(" "))
print("2: ", str.strip())

#Replace the string "Python" with "Jython"
str = "Python"
print("1: ", str.replace("Python","Jython"))
print("2: ", str.replace('P', 'J'))
print(str)
str = str.replace('P','J')
print(str)

#Split the String "Google Search - Python" at "-" and print each part separately
str="Google Search - Python"
print(str.split("-"))
print(str.split("-")[0])
print(str.split("-")[1].strip())
print(str.partition("-"))

#String Format
item = "books"
quantity = 4
print("1: I want to order", quantity, item)
str = "I want to order {} {}"
str = str.format(quantity, item)
print("2:",str)
print("3:",F"I want to order {quantity} {item}")

str = "Alpha123"
print(str.isalnum())

str = "We are learning Python in Pycharm"
print(str.partition("learning")[0],str.partition("learning")[1],str.partition("learning")[2])