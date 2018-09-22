from collections import OrderedDict
from ATMError import ATMError

class ATM():

    def __init__(self, user_balance=0,bank_name="", atm_balance=OrderedDict(
        {"100": 50, "50": 50, "20": 50, "10": 50, "5": 50, "2": 50, "1": 50})):
       self.__atm_banknotes=atm_balance
       self.__user_balance= user_balance
       self.bank_name=bank_name
       self.__withdrawals_list = []
       print("Welcome to " +str(self.bank_name))
       self.show_user_balance()

    def __banknotes_to_amount(self, banknotes):
        amount=sum ([int(name)* val for name,val in banknotes.items()])
        return amount

    def __calc_banknotes(self, amount):
        result = OrderedDict({"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0})
        for name in result.keys():
            result[name] = amount // int(name)
            amount = amount % int(name)
        return result

    def withdraw(self, request):
        if request>self.__user_balance:
            raise( ATMError("You don't have enough money"))

        if request>self.__banknotes_to_amount(self.__atm_banknotes):
            raise (ATMError("ATM has no sufficient money"))

        request_banknotes = self.__calc_banknotes(request)

        for name, val in request_banknotes.items():
            self.__atm_banknotes[name] = self.__atm_banknotes[name] - val

        self.__user_balance=self.__user_balance - request
        self.__give_cash(request_banknotes)
        
        self.__withdrawals_list.append(request)
        self.show_user_balance()

    def __give_cash(self, banknotes_to_withdraw):
        user_withdraw_banknotes=[( name, val) for name,val in banknotes_to_withdraw.items() if val>0]
        for ( name, val) in user_withdraw_banknotes:
                print ("Give %s$" %name, end=", ")
        
    def show_withdrawals(self):
        print("All withdrawals are: ", end=": ")
        for i,withdrawal in enumerate (self.__withdrawals_list):
            if i==len(self.__withdrawals_list)-1:
                print("%d$" %withdrawal)
            else:
                print("%d$" %withdrawal, end=', ')

    def show_user_balance(self):
        print("Current balance is: " + str(self.__user_balance))


balance1 = 500
atm1 = ATM(balance1, "Smart Bank")
for i in range(1,3):
    try:
        print("Request withdaraw %d$" %(60*i),end=" -> ")
        atm1.withdraw(60*i)
    except ATMError as e:
                print("Operation failed",e.value)

atm1.show_withdrawals()

print("-"*60)

balance2 = 1000
atm2 = ATM(balance2, "Baraka Bank")
for i in range(1,5):
    try:
        print("Request withdaraw %d$" %(70*i),end=" -> ")
        atm2.withdraw(70*i)
    except ATMError as e:
                print("Operation failed",e.value)
try:
    print("Request withdaraw %d$" %2000,end=" -> ")
    atm2.withdraw(2000)
except ATMError as e:
            print("Operation failed",e.value)

atm2.show_withdrawals()
