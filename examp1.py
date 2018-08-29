#separate odd and even numbers

a=[12,10,3,5,12,7,1,8]
x=[]
y=[]
for i in a:
   #for i in range(i+1):
         if (i % 2) == 0:
              x.append(i)
         else:
              y.append(i)

print("even list", x)
print("odd list", y)
