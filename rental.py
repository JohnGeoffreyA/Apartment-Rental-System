    def view_apartments(self):
        print(f"\n\tApartment Number: {self.num}")
        print(f"\tTenant Name: {self.name}")
        print(f"\tRent Date: {self.month}/{self.day}/{self.year}")
        print(f"\tRental End Date: {self.end_month}/{self.day}/{self.end_year}")
        print(f"\tRental Duration: {self.months} month(s)")
        print(f"\tRental Price: ${self.price}")
        print(f"\tTotal Payment: ${self.payment}")
        print(f"\tRemaining Payment: ${self.remaining_payment}")