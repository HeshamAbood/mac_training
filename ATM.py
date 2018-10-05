import collections

class ATM():
    __available_money_USD =  collections.OrderedDict({"100": 50, "50": 50, "20": 50, "10": 50, "5": 50, "2": 50, "1": 50})

    def __clac_banknotes(self, amount):
        result =  collections.OrderedDict({"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0})

        for name in result.keys():
            result[name] = amount // int(name)
            amount = amount % int(name)

        return result

    def withdraw(self,  amount):
        user_wthdraw_amount = amount

        user_withdraw = self.__clac_banknotes(amount)

        for name, val in user_withdraw.items():
            ATM.__available_money_USD[name] = ATM.__available_money_USD[name] - val

        print("withdraw amount is:" + str(user_wthdraw_amount))
        print("withdraw banknotes details:" + str(user_withdraw))


s=ATM()
s.withdraw(377)


