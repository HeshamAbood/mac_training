from collections import OrderedDict

class ATM():

    def __init__(self, user_balance=0,bank_name="", atm_balance=OrderedDict(
        {"100": 50, "50": 50, "20": 50, "10": 50, "5": 50, "2": 50, "1": 50})):
       self.__atm_banknotes=atm_balance
       self.__user_balance= user_balance
       self.bank_name=bank_name
       print("Welcome to " +str(self.bank_name))

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
        print("Current balance is: " + str(self.__user_balance))

        if request>self.__user_balance:
            print("You don't have enough money")
            return

        if request>self.__banknotes_to_amount(self.__atm_banknotes):
            print("ATM has no sufficient money")
            return

        request_banknotes = self.__calc_banknotes(request)

        for name, val in request_banknotes.items():
            self.__atm_banknotes[name] = self.__atm_banknotes[name] - val

        self.__user_balance=self.__user_balance-request
        self.__give_cash(request_banknotes)
        
    def __give_cash(self, banknotes_to_withdraw):
        user_withdraw_banknotes=[( name, val) for name,val in banknotes_to_withdraw.items() if val>0]
        for ( name, val) in user_withdraw_banknotes:
            for _ in range(val):
                print ("Give "+ str(name))

balance1 = 500
atm1 = ATM(balance1, "Smart Bank")
atm1.withdraw(277)	
atm1.withdraw(800)

balance2 = 1000
atm2 = ATM(balance2, "Baraka Bank")
atm2.withdraw(100)
atm2.withdraw(2000)
