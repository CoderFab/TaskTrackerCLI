# Funktion die das Hauptmenü aufruft
def Hauptmenue():
    print("1. Aufgaben hinzufügen")
    print("2. Aufgaben löschen")
    print("3. Aufgaben ändern")
    print("4. Alle abgeschlossenen Aufgaben anzeigen lassen")
    print("5. Alle nicht abgeschlossenen Aufgaben anzeigen lassen")
    print("6. Alle Aufgaben anzeigen lassen die momentan offen sind")
    print("7. Programm Ende")


# Aufgaben hinzufügen Untermenü
def hinzugefuegt():

    print("1. Aufgaben hinzufügen")
    print("2. Hauptmenü")
    wahl = input("Wähle eine Option => ")
    if wahl == "1":
        aufgabe = input("Schreibe deine Aufgabe aus => ")
        print("Deine Aufgabe lautet ", aufgabe)
    elif wahl == "2":
        print("Zurück zum Hauptmenü")
    else:
        print("Falsche Eingabe!")


# Untermenü Abgeschlossene Aufgaben anzeigen
def abgeschlossen():
    print("2. Hauptmenü")
    wahl = input("Wähle eine Option => ")
    if wahl == "1":
        aufgabe = input("Schreibe deine Aufgabe aus => ")
        print("Deine Aufgabe lautet ", aufgabe)
    elif wahl == "2":
        Hauptmenue()
    else:
        print("Falsche Eingabe!")


with open("art.txt", "r", encoding="utf-8") as file:
    print(file.read())
# Scheleife um eine Auswahl im Menü zu treffen
while True:
    Hauptmenue()
    wahl = input("Wähle eine Option => ")
    if wahl == "1":
        hinzugefuegt()
    elif wahl == "2":
        print("Aufgaben gelöscht")
    elif wahl == "3":
        print("Aufgaben ändern")
    elif wahl == "4":
        print("Abgeschlossene Aufgaben anzeigen")
    elif wahl == "5":
        print(" Nicht abgeschlossene Aufgaben")
    elif wahl == "6":
        print("Alle offenen Aufgaben anzeigen lassen")
    elif wahl == "7":
        print("Programm wird beendet")
        break
    else:
        print("Falsche Eingabe")
