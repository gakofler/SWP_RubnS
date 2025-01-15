class Auto:
    def __init__(self, ps):
        if not isinstance(ps, (int, float)):
            raise ValueError("PS muss eine Zahl sein.")
        if ps < 0:
            raise ValueError("PS darf nicht negativ sein.")
        self.ps = ps

    def __add__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Addition ist nur mit anderen Auto-Objekten möglich.")
        return self.ps + other.ps

    def __sub__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Subtraktion ist nur mit anderen Auto-Objekten möglich.")
        return self.ps - other.ps

    def __mul__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Multiplikation ist nur mit anderen Auto-Objekten möglich.")
        return self.ps * other.ps

    def __eq__(self, other):
        if not isinstance(other, Auto):
            return False
        return self.ps == other.ps

    def __lt__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Vergleich ist nur mit anderen Auto-Objekten möglich.")
        return self.ps < other.ps

    def __gt__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Vergleich ist nur mit anderen Auto-Objekten möglich.")
        return self.ps > other.ps

    def __len__(self):
        return self.ps

    def __repr__(self):
        return f"Auto({self.ps} PS)"


# Testzeilen
if __name__ == "__main__":
    # Objekte erstellen
    a1 = Auto(50)
    a2 = Auto(60)
    a3 = Auto(50)

    # Addition
    print(a1 + a2)  # 110

    # Subtraktion
    print(a2 - a1)  # 10

    # Multiplikation
    print(a1 * a2)  # 3000

    # Vergleichsoperationen
    print(a1 == a3)  # True
    print(a1 < a2)   # True
    print(a2 > a3)   # True

    # Länge (PS-Wert als Länge)
    print(len(a1))   # 50

    # Repräsentation
    print(a1)        # Auto(50 PS)

    # Fehlerhafte Operationen
    try:
        print(a1 + 10)  # Fehler
    except TypeError as e:
        print(e)

    try:
        print(a1 < 10)  # Fehler
    except TypeError as e:
        print(e)
