import sqlite3

conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()

# Create the table if it doesn't exist
ch = """
CREATE TABLE IF NOT EXISTS store (
    Name VARCHAR(35),
    Course VARCHAR(35),
    Batch VARCHAR(35),
    Enrollment_No VARCHAR(25) PRIMARY KEY
);
"""
cursor.execute(ch)

Name = ["kartike  ", "Bharat Singh Bhati", "Bhumika Kapoor", "Raj Singh Chauhan"]
Course = ["B.tech  ", "B.SC", "Btech BioTech", "B.COM"]
Batch = ["2022-2026 ", "2022-2026", "2022-2026", "2022-2026"]
Enrollment_No = ["A20405232069 ", "A20475222069", "A8024122025", "A20405622110"]

for x in range(len(Name)):
    a = """
    INSERT OR IGNORE INTO store (Name, Course, Batch, Enrollment_No)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(a, (Name[x].strip(), Course[x].strip(), Batch[x].strip(), Enrollment_No[x].strip()))

conn.commit()

# Fetch and print all records
cursor.execute("SELECT * FROM store")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
