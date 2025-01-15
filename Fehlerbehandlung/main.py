import sys

# Definition der Basisklasse Fahrzeug
class Fahrzeug:
    def __init__(self, marke, modell):
        # Initialisiert die Marke und das Modell eines Fahrzeugs
        self.marke = marke
        self.modell = modell

    def beschreibung(self):
        # Gibt eine allgemeine Beschreibung des Fahrzeugs zurück
        return f"Fahrzeug: {self.marke} {self.modell}"


# Definition der abgeleiteten Klasse Auto
class Auto(Fahrzeug):
    def __init__(self, marke, modell, anzahl_tueren):
        # Ruft den Konstruktor der Basisklasse auf
        super().__init__(marke, modell)
        # Initialisiert die Anzahl der Türen
        self.anzahl_tueren = anzahl_tueren

    def beschreibung(self):
        # Gibt eine spezifische Beschreibung des Autos zurück
        return f"Auto: {self.marke} {self.modell} mit {self.anzahl_tueren} Türen"


# Definition der abgeleiteten Klasse Motorrad
class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, hubraum):
        # Ruft den Konstruktor der Basisklasse auf
        super().__init__(marke, modell)
        # Initialisiert den Hubraum des Motorrads
        self.hubraum = hubraum

    def beschreibung(self):
        # Gibt eine spezifische Beschreibung des Motorrads zurück
        return f"Motorrad: {self.marke} {self.modell} mit {self.hubraum}cc Hubraum"


# Definition der abgeleiteten Klasse ElektroAuto
class ElektroAuto(Auto):
    def __init__(self, marke, modell, anzahl_tueren, batterie_kapazitaet):
        # Ruft den Konstruktor der Klasse Auto auf
        super().__init__(marke, modell, anzahl_tueren)
        # Initialisiert die Batteriekapazität
        self.batterie_kapazitaet = batterie_kapazitaet

    def beschreibung(self):
        # Gibt eine spezifische Beschreibung des Elektroautos zurück
        return (f"Elektroauto: {self.marke} {self.modell} mit {self.anzahl_tueren} Türen "
                f"und einer Batteriekapazität von {self.batterie_kapazitaet} kWh")


# Definition der abgeleiteten Klasse HybridAuto
class HybridAuto(ElektroAuto, Auto):
    def __init__(self, marke, modell, anzahl_tueren, batterie_kapazitaet, kraftstoffverbrauch):
        # Ruft den Konstruktor der Klasse ElektroAuto auf
        super().__init__(marke, modell, anzahl_tueren, batterie_kapazitaet)
        # Initialisiert den Kraftstoffverbrauch
        self.kraftstoffverbrauch = kraftstoffverbrauch

    def beschreibung(self):
        # Gibt eine spezifische Beschreibung des Hybridautos zurück
        return (f"Hybridauto: {self.marke} {self.modell} mit {self.anzahl_tueren} Türen, "
                f"einer Batteriekapazität von {self.batterie_kapazitaet} kWh und "
                f"einem Kraftstoffverbrauch von {self.kraftstoffverbrauch} l/100km")


# Fehlerarten a-d
def beispiele_fehlerbehandlung(marken, favourite_marke):
    # Fehler a: Neuer Fehler, behebar
    fahrzeug_1 = Fahrzeug(None, "600 Select")
    if fahrzeug_1.marke is None:
        fahrzeug_1.marke = "Unbekannt"  # LBYL (Look Before You Leap)
    print(fahrzeug_1.beschreibung())

    # Fehler b: Hochgeblubberter Fehler, behebar
    def finde_fahrzeug(marke):
        if marke in marken:
            found_brand = marke
        else:
            marken.append(marke)

        finde_fahrzeug("Audi")

    # Fehler c: Neuer Fehler, NICHT behebar
    def lade_fahrzeug(marke, modell):
        if not marke:
            raise ValueError("Marke muss angegeben werden.")  # Nicht behebar
        return Fahrzeug(marke, modell)

    lade_fahrzeug(None, "600 Select")

    # Fehler d: Hochgeblubberter Fehler, NICHT behebar
    def add_favourite_brand_of_customer(favourite_marke):
        marken.append(favourite_marke)  # Nicht behebar

    add_favourite_brand_of_customer(favourite_marke)


if __name__ == "__main__":
    try:
        # Beispielinstanzen erstellen
        fahrzeug = Fahrzeug("PistenBully", "600 Select")
        auto = Auto("BMW", "3er", 4)
        motorrad = Motorrad("Kawasaki", "Ninja", 650)
        elektroauto = ElektroAuto("Tesla", "Model 3", 4, 75)
        hybridauto = HybridAuto("Toyota", "Prius", 4, 8.8, 4.4)

        # Fahrzeuge beschreiben
        print(fahrzeug.beschreibung())
        print(auto.beschreibung())
        print(motorrad.beschreibung())
        print(elektroauto.beschreibung())
        print(hybridauto.beschreibung())

        marken = [fahrzeug.marke for fahrzeug in [fahrzeug, auto, motorrad, elektroauto, hybridauto]]

        favourite_marke = input("Bitte lieblingsmarke eingeben: ")

        # Fehlerbeispiele
        beispiele_fehlerbehandlung(marken, favourite_marke)

    except Exception as error:
        print(f"Unerwarteter Fehler: {error}")
        sys.exit(1)