#Przyjmij że z miejscowości A do miejscowości B jest 250km które pociąg pokonuje w 
#2h 45min. Użytkownik chciałby pokonać ten dystans samochodem. Napisz skrypt, 
#który pozwoli użytkownikowi wpisać informację na temat przypuszczanej średniej 
#prędkości na tej trasie, a następnie zwróci informację czy dojedzie on wolniej czy 
#szybciej niż pociąg.

distance = int(250)
avg_speed = int(input("Podaj z jaką średnią prędkością będziesz jechał/a: "))
time_train = float(2.45)

time_car = distance / avg_speed

if time_car < time_train:
    print("Pdróż samochodem jest szybsza")
else:
    print("Podróż pociągiem jest szybsza")
