from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Mitarbeiter(Person):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender)
        self.abteilung = None
        self.set_abteilung(abteilung)

    def set_abteilung(self, abteilung):
        self.abteilung = abteilung
        abteilung.add_mitarbeiter(self)


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender, abteilung)
        self.leitet_abteilung = None
        self.set_abteilungsleiter(abteilung)

    def set_abteilungsleiter(self, abteilung):
        self.leitet_abteilung = abteilung
        abteilung.set_leiter(self)


class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def set_leiter(self, leiter):
        self.leiter = leiter

    def get_mitarbeiter_count(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def get_mitarbeiter_count(self):
        return sum(len(abt.mitarbeiter) for abt in self.abteilungen)

    def get_abteilungsleiter_count(self):
        return sum(1 for abt in self.abteilungen if abt.leiter is not None)

    def get_abteilungen_count(self):
        return len(self.abteilungen)

    def get_largest_abteilung(self):
        return max(self.abteilungen, key=lambda abt: abt.get_mitarbeiter_count())

    def get_gender_distribution(self):
        total_mitarbeiter = self.get_mitarbeiter_count()
        if total_mitarbeiter == 0:
            return {"Male": 0, "Female": 0}
        male_count = sum(
            1 for abt in self.abteilungen for mit in abt.mitarbeiter if mit.gender == Gender.MALE
        )
        female_count = total_mitarbeiter - male_count
        return {
            "Male": male_count / total_mitarbeiter * 100,
            "Female": female_count / total_mitarbeiter * 100,
        }


if __name__ == "__main__":
    # Beispiel zur Nutzung der Klassen
    firma = Firma("Cola")

    # Abteilungen erstellen
    entwicklung = Abteilung("Entwicklung")
    vertrieb = Abteilung("Vertrieb")

    firma.add_abteilung(entwicklung)
    firma.add_abteilung(vertrieb)

    # Mitarbeiter und Abteilungsleiter erstellen
    m1 = Mitarbeiter("Alice", Gender.FEMALE, entwicklung)
    m2 = Mitarbeiter("Bob", Gender.MALE, entwicklung)
    m3 = Mitarbeiter("Charlie", Gender.MALE, vertrieb)

    leiter_entwicklung = Abteilungsleiter("Diana", Gender.FEMALE, entwicklung)

    # Ergebnisse
    print(f"Anzahl der Mitarbeiter: {firma.get_mitarbeiter_count()}")
    print(f"Anzahl der Abteilungsleiter: {firma.get_abteilungsleiter_count()}")
    print(f"Anzahl der Abteilungen: {firma.get_abteilungen_count()}")

    largest_abt = firma.get_largest_abteilung()
    if largest_abt:
        print(f"Größte Abteilung: {largest_abt.name} mit {largest_abt.get_mitarbeiter_count()} Mitarbeitern")

    gender_dist = firma.get_gender_distribution()
    print(f"Geschlechterverteilung: {gender_dist['Male']:.2f}% Männer, {gender_dist['Female']:.2f}% Frauen")
