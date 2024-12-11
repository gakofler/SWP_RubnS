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


if __name__ == "__main__":
    # Erstellung von Beispielinstanzen
    fahrzeug = Fahrzeug("PistenBully", "600 Select")
    auto = Auto("BMW", "3er", 4)
    motorrad = Motorrad("Kawasaki", "Ninja", 650)
    elektroauto = ElektroAuto("Tesla", "Model 3", 4, 75)
    hybridauto = HybridAuto("Toyota", "Prius", 4, 8.8, 4.4)

    # Beschreibung der Fahrzeuge ausgeben
    print(fahrzeug.beschreibung())
    print(auto.beschreibung())
    print(motorrad.beschreibung())
    print(elektroauto.beschreibung())
    print(hybridauto.beschreibung())