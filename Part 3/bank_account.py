class Account:
    def __init__(self, id_account, holder, balance, limit):
        self.__id_account = id_account
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    # Methods in account

    def extract(self):
        return print("The balance of {} is: {}".format(self.__holder, self.__balance))

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        if self.__can_withdraw(value):
            self.__balance -= value
        else:
            print("The amount to be withdrawn ({}) exceeded the available limit".format(value))

    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)

    def __can_withdraw(self, value):
        value_available = self.__balance + self.__limit
        return value <= value_available

    # Properties

    @property
    def __id_account(self):
        return self.__id_account

    @property
    def __holder(self):
        return self.__holder

    @property
    def __balance(self):
        return self.__balance

    @property
    def __limit(self):
        return self.__limit

    #  Setter

    @__limit.setter
    def __limit(self, n_limit):
        self.__limit = n_limit

    # Static Methods

    @staticmethod
    def banks_code():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @staticmethod
    def bank_code():
        return "001"
