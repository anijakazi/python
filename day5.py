# """# strip
# x="     anijakazi     "
# print(x.strip())

# x="     anijakazi     "
# print(x.lstrip())
# x="     anijakazi     "
# print(x.rstrip())"""

# """# just

# x="anijakazi"
# print(x.rjust(10,"*"))
# print(x.ljust(10,"*"))"""

# #x="anijakazi"
# #print(x.zfill(12))

# #Print your name left-justified in width 15 using *.
# a="anijakazi"
# print(a.ljust(15,"*"))

# #Print your name right-justified in width 15 using *.
# a="anijakazi"
# print(a.rjust(15,"*"))


#Generate roll numbers from 1 to 10 like R001, R002, … using zfill().
x=input("enter the string:-")
for i in range(1, 11):
    print("R",end="")
    print(x.zfill(2),end="")
    print(i)


   #Create a formatted table of student names (left-aligned) and marks (right-aligned). 
# for i in range(1,4):
#     x=input("enter the name of student:-")
#     r=input("enter the roll no:-")
#     print(x.lstrip(),r.rjust(10," "))