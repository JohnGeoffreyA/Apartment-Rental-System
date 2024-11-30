    def update_rental(self):
        self.name = input("\n\tEnter new Tenant Name: ")
        self.month, self.day, self.year = map(int, input("\tEnter new Rent Date (Month Day Year): ").split())
        print(f"\tUpdated rental information for apartment {self.num}.")
