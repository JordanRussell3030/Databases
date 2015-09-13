import sqlite3

def create_table(db_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

if __name__ == "__main__":
    db_name = "coffee_shop.db"
    sql = """create table Product
             (Product ID integer,
             Name text,
             Price real,
             primary key(Product ID))"""
    create_table(db_name, sql)
