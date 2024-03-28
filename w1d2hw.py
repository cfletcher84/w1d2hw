# Real World Python Dictionary Applications
# Task 1

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu['Beverages'] = 'Coke', 'Dr. Pepper'

print(restaurant_menu)

restaurant_menu['Main Course'].update({'Steak': '17.99'})

print(restaurant_menu['Main Course'])

restaurant_menu['Starters'].pop('Bruschetta')

print(restaurant_menu)

# Advanced data handling with Python

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def new_booking():
    booking_name = input("\nThank you for choosing Fletchers for your stay!\nWhat is your name? : ")
    for k, v in hotel_rooms.items():
        if v['status'] == 'available':
            v['status'] = "Booked"
            v['customer'] = booking_name
    print(f"You checked {booking_name}. ")



def check_out():
    check_out_user = input('\nWho will be checking out? : ') 
    for k, v in hotel_rooms.items():
        if v['customer'] == check_out_user:
            v['customer'] = ""
            v['status'] = 'available'
    return v

def room_status():
    print(f"\nHere is the status of the current bookings\n {hotel_rooms}")


new_booking()
check_out()
room_status()

# E-Commerce Product Search

matched_items = {}

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}
def search_item():
    user_input = input('\nWhat would you like to search for? : ')
    for  k, v in products.items():
        if v['name'] == user_input:
            matched_items.update(v)
            print(f"Here are the matching items found!: \n{matched_items}") 

        else:
            print(f"{user_input} has no matches sorry!")
    
    return matched_items

search_item()
    

# Python Programming Challenges for Customer Service Data Handling

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket():
    ticket_number = input('What is the ticket number? : ')
    if ticket_number in service_tickets:
        print(f"\nSorry that ticket number already exists!")
    else:   
        name = input("\nPlease enter your name? : ")
        issue = input('\nWhat is the issue you are experiencing? : ')

        service_tickets[ticket_number] = {}
        service_tickets[ticket_number]['Customer'] = name
        service_tickets[ticket_number]['Issue'] = issue
        service_tickets[ticket_number]['Status'] = 'Open'

    return service_tickets



def update_ticket():
    ticket = input(f"Which ticket are you trying to update? : ")

    if ticket in service_tickets:
        new_name = input("What is the new name? : ")
        new_issue = input('What is the new issue? : ')
        new_status = input('What is the new status? : ')

        service_tickets[ticket]['Customer'] = new_name
        service_tickets[ticket]['Status'] = new_status
        service_tickets[ticket]['Issue'] = new_issue
    else:
        print(f'Im sorry ticket {ticket} does not exist.')
    return service_tickets



def display_tickets():
    print(f"Here are you current service tickets: \
          \n{service_tickets}")
    

def start_app():
    while True:        
        try:
            print('\nWelcome to the service department!\
                  \nPlease select from the following menu items: \
                  \n1. Add a service ticket.\
                  \n2. Update a service ticket.\
                  \n3. View service tickets.\n')
            user_input = int(input("What would you like to do? Enter 1-4: "))
            if user_input == 4:
                break
            elif user_input == 3:
                display_tickets()
            elif user_input == 2:
                update_ticket()
            elif user_input == 1:
                add_ticket()
        except ValueError:
            print(f"\nThis is not a number 1-4, try again please.")
            break

    

start_app()
        

# Python Essentials for Business Analytics
        
import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

copied_sales = copy.deepcopy(weekly_sales)

copied_sales['Week 2'].update({'Electronics': 18000})

print(copied_sales)
print(weekly_sales)
