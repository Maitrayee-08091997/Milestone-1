
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
        title = input(" Enter the movie title: ")
        director = input("Enter the movie director: ")
        year = input("Enter the movie release year: ")
        n=input("Enter the name to add")
        n.append({
            'title': title,
            'director': director,
            'year': year
        })
        obj.add(n)
        print("List: ", obj.dis())


    elif choice == 2:
        n = input("Enter name to remove: ")
        obj.remove(n)
        print("List: ", obj.dis())

    elif choice == 3:
        print("List: ", obj.dis())
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()
