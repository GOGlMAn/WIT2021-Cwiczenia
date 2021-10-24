#Napisz skrypt który przyjmie od użytkownika informację na temat jego wieku i w 
#zależności od tej informacji poda jedną z trzech opcji:
#- Jeżeli ktoś ma powyżej 21 lat: „Możesz prowadzić samochód oraz głosować w 
#wyborach”
#- Jeżeli ktoś ma powyżej 17 lat ale mniej niż 21 lat: „Możesz prowadzić samochód”
#- W innym wypadku: „Nie możesz głosować ani prowadzić samochodu”

age = int(input("Podaj swój wiek: "))

if age >= 21:
    print("Możesz prowadzić samochód oraz głosować w wyborach")
elif age > 17 and age < 21:
    print("Możesz prowadzić samochód")
else:
    print("Nie możesz głosować ani prowadzić samochodu")
