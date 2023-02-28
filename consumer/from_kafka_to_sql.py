import psycopg2

connection = psycopg2.connect(
    host="172.31.0.2",
    port="5432",
    database="testdb",
    user="astro",
    password="1234"
)

table = connection.cursor()
table.execute("CREATE TABLE messages (id SERIAL PRIMARY KEY, message TEXT)")

message = "Second message in sql"
table.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
connection.commit()

table.close()
connection.close()
