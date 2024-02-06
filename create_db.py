import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Gangara4'
)

my_cursor = mydb.cursor()

# Check if the database exists
my_cursor.execute("SHOW DATABASES")
databases = my_cursor.fetchall()
database_exists = False
for db in databases:
    if 'waec_registration' in db:
        database_exists = True
        break

# If the database doesn't exist, create it
if not database_exists:
    my_cursor.execute("CREATE DATABASE waec_registration")
    print("Database 'waec_registration' created successfully.")
else:
    print("Database 'waec_registration' already exists.")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

my_cursor.close()
mydb.close()
