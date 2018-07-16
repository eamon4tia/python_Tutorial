import sqlite3

def main():
    db=sqlite3.connect("informintion.db")
    db.row_factory =sqlite3.Row
    db.execute("create table if not exists Admin(Name text , age int) ")
    db.execute("insert into Admin (Name,age) values (?  ,?)",("eamon",14))
    cu=db.execute("select * from Admin")
    db.commit()
    for row in cu:
        print("Name:{},age:{}".format(row["Name"],row["age"]))

if __name__ == '__main__':main()
