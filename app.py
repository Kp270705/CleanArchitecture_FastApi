import psycopg2

try:
    conn = psycopg2.connect(
        dbname="bank",
        user="postgres",
        password="admin@123",
        host="localhost"
    )
    print("✅ Login success")
    conn.close()
except Exception as e:
    print("❌ Login failed:", e)
