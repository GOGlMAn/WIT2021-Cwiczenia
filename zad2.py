#zad2

lista = [4, 7, 89, -4, 356, 0, 1]


def find_min():
    min_var = 0
    for i in lista:
        if min_var == None or min_var > i:
            min_var = i
    return min_var

print (find_min())
