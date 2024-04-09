class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.users = {}
    
    def addUser(self):
        if self.username not in self.users:
            self.users[self.username] = self.password
            print( "register is access")
        else:
            print("user in use")




if __name__ == "__main__":

    # Luodaan käyttäjäolio ja pyydetään käyttäjältä käyttäjätunnus ja salasana
   
    username = input("Syötä käyttäjätunnus: ")
    password = input("Syötä salasana: ")

    # Lisätään käyttäjä annetuilla tiedoilla
    new_user = User(username, password)
    new_user.addUser()

    
