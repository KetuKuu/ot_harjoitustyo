class User:

    def __init__(self, username, password):
        

        self.username = username
        self.password = password
        #self.email = email
        print("User")
    def change_password(self, new_password):
        self.password = new_password


    #def update_email(self, new_email):
        #self.email = new_email
    