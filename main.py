import sqlite3
conn = sqlite3.connect('db.sqlite3')
obj = conn.cursor()
obj.execute("""
            CREATE TABLE IF NOT EXISTS STUDENTS(
            id integer PRIMARY KEY AUTOINCREMENT,
            name CHAR(100) NOT NULL,
            email CHAR(100)NOT NULL UNIQUE,
            address CHAR(100) NOT NULL)
            """)
conn.commit()

def insert():
    obj.execute("""
            INSERT INTO students(name,email,address)
            VALUES('ram','ram@gmail.com','kathmandu')
            """)
    conn.commit()

def show():
    obj.execute("""SELECT * FROM STUDENTS""")
    # data = obj.fetchall()
    # data = obj.fetchmany(2)
    data=obj.fetchone()
    print(data)
show()
# insert()
# def delete():
#     obj.execute("""DELETE FROM students WHERE id = 1 """)
#     conn.commit()
# delete()