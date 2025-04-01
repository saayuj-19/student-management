import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres.zmadiqhihoxgcraydets"
DB_PASSWORD = "3IGEvnN2sHG13iZF"
DB_HOST = "aws-0-ap-southeast-1.pooler.supabase.com"
DB_PORT = "6543"
def db_connection():
    try:
        conn =  psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        print(conn)
        return conn
    except Exception as e:
        print("Error connecting to database")
        return None

def create_tables():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teacher(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")

if __name__ == "__main__":
    create_tables()
    