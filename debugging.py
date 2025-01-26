import random
import time


def calculate_average(numbers):
    """Berechnet den Durchschnitt einer Liste von Zahlen."""
    if not numbers:
        raise ValueError("Die Liste der Zahlen darf nicht leer sein.")
    total = sum(numbers)
    count = len(numbers)
    average = total / count  # Fehlerquelle: Division durch Null vermeiden
    return average


def find_max_value(numbers):
    """Findet den größten Wert in einer Liste."""
    max_value = numbers[0]  # Annahme: Liste ist nicht leer
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def main():
    print("Starte Debugging-Demo...")

    # 1. Erzeuge eine zufällige Liste von Zahlen
    numbers = [random.randint(1, 100) for _ in range(10)]  # Füge hier Breakpoints hinzu

    print(f"Zahlenliste: {numbers}")

    # 2. Berechne den Durchschnitt
    try:
        average = calculate_average(numbers)
        print(f"Durchschnitt: {average}")
    except ValueError as e:
        print(f"Fehler: {e}")
    test = 10
    # 3. Finde den maximalen Wert
    max_value = find_max_value(numbers)
    print(f"Maximaler Wert: {max_value}")

    # 4. Simuliere einen Fehlerfall
    try:
        print("Teste mit einer leeren Liste...")
        empty_average = calculate_average([])  # Sollte einen Fehler auslösen
        print(f"Durchschnitt der leeren Liste: {empty_average}")
    except ValueError as e:
        print(f"Erwarteter Fehler: {e}")

    # 5. Untersuche eine Schleife mit bedingtem Debugging
    print("Prüfe Zahlen auf Teilbarkeit durch 3...")
    divisible_by_three = [num for num in numbers if num % 3 == 0]
    print(f"Zahlen, die durch 3 teilbar sind: {divisible_by_three}")

print("master3 branch")

if __name__ == "__main__":
    main()
