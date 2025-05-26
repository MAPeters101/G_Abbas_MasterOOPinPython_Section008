class Account:
    def createAccount(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def createAccount(self, name, email, password, mobileno):
        self.name = name
        self.email = email
        self.password = password
        self.mobileno = mobileno

    def showData(self):
        print(self.name)
        print(self.email)
        print(self.password)
        print(self.mobileno)


acc = Account()
acc.createAccount("John", "john@gmail.com", "password", 123456789)
acc.showData()



