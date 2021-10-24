#Napisz skrypt który przyjmie od użytkownika informację na temat kapitału 
#początkowego, miesięcznych wpływów, okresu inwestowania w miesiącach oraz 
#pożądanej końcowej wartości inwestycji. Przyjmij, że na koniec naliczany jest profit w 
#wysokości 2% od całości obecnego kapitału. Program ma za zadanie obliczyć ilość
#pieniędzy po upływie podanej liczby miesięcy oraz zwrócić informację czy jest ona 
#większa czy mniejsza niż pożądana końcowa wartość inwestycji.

capital = float(input("Wielkość początkowego kapitału: "))
income = float(input("Wielkość miesięcznych wpływów: "))
time = int(input("Ile miesięcy ma trwać inwestycja: "))
wish_capital = float(input("Ile chciałbyś/chciałabyś osiągnąć na koniec inwestycji: "))
end_capital = (capital + (income * time)) * 1.02

if end_capital < wish_capital:
    print("Nie udało Ci się osiągnąć zamierzonej kwoty!")
else:
    print("Udało Ci się osiągnąć zamierzoną kwotę!")
