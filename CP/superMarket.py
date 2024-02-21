class superMarket:
    def __init__ (self):
        self.stock = {}

    def inventory(self):
        for key, value in self.stock.items():
            print(f"{key}: {value}")
    
    def buyForVendor(self):
        pass

class signUp:

    def __init__ (self,name,email_id,password):
        self.name = name
        self.email_id = email_id
        self.password = password

    def checkName(self):
        return self.name.isalpha()
    def checkEmailId(self):
        return self.email_id.islower().endswith('@gmail.com')
    def checkPassword(self):
        d = 0
        u = 0
        l = 0
        s = 0
        if len(self.password) < 8:
            print("Minimum password length is 8")
            return False
        for i in self.password:
            if i.isdigit():
                d += 1
            if i.isalpha() and i.islower():
                l += 1
            if i.isalpha() and i.isupper():
                u += 1
            if not (i.isalpha() or i.isdigit() or i == ' '):
                s += 1
        if (d>0 and u>0 and l>0 and s>0):
            print("Login Successful")
            return True
        print("Invalid password")
        return False
        
    def login(self):
        self.checkName()
        if self.checkName():
            if self.checkEmailId():
                self.checkPassword()

    

        

name = input("Name: ")
email_id = input("Email id: ")
password = input("Password: ")
signup = signUp(name,email_id,password)
signup.login()