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

class Apartment:
    def __init__(self):
        self.num = 0
        self.name = ""
        self.month = 0
        self.day = 0
        self.year = 0
        self.months = 0
        self.end_month = 0
        self.end_year = 0
        self.price = 0.0
        self.payment = 0.0
        self.remaining_payment = 0.0

    def rent_apartment(self, apartments):
            while True:
                try:
                    self.num = int(input("\n\tEnter Apartment Number (1-30): "))
                    if 1 <= self.num <= 30:
                        if self.num in apartments:
                            print("\tApartment number is already taken. Please choose another one.")
                        else:
                            break  
                    else:
                        print("\tPlease choose a number (1-30).")
                except ValueError:
                    print("\tInvalid input. Please enter a valid number.")

            self.name = input("\tEnter Tenant Name: ")
            while True:
                try:
                    self.month, self.day, self.year = map(int, input("\tEnter Rent Date (Month Day Year): ").split())

                    if not (1 <= self.month <= 12):
                        print("\tInvalid month. Please enter a month (1-12).")
                        continue

                    if not (1 <= self.day <= 31):
                        print("\tInvalid day. Please enter a day (1-31).")
                        continue

                    if self.year <= 2023:
                        print("\tInvalid year. The year must be 2024 or later.")
                        continue

                    break
                except ValueError:
                    print("\tInvalid input. Please enter the date in the format: Month Day Year (example: 1 15 2024).")

        print("\tChoose Payment Option:")
        print("\t[1] Full Payment")
        print("\t[2] Down Payment")
        payment_choice = int(input("\tEnter (1-2): "))

        if payment_choice == 1:
            print(f"\tTotal Payment Amount: ${self.payment}")
            self.remaining_payment = 0 
        elif payment_choice == 2:
            down_payment = float(input("\tEnter down payment amount: $"))
            if down_payment > self.remaining_payment:
                print(f"\tYour down payment exceeds the total rental price. Here's your change: ${down_payment - self.remaining_payment}")
                down_payment = self.remaining_payment 
            self.remaining_payment -= down_payment  
            print(f"\tRemaining Payment: ${self.remaining_payment}")

        print(f"\n\tYour rental has been successfully confirmed!")
        print(f"\tYour rental end date is: {self.end_month}/{self.day}/{self.end_year}")

    def update_rental(self):
        self.name = input("\n\tEnter new Tenant Name: ")
        self.month, self.day, self.year = map(int, input("\tEnter new Rent Date (Month Day Year): ").split())
        print(f"\tUpdated rental information for apartment {self.num}.")

    def view_apartments(self):
        print(f"\n\tApartment Number: {self.num}")
        print(f"\tTenant Name: {self.name}")
        print(f"\tRent Date: {self.month}/{self.day}/{self.year}")
        print(f"\tRental End Date: {self.end_month}/{self.day}/{self.end_year}")
        print(f"\tRental Duration: {self.months} month(s)") 
        print(f"\tRental Price: ${self.price}")
        print(f"\tTotal Payment: ${self.payment}")
        print(f"\tRemaining Payment: ${self.remaining_payment}") 

    def end_rent(self, apartments):
        if self.num in apartments:
            del apartments[self.num]
            print(f"\n\tApartment {self.num} rental has ended and is now available again!")
        else:
            print("\tApartment not found!")

        print("\n\tEnding the rental process. Thank you for using our service!")

if __name__ == "__main__":
    main()