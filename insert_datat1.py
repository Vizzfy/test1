import mysql.connector


def insert_data(Vorname, Nachname):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="hello1234",
        database="Gymt"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO Beispiel2 (Vorname2, Nachname2) VALUES (%s, %s)"
    val = (Vorname, Nachname)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Datensatz eingefügt.")

    mycursor.close()
    mydb.close()


