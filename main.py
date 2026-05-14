Reserved = 1
Empty = 0

def reserve_seat(seats):
    # إضافة دالة العرض هنا قبل طلب رقم الكرسي
    show_available(seats)
    
    seat_num = int(input("Enter seat number (1-12): "))
    if 1 <= seat_num <= 12:
        index = seat_num - 1
        if seats[index] == 0:
            seats[index] = 1
            print("Seat reserved successfully")
        else:
            print("Seat already reserved")
    else:
        print("Error: Invalid seat number! Please choose between 1 and 12.")

def cancel_reservation(seats):
    seat_num = int(input("Enter seat number (1-12): "))
    if 1 <= seat_num <= 12:
        index = seat_num - 1
        if seats[index] == 1:
            seats[index] = 0
            print("Reservation canceled")
        else:
            print("Seat is already empty")
    else:
        print("Error: Invalid seat number! Please choose between 1 and 12.")

def show_available(seats):
    print("Available seats:")
    for i in range(len(seats)):
        if seats[i] == 0:
            print(i + 1)

def show_reserved(seats):
    print("Reserved seats:")
    for i in range(len(seats)):
        if seats[i] == 1:
            print(i + 1)

def summary(seats): # البوووووووووونصصصصصص
    reserved = seats.count(1)
    available = seats.count(0)            
    print("Summary:")
    print("Reserved:", reserved)
    print("Available:", available)

def menu():
    seats = [0] * 12 #هنا الكراسي كلها فاااااضيه
    while True:
        print("\n1. Reserve")
        print("2. Cancel")
        print("3. Show available")
        print("4. Show reserved")
        print("5. Summary") #هنا بنستدعى البونص
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            reserve_seat(seats)
        elif choice == '2':
            cancel_reservation(seats)
        elif choice == '3':
            show_available(seats)
        elif choice == '4':
            show_reserved(seats)
        elif choice == '5':
            summary(seats)   
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
menu()
