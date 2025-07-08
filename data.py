import sqlite3
con = sqlite3.connect("test.db")

cur = con.cursor()

# cur.execute("CREATE TABLE movie(title, year, score)")
title = input("Enter title")
year = input("Enter year")
score = input("Enter score")

cur.execute(f"""
    INSERT INTO movie VALUES
        {title,year,score}
""")
data = cur.execute(f"""
    SELECT * from movie
""")
print(data)
con.commit()