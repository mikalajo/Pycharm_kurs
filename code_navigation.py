

class Person_class:
    """Basisklasse, die eine allgemeine Person repräsentiert."""
    species = "Homo sapiens"  # Klassenvariable

    def __init__(self, name, age):
        """Initialisiert eine neue Person."""
        self.personen_name = name  # Instanzvariable
        self.age = age    # Instanzvariable


    def introduce(self):
        """Gibt eine Vorstellung der Person aus."""
        return f"Hi, ich heiße {self.personen_name} und bin {self.age} Jahre alt."
    # todo: walk funktion implementieren

class Employee(Person_class):
    """Unterklasse, die einen Angestellten repräsentiert."""
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id  # Instanzvariable
        self.department = department    # Instanzvariable

    def work(self):
        """Beschreibt die Tätigkeit eines Angestellten."""
        # fixme: work methode tut nicht
        return f"{self.personen_name} arbeitet im Bereich {self.department}."

    def introduce(self):
        """Überschreibt die Methode der Basisklasse, um zusätzliche Informationen hinzuzufügen."""
        base_introduction = super().introduce()
        return f"{base_introduction} Ich bin Angestellter mit der ID {self.employee_id}."

class Manager(Employee):
    """Unterklasse, die einen Manager repräsentiert."""
    def __init__(self, name, age, employee_id, department, team_size):
        """Initialisiert einen neuen Manager."""
        super().__init__(name, age, employee_id, department)
        self.team_size = team_size  # Instanzvariable

    def manage(self):
        """Beschreibt die Management-Tätigkeit."""
        return f"{self.personen_name} leitet ein Team von {self.team_size} Personen."

    def introduce(self):
        """Erweitert die Einführung um Management-Details."""
        base_introduction = super().introduce()
        return f"{base_introduction} Ich manage ein Team von {self.team_size} Personen."


# Beispielverwendung:
if __name__ == "__main__":
    person = Person_class("Alice", 30)
    print(person.introduce())

    employee = Employee("Bob", 35, "E123", "Entwicklung")
    print(employee.introduce())
    print(employee.work())

    manager = Manager("Clara", 40, "M456", "Marketing", 10)
    print(manager.introduce())
    print(manager.manage())
