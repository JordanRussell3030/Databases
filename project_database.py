import sqlite3

def create_table(db_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

if __name__ == "__main__":
    db_name = "trigonometry_tests.db"
    sql = """create table Product
             (Username integer,
             First Name text,
             Surname text,
             Date_of_test text,
             Test ID integer,
             Score integer,
             Percentage text,
             Q1 percentage text,
             Q2 percentage text,
             Colour face text,
             Number_of_Attempts integer,
             primary key(Username, Test ID))"""
    create_table(db_name, sql)

