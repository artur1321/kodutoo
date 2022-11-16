
#15.11.22
#kodutoo

#tegin kysimused
a = int(input("kui te soovite kalkuleerida EUR>EEK, siis vajutage number '1' kui te soovite kalkuleerida EEK>EUR, siis vajutage number '2': "))
b = float(input("palju yhikud soovite kalkuleerida: "))

#tegin arvutused
if a == 1:
    print(round(15.64664*b,2))
elif a == 2:
    print(round(b*0.063911485,2))
else:
    print("Valuuta valik oli vale")

    
    
    