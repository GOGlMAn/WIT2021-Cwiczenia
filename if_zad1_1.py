# Napisz skrypt który przyjmie od użytkownika informację na temat jego wieku i na 
#podstawie tej informacji wydrukuje na ekranie „Jesteś pełnoletni/-a” lub „Nie masz 
#ukończonych 18 lat”

age = int(input("Podaj swój wiek: "))

if age >= 18:
    print("Jesteś pełnoletni/a")
else:
    print("Nie masz ukończonych 18 lat")
