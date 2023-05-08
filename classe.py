import sqlite3

conn = sqlite3.connect("./moko.db")

cur = conn.cursor()

class Student:

    def __init__(self):
        self.conn = sqlite3.connect("./moko.db")
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS student(
        id INTEGER  PRIMARY KEY,
        nom TEXT,
        age INTEGER,
        classe TEXT
        )''')

    def add_student(self, nom, age,classe):
        self.cur.execute("""INSERT INTO student(nom, age, classe) VALUES(?, ?, ?)""", (nom, age, classe))
        self.conn.commit()

    def get_all_student(self):
        self.cur.execute("""INSERT INTO student(nom,age,classe)VALUES(?,?,?)""",(nom,age,classe))
        self.conn.commit()
        

    def get_student(self):
        pass

    def update(self):
        self.cur.execute('''SELECT*FROM student''')
        students = self
        pass

    def delate(self):
        pass

