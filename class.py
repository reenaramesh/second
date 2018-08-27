class String():
    def __init__(self):
        self.n = []
    def add(self, a):
        return self.n.append(a)
    def remove(self, b):
        self.n.remove(b)
    def dis(self):
        return (self.n)

obj = String()

choice = 1
while choice !=0:
     print ("0:exit")
     print("1:add")
     print("2:remove")
     print("3.display")
     choice = int(input("enter choice"))
     if choice==1:
         n= int(input("enter no to add"))
         obj.add(n)
         print(obj.dis())
     elif choice == 2:
          n= int(input("enetr no to remove"))
          obj.remove(n)
          print(obj.dis())
     elif choice==3:
          print(obj.dis())
     elif choice==0:
          print(" exit ")
     else:
          print("invalid choice")

print()


class check():
    def __init__(self):
        self.n = []

    def add(self, a):
        return self.n.append(a)

    def remove(self, b):
        self.n.remove(b)

    def dis(self):
        return (self.n)


obj = check()

choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    choice = int(input("Enter choice: "))
    if choice == 1:
        n = int(input("Enter number to append: "))
        obj.add(n)
        print("List: ", obj.dis())

    elif choice == 2:
        n = int(input("Enter number to remove: "))
        obj.remove(n)
        print("List: ", obj.dis())

    elif choice == 3:
        print("List: ", obj.dis())
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()
0