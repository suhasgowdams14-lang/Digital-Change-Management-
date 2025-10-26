import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect('change_management.db')
cursor = conn.cursor()

# --- Create Tables ---

# 1. Initiatives Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS initiatives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date TEXT
)
''')

# 2. Metrics Table (tracks adoption and readiness)
cursor.execute('''
CREATE TABLE IF NOT EXISTS metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    initiative_id INTEGER,
    metric_date TEXT NOT NULL,
    adoption_rate REAL,
    readiness_score REAL,
    FOREIGN KEY (initiative_id) REFERENCES initiatives (id)
)
''')

# 3. Feedback Table (tracks sentiment)
cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    initiative_id INTEGER,
    submission_date TEXT NOT NULL,
    sentiment_score REAL, -- e.g., -1.0 (negative) to 1.0 (positive)
    comment TEXT,
    FOREIGN KEY (initiative_id) REFERENCES initiatives (id)
)
''')

# --- Insert Sample Data ---

try:
    # Add a sample initiative
    cursor.execute("INSERT INTO initiatives (name, start_date) VALUES ('Project Phoenix', '2025-01-01')")
    initiative_id = cursor.lastrowid

    # Add sample metrics
    metrics_data = [
        (initiative_id, '2025-01-10', 0.15, 0.4),
        (initiative_id, '2025-01-17', 0.25, 0.5),
        (initiative_id, '2025-01-24', 0.40, 0.6)
    ]
    cursor.executemany("INSERT INTO metrics (initiative_id, metric_date, adoption_rate, readiness_score) VALUES (?, ?, ?, ?)", metrics_data)

    # Add sample feedback
    feedback_data = [
        (initiative_id, '2025-01-12', 0.8, 'Excited about the new tools!'),
        (initiative_id, '2025-01-15', -0.5, 'Training was confusing.'),
        (initiative_id, '2025-01-18', 0.1, 'I am neutral, need more info.'),
        (initiative_id, '2025-01-22', 0.6, 'Much better after the follow-up session.')
    ]
    cursor.executemany("INSERT INTO feedback (initiative_id, submission_date, sentiment_score, comment) VALUES (?, ?, ?, ?)", feedback_data)

    conn.commit()
    print("Database created and seeded successfully.")

except sqlite3.IntegrityError:
    print("Data already exists.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    conn.close()