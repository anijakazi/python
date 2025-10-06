"""s= input("enter your string:")
print (s[1:3])
print(s.capitalize())
print(s.title())"""



'''s="aabbccdde"
x=(s.count('a'))
y=(s.count('b'))
z=(s.count('c'))
r=(s.count('d'))
t=(s.count('e'))

if(x < y and x < z and x < r and x < t):
    print("x is less frequent")
if(y < x and y < z and y < r and y < t):
    print("yis less frequent")
if(z < y and z < x and z < r and z < t):
    print("z is less frequent")
if(r < y and r < z and r < x and r < t):
    print("r is less frequent")
if(t < y and t < z and t < r and t < x):
    print("t is less frequent")
'''


''''s=input("enter your string:-")
vowels="aeiouAEIOU"
count1=0
count2=0
for i in s:
 if i in vowels:
 print(i)
 count1=count1+1
 else:
 print(i,ends" ")
count2=count2+1 
print("vowels are",count1)
print("consonants are",count2)
 
'''


'''s="anijakazi16 "
print(s.center(20,'0'))
print(s.endswith('a'))
print(s.find('j'))
print(s.index('n'))
print(s.isalpha())
print(s.isalnum())
print(s.isdecimal())
print(s.isdigit())
print(s.isupper())
print(s.islower())
print(s.swapcase())
print(s.startswith("a"))
print(s.endswith("i"))
print(s.replace("a","s"))
print(s.casefold())
name="anija"
year=2
age=19
print("my name is {}. i am in {} year as cse engineering ,my age is{}".format(name,year,age))'''


dict={
"name":"anija",
"age":19,
"village":"pandharpur"

}
print("my name is {name}, i am {age}year old, i  live in{village}".format_map(dict))