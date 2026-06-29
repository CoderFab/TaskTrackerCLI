import json
import os

# Funktion die ein Löschen der JSON ermöglicht
# def löschen():


# Funktion den Bildschirm zu klären
def clear_screen():
    # Windows verwendet 'cls'
    # macOS und Linux verwenden 'clear'
    os.system("cls" if os.name == "nt" else "clear")


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
    while True:
        print("1. Aufgaben hinzufügen")
        print("2. Hauptmenü")
        wahl = input("Wähle eine Option => ")
        if wahl == "1":
            aufgabe = input("Schreibe deine Aufgabe => ")
            neue_daten = {"aufgabe": aufgabe}
            datei_name = "daten.json"
            naechste_id = 1
            # 1. Prüfen, ob die Datei existiert und die aktuelle ID ermitteln
            if os.path.exists(datei_name):
                with open(datei_name, "r", encoding="utf-8") as datei:
                    # Zähle nur Zeilen, die nicht leer sind
                    eintraege = [zeile for zeile in datei if zeile.strip()]
                    if eintraege:
                        naechste_id = len(eintraege) + 1

            # 2. Die ID an den Anfang des aktuellen Eintrags setzen
            eintrag_mit_id = {"id": naechste_id}
            eintrag_mit_id.update(neue_daten)

            # 3. Den Eintrag mit Absatz in die Datei schreiben
            with open(datei_name, "a", encoding="utf-8") as datei:
                datei.write(json.dumps(eintrag_mit_id, ensure_ascii=False) + "\n\n")
        elif wahl == "2":
            print("Zurück zum Hauptmenü")
            clear_screen()
        else:
            print("Falsche Eingabe!")
        break


# Untermenü Abgeschlossene Aufgaben anzeigen
def abgeschlossen():
    print("2. Hauptmenü")
    wahl = input("Wähle eine Option => ")
    if wahl == "1":
        aufgabe = input("Schreibe deine Aufgabe aus => ")
        print("Deine Aufgabe lautet ", aufgabe)
    elif wahl == "2":
        clear_screen()
        Hauptmenue()

    else:
        print("Falsche Eingabe!")


# Schleife um eine Auswahl im Menü zu treffen
while True:
    with open("art.txt", "r", encoding="utf-8") as file:
        print(file.read())
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
