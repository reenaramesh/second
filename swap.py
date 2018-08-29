
# swap 1st nd last value
"""a=[22,5,4,87,52]
n = len(a)
for i in range(0,n):
    temp = a[0]
    a[0] = a[n-1]
    a[n-1] = temp
print(a)"""

#  remove duplicate terms in list

"""new_list=[12,33,44,6,12]
new1_list=[]


[new1_list.append(x) for x in new_list if x not in new1_list]
print(new1_list) """

# fetch the word which has longest length

a = ['afdhgfh','twerterdfgdf','kjgjk','efre']
b = []
n = len(a)
#for number in a:
for x in range(0, n):
   temp = len(a[0])
   val = a[0]
   for i in a:

       if (len(i) > temp):
           temp = len(i)
           val = i
print(val)


