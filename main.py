import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hello1234",
    database="Gymt"
)
mycursor = mydb.cursor()

mycursor.execute('INSERT INTO Beispiel (schluessel, Vorname, Nachname) VALUES (1, "Kristian", "Anastasia")')
def insert_data(Vorname, Nachname):
    sql = "INSERT INTO Beispiel2 (schluessel2, Vorname2, Nachname2) VALUES (2, %s, %s)"
    val = (Vorname, Nachname)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Datensatz eingefügt.")

# Benutzereingabe für Namen und Alter abfragen
Vorname = input("Bitte gib deinen Vornamen ein: ")
Nachname = input("Bitte gib deinen Nachnamen ein: ")

insert_data(Vorname, Nachname)

mydb.commit()
mycursor.close()
mydb.close()
