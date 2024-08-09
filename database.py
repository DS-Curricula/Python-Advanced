import sqlite3

# Step 1: Connect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Step 2: Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
)
''')
connection.commit()

# Step 3: Insert data
cursor.execute('''
INSERT INTO employees (name, position, department, salary)
VALUES (?, ?, ?, ?)
''', ('John Doe', 'Software Engineer', 'IT', 70000.00))
connection.commit()

# Step 4: Query data
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 5: Update data
cursor.execute('''
UPDATE employees
SET salary = ?
WHERE name = ?
''', (75000.00, 'John Doe'))
connection.commit()

# Step 6: Delete data
cursor.execute('''
DELETE FROM employees
WHERE name = ?
''', ('John Doe',))
connection.commit()

# Step 7: Close the connection
cursor.close()
connection.close()
