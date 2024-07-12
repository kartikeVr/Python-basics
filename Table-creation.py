import sqlite3
conn = sqlite3.connect("sqlite.db")
ch = f"""CREATE TABLE IF NOT EXISTS store (
                        Name VARCHAR(35),
                        Course VARCHAR(35),
                        Batch VARCHAR(35),
                        Enrollment_No VARCHAR(25) PRIMARY KEY,
                        Count INTEGER DEFAULT 1,
                        Time VARCHAR(35)
);"""

conn.execute(ch)
conn.commit()
conn.close()
