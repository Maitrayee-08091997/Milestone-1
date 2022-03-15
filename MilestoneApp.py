class Hotel:
    def init(self, Hotel_name, Hotel_id, Hotel_type):
        self.Hotel_name = Hotel_name

        self.Hotel_id = Hotel_id
        self.Hotel_type = Hotel_type


class Customer:
    def init(self, Customer_ID, Customer_name, Customer_offers, Hotel_id):
        self.Customer_ID = Customer_ID

        self.Customer_name = Customer_name
        self.Customer_offers = Customer_offers
        self.Hotel_id = Hotel_id
if __name__ == '_ main _':

    Customers = []


    Hotels = []
while (True):
    print("1.Add Customer")
    print("2.Add Hotel")
    print("3.Delete Customer")
    print("4.Delete Hotel")
    print("5.Exit")
    n = int(input("Enter the number"))
    if (n == 1):
        Customer_ID = int(input("Enter the Customer Id:"))
        Customer_name = input("Enter the Customer Name:")
        Customer_offers = input("Enter the Customer offers:")
        Hotel_id = int(input("Enter the Customer Hotel id:"))


Customers.append(Customer(Customer_ID, Customer_name, Customer_offers, Hotel_id))

if (n == 2):
    Hotel_name = input("Enter the Hotel Name:")
    Hotel_id = int(input("Enter the Hotel_Id:"))
    Hotel_type = input("Enter the Hotel Type:")
    Hotels.append(Hotel(Hotel_name, Hotel_id, Hotel_type))


    if (n == 3):
        if len(Customers) == 0:
          print("No Customer Records Added")
        else:
            customer_id = int(input("Enter the Customer ID to Delete:"))
            for i in Customers:
                if i.Customer_ID == customer_id: Customers.remove(i)
                break

    if (n == 4):
        if len(Hotels) == 0:
            print("No Hotels Records Added")
        else:
            Hotel_id = int(input("Enter the Hotel_id to Delete:"))
            deleting_Customer_records = []
            for i in Customers:
                if i.Hotel_id == Hotel_id: deleting_Customer_records.append(i)
            for i in deleting_Customer_records: Customers.remove(i)
            for i in Hotels:
                if i.Hotel_id == Hotel_id: Hotels.remove(i)
                break




