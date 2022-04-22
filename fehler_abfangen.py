#  Copyright (c) 2022 - Bastian Fischer. All rights reserved.

# Eingabe
print("Bitte geben sie eine ganze Zahl ein:")
z = input()

# Versuch der Umwandlung
try:
    zahl = int(z)
    print("Sie haben die ganze Zahl", zahl, "richtig eingegeben")

# Fehler bei der Umwandlung
except:
    print("Sie haben die ganze Zahl nicht richtig eingegeben")

print("Ende des Programms")
