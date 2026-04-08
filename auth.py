from db import get_connection

def signup(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    # 🔍 Check if user already exists
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    if cursor.fetchone():
        conn.close()
        return "exists"

    # ✅ Insert new user
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )

    conn.commit()   # 🔥 VERY IMPORTANT
    conn.close()
    return "success"


def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    return user