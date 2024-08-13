import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

# Create courses table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT,
        student_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(student_id)
    )
''')

# Insert data into students table
cursor.execute("INSERT INTO students (name) VALUES ('Alice')")
cursor.execute("INSERT INTO students (name) VALUES ('Bob')")

# Insert data into courses table
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES ('Math', 1)")
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES ('Science', 1)")
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES ('Art', 2)")

# Commit the transaction
conn.commit()

# Execute a JOIN query to combine data from students and courses
cursor.execute('''
    SELECT students.name, courses.course_name
    FROM students
    JOIN courses ON students.student_id = courses.student_id
''')

# Fetch and display the results
rows = cursor.fetchall()
for row in rows:
    print(f"Student: {row[0]}, Course: {row[1]}")

# Close the connection
conn.close()
