
class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__LenPassword()
        self.__PasswordComplexity()

    def __LenPassword(self):
        if len(self.password) < 8:
            raise ValueError('Слабый пароль')

    def __PasswordComplexity(self):
        self.password_complexity = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        for j in n:
            #if '1234567890' not in self.password:
            raise ValueError('Weak password')

    def save(self):
        with open('users', 'a') as r:
            r.write(f'{self.login, self.password}'+'\n')


