from insert_datat1 import insert_data

# Abfrage Ob eine Person hinzugefügt werden soll
Abfrage = input("Soll eine Person hinzugefügt werden sollen (JA/NEIN)")
# Benutzereingabe für Namen und Alter abfragen
if Abfrage.upper() == "JA":
    Vorname = input("Bitte gib deinen Vornamen ein: ")
    Nachname = input("Bitte gib deinen Nachnamen ein: ")
    insert_data(Vorname, Nachname)
elif Abfrage.upper() == "NEIN":
    print("Was willst du dann machen?")
else:
    StopIteration