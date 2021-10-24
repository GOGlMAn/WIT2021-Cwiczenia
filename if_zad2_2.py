#Napisz skrypt w którym zdefiniujesz zmienne username = „Admin” i password = 
#„1234”. Przy pomocy nieskończonej pętli while przyjmuj od użytkownika login 
#oraz hasło tak długo dopóki użytkownik nie poda właściwych informacji.
user_usr = input("Podaj nazwę użytkownika: ")
user_pass = input("Podaj hasło: ")


while user_usr != "Admin" and user_pass != "1234":
    user_usr = input("Podaj nazwę użytkownika: ")
    user_pass = input("Podaj hasło: ")
    
print("Zalogowano")

