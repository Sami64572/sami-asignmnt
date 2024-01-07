class BankAccount:
    def __init__(self, account_number, balance, owner_name, pin):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner_name = owner_name
        self.__pin = pin

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_owner_name(self):
        return self.__owner_name

    def set_balance(self, new_balance):
    
        self.__balance = new_balance

    def set_owner_name(self, new_owner_name):
        
        self.__owner_name = new_owner_name

    def set_pin(self, new_pin):
    
        self.__pin = new_pin

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")
        print(f"Owner Name: {self.__owner_name}")

account = BankAccount(account_number="123456789", balance=1000.0, owner_name="John Doe", pin="1234")


print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())
print("Owner Name:", account.get_owner_name())


account.set_balance(1500.0)
account.set_owner_name("Jane Doe")
account.set_pin("5678")


account.display_account_info()