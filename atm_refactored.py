from collections import OrderedDict

class ATM():
    __atm_banknotes = OrderedDict(
        {"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0})
    __pw = "123456"

    def __init__(self, user_balance=0, atm_balance=OrderedDict(
        {"100": 50, "50": 50, "20": 50, "10": 50, "5": 50, "2": 50, "1": 50})):
       ATM.__atm_banknotes=atm_balance
       self.user_balance= user_balance

    @classmethod
    def banknotes_to_amount(cls, banknotes):
        amount=sum ([int(name)* val for name,val in banknotes.items()])
        return amount

    @classmethod
    def calc_banknotes(cls, amount):
        result = OrderedDict({"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0})
        for name in result.keys():
            result[name] = amount // int(name)
            amount = amount % int(name)
        return result

    def withdraw(self, request):
        print("Current balance is: " + str(self.user_balance))

        if request>self.user_balance or request>ATM.banknotes_to_amount(ATM.__atm_banknotes):
            print("Can't give you all this money !!")
            return

        request_banknotes = self.calc_banknotes(request)

        for name, val in request_banknotes.items():
            ATM.__atm_banknotes[name] = ATM.__atm_banknotes[name] - val

        self.user_balance=self.user_balance-request
        self.__give_cash(request_banknotes)
        
    def __give_cash(self, banknotes_to_withdraw):
        user_withdraw_banknotes=[( name, val) for name,val in banknotes_to_withdraw.items() if val>0]
        for ( name, val) in user_withdraw_banknotes:
            for _ in range(val):
                print ("Give "+ str(name))

    @classmethod
    def get_atm_available_money(cls, pw):
        if pw == ATM.__pw:
            print("Available money amount in the ATM: "+ str(ATM.banknotes_to_amount(ATM.__atm_banknotes)))
            print("Available money papers in the ATM: " + str(ATM.__atm_banknotes))
        else:
            print("You are not authorize for this operation")

#ATM().get_atm_available_money("123456")
balance=500
c = ATM(balance)
c.withdraw(277)
c.withdraw(30)
c.withdraw(5)
c.withdraw(500)
