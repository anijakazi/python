#replace
# s="shital shital shital shailesh"
# s=s.replace("shital","vasudha",3)
# print(s)

# #translate  and maketrans
# s=str.maketrans("aeiou","12345","Edu")
# text="Education"
# print(text.translate(s))
# text = "A\tB\tC"
# print(text.expandtabs(0))

# text = "shital"
# print(text.encode())

# text= "123"
# print(text.isprintable())

# txt = "~$###123Shital_-+="
# x = txt.isascii()
# print(x)
#The isidentifier() method returns True if the string is a valid identifier, otherwise False.
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

# a = "MyFolder"
# b = "Demo002"
# c = "2bring"
# d = "my demo"

# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

# s=" 0"
# print(s.isspace())

# s="Shital Sahebrao chavan"
# print(s.istitle())

# The isascii() method returns True if all the characters are ascii characters  (a-z).
# s="89"
# print(s.isascii())



"""s="anija  anija zuberpasha "
x=s.replace("anija ", "kazi",1)
print(x)
"""
"""s="anija  anija zuberpasha "
print(s.replace("anija ","kazi",1))"""

"""anija ="kazi _#$%$$anija zuberpasha"
print(anija.isprintable())"""

"""anija ="kazi1234anija zuberpasha"
print(anija.encode())"""


"""a="anija kazi"
b=" kazi"
x="12th"
v="*is star"
y="_anijak"
z="anija_kazi_19"

print(a.isidentifier())
print(b.isidentifier())
print(x.isidentifier())
print(v.isidentifier())
print(y.isidentifier())
print(z.isidentifier())"""


"""q=" 988 "
print(q.isspace())

q=" "
print(q.isspace())"""


"""s="Anija Kazi 19 "
print(s.istitle())
"""

"""s="anija\t kazi"
print(s.expandtabs(100))"""



s=str.maketrans("anijaa","saniya")
a="anijaa "
print(a.translate(s))