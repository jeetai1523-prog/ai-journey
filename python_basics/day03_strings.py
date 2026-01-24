# #Day3 - Strings and user Input
# name="vishwajeet"
# city="solapur"
# mobile="9518541486"

# print("My name is",name)
# print("I live in",city)
# print("contact number",mobile)
# # Takin inputs from user

# user_name=input("Enter ue name:")
# user_age=input("Enter user age:")

# print("hello", user_name)
# print("Ur age is",user_age)

#String operations
#1-Concatenation
str1="hello \n"
str2="python"
print(str1+str2)

#Length
print(len(str1))
print(len(str2))

#Indexing
ch=str1[1]
print(ch)
print(str2[2:5])
print(str2[2:6])

#StrigFunctions
print(str2.endswith("on"))
print(str1.endswith("\n"))

str2=str2.capitalize()
print(str2)
print(str1.capitalize())## it doesnt replace the original string. it creates a new string in which this action is performed.
print(str1)

str3="rainbow is having beautiful colours. Colours are looking wonderful"
str4=str3.replace("u","")## it doesnt replace the original string. it creates a new string in which this action is performed.
print(str4)

print(str4.find("e"))## finds the index of that character
print(str4.count("o"))