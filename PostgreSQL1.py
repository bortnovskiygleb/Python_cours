import psycopg2

# connecting to db
con = psycopg2.connect(
    host="localhost",
    database="firstdb",
    user="postgres",
    password="1234"
)

# create cursor
cur = con.cursor()

# execute query
cur.execute("select * from employees")
print(cur.fetchall())

cur.close()
con.close()
