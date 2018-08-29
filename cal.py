class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def product(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

a = int(input("enter value"))
b = int(input("enter value"))
obj=cal(a,b)
choice = 1
while(choice!=0):
    print("0.exit")
    print("1.add")
    print ("3.sub")
    print ("4.product")
    print("5. div")
    print(" enter choice")
    choice = int(input("enter choice"))
    if choice==1:
        print("result", obj.add())
    elif choice ==2:
        print("result",obj.sub())
    elif choice == 3:
        print("result", obj.product())
    elif choice==4:
        print("result", obj.div())
    else:
        print("invalid choice")
print()