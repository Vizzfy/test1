import mysql.connector
from insert_datat1 import insert_data
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hello1234",
    database="Gymt"
)
mycursor = mydb.cursor()

mycursor.execute('INSERT INTO Beispiel (schluessel, Vorname, Nachname) VALUES (1, "Kristian", "Anastasia")')


mydb.commit()
mycursor.close()
mydb.close()
