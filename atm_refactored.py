import collections


class ATM():
    __available_money_banknotes_USD = collections.OrderedDict(
        {"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0})
    __pw = "123456"

    def __init__(self, user_balance=0, atm_balance=collections.OrderedDict(
        {"100": 50, "50": 50, "20": 50, "10": 50, "5": 50, "2": 50, "1": 50})):

       '''initailze the ATM banknotes ''' 
       ATM.__available_money_banknotes_USD=atm_balance

       '''Set user balance'''
       self.user_balance= user_balance

    @classmethod
    def banknotes_to_amount(cls, banknotes):
        amount=sum ([int(name)* val for name,val in banknotes.items()])
        return amount

    @classmethod
    def calc_banknotes(cls, amount):
        '''claculate the corresponding money papers for the givin amount '''
        result = collections.OrderedDict({"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0})

        for name in result.keys():
            result[name] = amount // int(name)
            amount = amount % int(name)

        return result

    def withdraw(self, request):
        print("Current balance is: " + str(self.user_balance))

        if request>self.user_balance or request>ATM.banknotes_to_amount(ATM.__available_money_banknotes_USD):
            print("Can't give you all this money !!")
            return

        user_withdraw_banknotes = self.calc_banknotes(request)

        #exclud the request amount from ATM available money
        for name, val in user_withdraw_banknotes.items():
            ATM.__available_money_banknotes_USD[name] = ATM.__available_money_banknotes_USD[name] - val

        #exclud the request amount from user balance    
        self.user_balance=self.user_balance-request

        for ( name, val) in [( name, val) for name,val in user_withdraw_banknotes.items() if val>0]:
            for _ in range(val):
                print ("Give "+ str(name))


    @classmethod
    def get_atm_available_money(cls, pw):
        if pw == ATM.__pw:
            print("Available money amount in the ATM: "+ str(ATM.banknotes_to_amount(ATM.__available_money_banknotes_USD)))
            print("Available money papers in the ATM: " + str(ATM.__available_money_banknotes_USD))
        else:
            print("You are not authorize for this operation")


#ATM().get_atm_available_money("123456")
balance=500
c = ATM(balance)
c.withdraw(277)
c.withdraw(30)
c.withdraw(5)
c.withdraw(500)
