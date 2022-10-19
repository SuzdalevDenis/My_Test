from Regist import Registration

class Regist_Auth(Registration):

    def __init__(self, login, password, repeat_password):
        self.repeat_password = repeat_password
        self.__RepPassword()
        Registration.__init__(self, login, password)

    def __RepPassword(self):
        if self.repeat_password != self.password:
            raise ValueError('Пароли не совпадают')
        Registration.save(self)

    def save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}'+'\n' == i:
                    raise ValueError('Такой есть')
        Registration.save(self)

    def show(self):
        return self.login, self.password


x = Regist_Auth(str(input('Enter login:')), str(input('Enter password:')), str(input('Repeat password: ')))
x.save()