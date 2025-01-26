import math  # Mehrere Imports in einer Zeile (gegen PEP 8)


def myFunction(a, m=None):  # Falsche Benennung und Leerzeichen
    result = a + m  # Falsche Einrückung
    return (result)  # Unnötige Klammern


x = 42  # Unnötige Leerzeichen
y = 23  # Fehlender Abstand um den Operator
z = myFunction(x, y)  # Falsches Leerzeichen in Funktionsaufruf


def calculateSum(numbers):  # Falscher Funktionsname
    sum = 0  # Lokale Variable überschreibt eingebauten Namen 'sum'
    for i in numbers: sum += i  # Schlechte Lesbarkeit durch fehlende Einrückung
    return sum


listOfNumbers = [1, 2, 3, 4]  # Unregelmäßige Leerzeichen in der Liste

# Unnötiger Kommentar, der den Code beschreibt
# Diese Schleife iteriert über die Liste und gibt jedes Element aus
for num in listOfNumbers: print(num)  # Fehlendes Leerzeichen nach dem Doppelpunkt

# Veraltete Funktion
time = math.clock()  # 'clock()' ist in Python 3.8+ veraltet
