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
    CREATE TABLE students(
    student_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(100),
     age INT,
    gender TEXT CHECK(gender IN ('Male','Female','Other')),
    email VARCHAR(255) UNIQUE
    )
    """)
    cursor.execute("""
    CREATE TABLE courses(
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    department_id INT,
    credits INT NOT NULL
    )
    """)
    cursor.execute("""
    create table enrollments(
    enrollment_id serial primary key,
    student_id int references students(student_id) on delete cascade,
    course_id int references courses(course_id) on delete cascade,
    grade varchar(2)
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")

def insert_teacher(name,age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teacher (name,age) VALUES(%s,%s) RETURNING id",(name,age))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Added")

def update_data(name,age,id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE teacher SET name = %s, age = %s WHERE id = %s ", (name,age,id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Updated")

def delete_tables(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teacher WHERE id = '%s'", (id,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    # id = int(input("Enter the id: "))
    # # name = input("Enter the name: ")
    # # age = int(input("Enter the age: "))
    # # update_data(name,age,id)
    # delete_tables(id)
    create_tables()