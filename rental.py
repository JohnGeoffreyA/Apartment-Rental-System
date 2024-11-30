        print("\tChoose Payment Option:")
        print("\t[1] Full Payment")
        print("\t[2] Down Payment")
        payment_choice = int(input("\tEnter (1-2): "))

        if payment_choice == 1:
            print(f"\tTotal Payment Amount: ${self.payment}")
            self.remaining_payment = 0
            down_payment = float(input("\tEnter down payment amount: $"))
            if down_payment > self.remaining_payment:
                print(f"\tYour down payment exceeds the total rental price. Here's your change: ${down_payment - self.remaining_payment}")
                down_payment = self.remaining_payment
            self.remaining_payment -= down_payment
            print(f"\tRemaining Payment: ${self.remaining_payment}")

        print(f"\n\tYour rental has been successfully confirmed!")
        print(f"\tYour rental end date is: {self.end_month}/{self.day}/{self.end_year}")