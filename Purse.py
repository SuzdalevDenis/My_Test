class Purse:

    def __init__(self, valuta, name="UNKNOW"):
        if valuta not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    def top_down_balance_valuta(self, howmany):
        if self.__money - howmany < 0:
            print('Не достаточно средств')
            raise ValueError('Не достаточно средств')
        self.__money = self.__money - howmany
        return howmany

    def from_purse_to_purse(self, howmany_purse):
        if self.__money - howmany_purse < 0:
            print('Не достаточно средств')
            raise ValueError('Не достаточно средств')
        self.__money = self.__money - howmany_purse
        return howmany_purse

    def from_USD_to_EUR(self, howmany_USD):
        if self.__money - howmany_USD < 0:
            print('Не достаточно средств')
            raise ValueError('Не достаточно средств')
        self.__money = self.__money - howmany_USD
        howmany_USD *= 1.026
        return howmany_USD

    def from_EUR_to_USD(self, howmany_EUR):
        if self.__money - howmany_EUR < 0:
            print('Не достаточно средств')
            raise ValueError('Не достаточно средств')
        self.__money = self.__money - howmany_EUR
        howmany_EUR *= 0.9737
        return howmany_EUR

    def info(self):
        print(self.__money, self.valuta)

    def __del__(self):
        print('Purse delete')
        return self.__money


u = Purse('USD')
i = Purse('EUR', "Bill")
p = Purse('USD', 'Rei')
u.top_up_balance(round(float(input('Howmany up?: ')), 2))
i.top_up_balance(round(u.from_USD_to_EUR(float(input('Howmany down?: '))), 2))
u.from_purse_to_purse(round(p.top_up_balance(float(input('Howmany up to purse?: '))), 2))
u.info()
i.info()
p.info()