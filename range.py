"""a = [('a','12CS039'),('b','12CS320'),('c','12CS055'),('d','12CS100')]
l_range = int(input("enter a number "))
u_range = int(input("enter a number"))
#for i in range(0,n):
l = '12CS0' + str(l_range)
u = '12CS' + str(u_range)
final=[x for x in a if x[1]>l and x[1]<u]
print(final)"""""

"""y=[('a','12CS039'),('b','12CS320'),('c','12CS055'),('d','12CS100')]
low=int(input("Enter lower roll number (starting with 12CS):"))
up=int(input("Enter upper roll number (starting with 12CS):"))
l='12CS0'+str(low)
u='12CS'+str(up)
p=[x for x in y if x[1]>l and x[1]<u]
print(p)"""""

"""n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev) """


#reverse string
a = "welcome"
b = ""
n = len(a)
while n>0:
    b = b+ a[n-1]
    n = n-1
print(b)


