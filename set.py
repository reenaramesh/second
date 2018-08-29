#count vowels

"""string = "hello welcome"
vowels = set("aeiou")
count = 0
for i in string:
    if i in vowels:
        count = count+1
print(count)"""

#check comon b/w 2 strings
"""string1 = "hi hello"
string2 = "hello"
#a = string1.split()
#b = string2.split()
for i in range(0,len(string1)):
    for j in range(0,len(string2)):
        if string1[i] == string2[j]:
         print(string2[j])"""

a = ""
x = "hello kjhjkhk"
y = "hi hello"

for i in range(0,len(x)):
    for j in range(0,len(y)):
        if (x[i]==y[j]):
           print(x[i])


a= list(set(x)&(set(y)))
print(a)

a= list(set(x)-(set(y)))
print(a)

a= list(set(x)|(set(y)))
print(a)

a= list(set(x)^(set(y)))
print(a)





