#zad6

nazwa = str(input("Wprowadź słowo: "))

def remove_outer_characters(nazwa):
    nazwa_2 = len(nazwa)
    return(nazwa[1:nazwa_2-1])
print(remove_outer_characters(nazwa))
