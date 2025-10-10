# count how many time letter "a"apper in string in s=aAabcdefg

"""s="aAabcdefg"
print(s.count("a"))"""

 
#2. Take input from the user and check whether it starts with "Hello" and ends with "Bye" or not

""""s=input("enter your string")
print(s.startswith("hello"))
print(s.endswith("by"))"""
#3. Given "Python Programming", replace all spaces with "_" and convert the whole string to uppercase.
'''s=" a n i j a k a z i "
print(s.replace(" ","_"),s.upper())'''

#4. Write a program that checks if a given string is all lowercase, then convert it to title case.
"""s="anija kazi"
print(s.upper())"""


#5.Given "Welcome*", remove all "*" characters from the end of the string.
'''s="welcome*"
print(s.removesuffix("*"))'''


#6.Convert this list of words into a single comma-separated string:
#["Apple", "Banana", "Cherry", "Dates"]
#8.Format the output of name = "Alice" and marks = 89 like this using .format()
#Student Alice has scored 89 marks
'''name="alice"
marks=89
s=f"student {name} has scored {marks}matks"
print(s)
x="student {} has scored {}matks".format(name,marks)
print(x)'''


#10. Remove all leading and trailing whitespaces, then print the length of the cleaned string.
'''s="a n i j a k a z i "
print(s.replace(" ",""))
print(len(s))'''

##11.Write a program to print each word of "Python is fun to learn" on a new line using split().
# s="Python is fun to learn"
# print(s.split())
# for i in s:
#     print(i)
   
#12. From the string "Email: example@gmail.com", extract only the email ID using slicing or string methods.
# s="Email: example@gmail.com"
# print(s[7:14])


# 13.Replace all vowels in "Education" with "*".
# s="Education"
# vowels="aeiouAEOIU"
# p=""
# for i in s:
#     if i in vowels:
#         p=p+"*"
#     else:
#         p=p+i
# print(p)         




#14. Write a program that finds both the first and last position of the substring "data" in "Big data is transforming data analytics".
# s="Big data is transforming data analytics"
# print(s.find("data"))
# print(s.rfind("data"))


#15. Create 5 serial IDs in the format ID001, ID002, …, ID005 using zfill().
# x=input("enter the string:-")
# for i in range(1,6):
#     print("ID",end="")
#     print(x.zfill(2),end="")
#     print(i)

