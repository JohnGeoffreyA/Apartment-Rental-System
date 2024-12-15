import csv

def main():
    apartments = load_apartments()
    studio_count = 0
    one_bedroom_count = 0
    two_bedroom_count = 0
    
    while True:
        print("\n\t\t\t|--------------------------------------------------------------------|")
        print("\t\t\t|                            Apartment Rentals                       |")
        print("\t\t\t|--------------------------------------------------------------------|")
        print("\t\t\t|\t\t\t\t\t\t\t     |")
        print("\t\t\t|    [1] Rent Apartment\t\t        [4] View All Apartments      |")
        print("\t\t\t|    [2] Update Rental Information\t[5] Exit                     |")
        print("\t\t\t|    [3] End Rent\t\t\t\t\t     |")
        print("\t\t\t|--------------------------------------------------------------------|")
        try:
            choice = int(input("\tEnter your choice: "))
        except ValueError:
            print("\tInvalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            apartment = Apartment()
            apartment.rent_apartment(apartments)
            apartments[apartment.num] = apartment
            if apartment.type == "Studio":
                studio_count += 1
            elif apartment.type == "1-Bedroom":
                one_bedroom_count += 1
            elif apartment.type == "2-Bedroom":
                two_bedroom_count += 1
        elif choice == 2:
            try:
                apartment_number = int(input("\n\tEnter the Apartment Number to Update: "))
                if apartment_number in apartments:
                    apartments[apartment_number].update_rental()
                else:
                    print("\tApartment not found!")
            except ValueError:
                print("\tInvalid input. Please enter a valid apartment number.")
        elif choice == 3:
            try:
                apartment_number = int(input("\n\tEnter the Apartment Number to End Rent: "))
                if apartment_number in apartments:
                    
                    apartment_type = apartments[apartment_number].type
                    if apartment_type == "Studio":
                        studio_count -= 1
                    elif apartment_type == "1-Bedroom":
                        one_bedroom_count -= 1
                    elif apartment_type == "2-Bedroom":
                        two_bedroom_count -= 1

                    apartments[apartment_number].end_rent(apartments)
                else:
                    print("\tApartment not found!")
            except ValueError:
                print("\tInvalid input. Please enter a valid apartment number.")
        elif choice == 4:
            if apartments:
                print("\n\tRented Apartments:")
                for apartment in apartments.values():
                    apartment.view_apartments()

                print("\n\tAvailable Apartments:")
                print(f"\tStudio Apartments Available: {10 - studio_count}")
                print(f"\t1-Bedroom Apartments Available: {10 - one_bedroom_count}")
                print(f"\t2-Bedroom Apartments Available: {10 - two_bedroom_count}\n")
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
    def __init__(self, num=0, name="", month=0, day=0, year=0, months=0, price=0.0, type="", payment=0.0, remaining_payment=0.0, features=""):
        self.num = num
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.months = months
        self.end_month = 0
        self.end_year = 0
        self.type = type
        self.price = price
        self.payment = payment
        self.remaining_payment = remaining_payment
        self.features = features


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
        while not self.name.strip():
            print("\tTenant name cannot be empty. Please enter a valid name.")
            self.name = input("\tEnter Tenant Name: ")

        while True:
            try:
                rent_date = input("\tEnter Rent Date (MM/DD/YYYY): ")

                self.month, self.day, self.year = map(int, rent_date.split("/"))

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
                print("\tInvalid input. Please enter the date in the format: MM/DD/YYYY (example: 01/15/2024).")

        while True:
            print("\tWhat type of apartment would you like?")
            print("\t[1] Studio - $1000 (Includes: 1 room with combined bedroom, small kitchen, and bathroom)")
            print("\t[2] 1-Bedroom - $2000 (Includes: 1 bedroom, living room, kitchen, and bathroom)")
            print("\t[3] 2-Bedroom - $3000 (Includes: 2 bedrooms, living room, kitchen, and bathroom)")
            try:
                apartment_type = int(input("\tEnter (1-3): "))
                if apartment_type == 1:
                    self.type = "Studio"
                    self.price = 1000.0
                    self.features = "Includes: 1 room with combined bedroom, small kitchen, and bathroom"
                    break
                elif apartment_type == 2:
                    self.type = "1-Bedroom"
                    self.price = 2000.0
                    self.features = "Includes: 1 bedroom, living room, kitchen, and bathroom"
                    break
                elif apartment_type == 3:
                    self.type = "2-Bedroom"
                    self.price = 3000.0
                    self.features = "Includes: 2 bedrooms, living room, kitchen, and bathroom"
                    break
                else:
                    print("\tInvalid input. Please choose from (1-3).")
            except ValueError:
                print("\tInvalid input. Please enter a number (1-3).")

        while True:
            try:
                self.months = int(input("\tEnter rental duration in months: "))
                if self.months > 0:
                    break
                else:
                    print("\tRental duration must be a positive number.")
            except ValueError:
                print("\tInvalid input. Please enter a valid number of months.")

        self.payment = self.price * self.months
        self.remaining_payment = self.payment  
        print(f"\tTotal Payment Amount: ${self.payment}")

        total_months = self.month + self.months - 1
        self.end_year = self.year + (total_months // 12)
        self.end_month = (total_months % 12) + 1

        print("\tChoose Payment Option:")
        print("\t[1] Full Payment")
        print("\t[2] Down Payment")
        while True:
            try:
                payment_choice = int(input("\tEnter (1-2): "))
                if payment_choice == 1:
                    print(f"\tTotal Payment Amount: ${self.payment}")
                    self.remaining_payment = 0
                    break
                elif payment_choice == 2:
                    while True:
                        try:
                            down_payment = float(input("\tEnter down payment amount: $"))
                            if down_payment > self.payment:
                                print(f"\tYour down payment exceeds the total rental price. Here's your change: ${down_payment - self.payment}")
                                down_payment = self.payment
                            self.remaining_payment -= down_payment
                            print(f"\tRemaining Payment: ${self.remaining_payment}")
                            break
                        except ValueError:
                            print("\tInvalid input. Please enter a valid amount.")
                    break
                else:
                    print("\tInvalid input. Please choose from (1-2).")
            except ValueError:
                print("\tInvalid input. Please enter a number (1-2).")

        print(f"\n\tYour rental has been successfully confirmed!")
        print(f"\tYour rental end date is: {self.end_month}/{self.day}/{self.end_year}")

    def update_rental(self):
        self.name = input("\n\tEnter new Tenant Name: ").strip()
        while True:
            try:
                self.month, self.day, self.year = map(int, input("\tEnter new Rent Date (Month Day Year): ").split("/"))
                if 1 <= self.month <= 12 and 1 <= self.day <= 31 and self.year > 2023:
                    break
                else:
                    print("\tInvalid date. Please enter a valid date.")
            except ValueError:
                print("\tInvalid input. Please enter the date in the format: Month Day Year (example: 1/15/2024).")
        
        print("\n\tWhat type of apartment would you like?")
        print("\t[1] Studio - $1000 (Includes: 1 room with combined bedroom, small kitchen, and bathroom)")
        print("\t[2] 1-Bedroom - $2000 (Includes: 1 bedroom, living room, kitchen, and bathroom)")
        print("\t[3] 2-Bedroom - $3000 (Includes: 2 bedrooms, living room, kitchen, and bathroom)")
        while True:
            try:
                apartment_type = int(input("\tEnter (1-3): "))
                if apartment_type == 1:
                    self.type = "Studio"
                    self.price = 1000.0
                    self.features = "Includes: 1 room with combined bedroom, small kitchen, and bathroom"
                    break
                elif apartment_type == 2:
                    self.type = "1-Bedroom"
                    self.price = 2000.0
                    self.features = "Includes: 1 bedroom, living room, kitchen, and bathroom"
                    break
                elif apartment_type == 3:
                    self.type = "2-Bedroom"
                    self.price = 3000.0
                    self.features = "Includes: 2 bedrooms, living room, kitchen, and bathroom"
                    break
                else:
                    print("\tInvalid input. Please choose from (1-3).")
            except ValueError:
                print("\tInvalid input. Please enter a number (1-3).")
        
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
        print(f"\tApartment Type: {self.type}")
        print(f"\tApartment Features: {self.features}")

    def end_rent(self, apartments):
    
        if self.num in apartments:
            del apartments[self.num]  
            print(f"Apartment {self.num} rental has ended and is now available again!")
        else:
            print(f"Apartment {self.num} not found!")
        
def save_apartments(apartments):
    try:
        with open('rental.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(["Apartment Number", "Tenant Name", "Rent Date", "Rental End Date", "Duration (months)", "Price", "Remaining Payment", "Apartment Type", "Apartment Features"])
            for apartment in apartments.values():
                writer.writerow([
                    apartment.num,
                    apartment.name,
                    f"{apartment.month}/{apartment.day}/{apartment.year}",
                    f"{apartment.end_month}/{apartment.day}/{apartment.end_year}",
                    apartment.months,
                    apartment.price,
                    apartment.remaining_payment,
                    apartment.type,  
                    apartment.features  
                ])
        print("\n\tApartment data successfully saved to 'rental.csv'.")
    except Exception as e:
        print(f"\n\tAn error occurred while saving to 'rental.csv': {e}")

def load_apartments():
    apartments = {}
    try:
        with open('rental.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                apartment = Apartment()
                apartment.num = int(row["Apartment Number"])  
                apartment.name = row["Tenant Name"]
                rent_date = row["Rent Date"].split("/")
                apartment.month, apartment.day, apartment.year = map(int, rent_date)
                end_date = row["Rental End Date"].split("/")
                apartment.end_month, apartment.day, apartment.end_year = map(int, end_date)
                apartment.months = int(row["Duration (months)"])
                apartment.price = float(row["Price"])
                apartment.remaining_payment = float(row["Remaining Payment"])
                apartment.type = row["Apartment Type"]
                apartment.features = row["Apartment Features"]
                apartments[apartment.num] = apartment  
        print("\n\tApartment data successfully loaded from 'rental.csv'.")
    except FileNotFoundError:
        print("\n\t'rental.csv' not found. Starting with an empty apartment list.")
    except Exception as e:
        print(f"\n\tAn error occurred while loading 'rental.csv': {e}")
    return apartments

if __name__ == "__main__":
    main()
