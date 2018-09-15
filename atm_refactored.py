import collections


class ATM():
    __available_money_banknotes_USD = collections.OrderedDict(
        {"100": 50, "50": 50, "20": 50, "10": 50, "5": 50, "2": 50, "1": 50})
    __pw = "123456"

    @staticmethod
    def calc_banknotes( amount):
        result = collections.OrderedDict({"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0})

        for name in result.keys():
            result[name] = amount // int(name)
            amount = amount % int(name)

        return result

    def withdraw(self, amount):
        user_withdraw_amount = amount

        user_withdraw = self.calc_banknotes(amount)

        for name, val in user_withdraw.items():
            ATM.__available_money_banknotes_USD[name] = ATM.__available_money_banknotes_USD[name] - val

        print("withdraw amount is:" + str(user_withdraw_amount))
        print("withdraw banknotes details:" + str(user_withdraw))

    @classmethod
    def get_atm_available_money(cls, pw):
        if pw == ATM.__pw:
            print("available money in the ATM: " + str(ATM.__available_money_banknotes_USD))
        else:
            print("You are not authorize for this operation")


ATM().get_atm_available_money("123456")
s = ATM()
s.withdraw(377)
