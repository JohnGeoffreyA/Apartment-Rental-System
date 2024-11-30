import sys
import json

def main():
    apartments = load_apartments()
    while True:
        print("\n\t\t\t|--------------------------------------------------------------------|")
        print("\t\t\t|                            Apartment Rentals                       |")
        print("\t\t\t|--------------------------------------------------------------------|")
        print("\t\t\t|\t\t\t\t\t\t\t\t     |")
        print("\t\t\t|    [1] Rent Apartment\t\t        [4] View All Apartments      |")
        print("\t\t\t|    [2] Update Rental Information\t[5] Exit                     |")
        print("\t\t\t|    [3] End Rent\t\t\t\t\t\t     |")
        print("\t\t\t|--------------------------------------------------------------------|")
        choice = int(input("\tEnter your choice: "))

        if choice == 1:
            apartment = Apartment()
            apartment.rent_apartment(apartments) 
            apartments[apartment.num] = apartment
        elif choice == 2:
            apartment_number = int(input("\n\tEnter the Apartment Number to Update: "))
            if apartment_number in apartments:
                apartments[apartment_number].update_rental()
            else:
                print("\tApartment not found!")
        elif choice == 3:
            apartment_number = int(input("\n\tEnter the Apartment Number to End Rent: "))
            if apartment_number in apartments:
                apartments[apartment_number].end_rent(apartments)  
            else:
                print("\tApartment not found!")
        elif choice == 4:
            if apartments:
                print("\n\tRented Apartments:")
                for apartment in apartments.values():
                    apartment.view_apartments()

                print("\n\tAvailable Apartments:")
                for i in range(1, 31):
                    if i not in apartments:
                        print(f"\tApartment Number: {i} is available")
            else:
                print("\tAll apartments are available!")
        elif choice == 5:
            print("\n\tExiting the program. Goodbye!")
            save_apartments(apartments)  
            break
        else:
            print("\tInvalid choice. Please try again.")