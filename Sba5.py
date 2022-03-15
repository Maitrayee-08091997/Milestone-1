import sys


class Hotel:
    def __init__(self, listofhotels):  # this init method is the first method to be invoked when you create an object
        # what attributes does a library in general have? - for now, let's abstract and just say it has availablebooks (we're not going to program the shelves, and walls in!)
        self.availablehotels = listofhotels

    def displayAvailablehotels(self):
        print("The hotels we have in our list are as follows:")
        print("================================")
        for hotels in self.availablehotels:
            print(hotels)

    def delHotel(self, Hotel_id):
        if Hotel_id in self.availablehotels:
            print("The hotel you requested ")
            self.availablehotels.remove(Hotel_id)
        else:
            print("Sorry the hotel you have requested is currently not in the list")

    def addHotel(self, Hotel_id):
        self.availablehotels.append(Hotel_id)
        print("Thanks ")


class Customer:
    def deleteHotel(self):
        print("Enter the name of the book you'd like to borrow>>")
        self.hotels = input()
        return self.hotels

    def DeleteCustomer(self):
        print("Enter the name of the book you'd like to return>>")
        self.hotels = input()
        return self.hotels


def main():
    hotel = Hotel(["The Last Battle", "The Screwtape letters", "The Great Divorce"])
    customer = Customer()
    done = False
    while done == False:
        print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)

        choice = int(input("Enter Choice:"))
        if choice == 1:
            hotel.displayAvailablehotels()
        elif choice == 2:
            hotel.deleteHotel(customer.Hotel_id())
        elif choice == 3:
            hotel.addHotel(customer.Hotel_id())
        elif choice == 4:
            sys.exit()


main()

