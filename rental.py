    def end_rent(self, apartments):
        if self.num in apartments:
            del apartments[self.num]
            print(f"\n\tApartment {self.num} rental has ended and is now available again!")
        else:
            print("\tApartment not found!")

        print("\n\tEnding the rental process. Thank you for using our service!")