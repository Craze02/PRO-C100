class atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def cashwithdrawal(self, balance):
        remainingBalance = 1000 - balance
        print("You withdrew: " +str(balance)+ ". Your remaining balance is: " +str(remainingBalance))

    def balanceinquiry(self):
        print("Balance : 1000 ")
    

def main():
    cardNumber = input("Enter your card number : ")
    pin = input("Enter your pin : ")

    userDetails = atm(cardNumber, pin)

    print("What service would you like to use?")
    print("Balance Inquiry(Service number 1) or Cash withdrawal(Service number 2)")
    service = int(input("Enter service number: "))

    if(service == 1):
        userDetails.balanceinquiry()
    elif (service == 2):
        amount =int(input("Enter withdrawal amount "))
        userDetails.cashwithdrawal(amount)
    else:
        print("Wrong input please try again")

if __name__ == "__main__":
    main()