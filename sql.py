import sqlite3

# Connecting to SQLite
connection = sqlite3.connect("student.db")

# Creating a Cursor object for executing queries
cursor = connection.cursor()

# Creating a table only if it doesn't exist
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Inserting records into the table
records = [
    ('Krish', 'Data Science', 'A', 90),
    ('Sudhanshu', 'Data Science', 'B', 100),
    ('Darius', 'Data Science', 'A', 86),
    ('Vikash', 'DEVOPS', 'A', 50),
    ('Dipesh', 'DEVOPS', 'A', 35),
]

# Use `INSERT OR IGNORE`  to prevent duplicates
for record in records:
    cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)", record)

# Displaying all records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

# Committing changes to the database
connection.commit()
connection.close()
