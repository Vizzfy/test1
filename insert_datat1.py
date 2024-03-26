import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hello1234",
    database="Gymt"
)
mycursor = mydb.cursor()

def insert_data(Vorname, Nachname):
    sql = "INSERT INTO Beispiel2 (Vorname2, Nachname2) VALUES (%s, %s)"
    val = (Vorname, Nachname)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Datensatz eingefügt.")

# Benutzereingabe für Namen und Alter abfragen
Vorname = input("Bitte gib deinen Vornamen ein: ")
Nachname = input("Bitte gib deinen Nachnamen ein: ")

insert_data(Vorname, Nachname)