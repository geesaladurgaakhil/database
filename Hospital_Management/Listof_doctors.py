# Question 4: Get a list of doctors from a given hospital
import psycopg2
def get_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="python_db")
    return connection

def close_connection(connection):
    if connection:
        connection.close()
        print("PostgresSql connection closed")

# Fetch Hospital Name using Hospital id
def get_hospital_name(hospital_id):
    try:
        connection = get_connection()
        cursor=connection.cursor()
        select_query="""select * from hospital where Hospital_id=%s"""
        cursor.execute(select_query,(hospital_id,))
        record=cursor.fetchall()
        for i in record:
            return i[1]
    except (Exception,psycopg2.Error) as error:
        print("Error while getting data from PostgreSQL",error)

# Fetch Hospital Name using Hospital id
def get_doctors(hospital_id):
    try:
        hospital_name=get_hospital_name(hospital_id)
        connection=get_connection()
        cursor=connection.cursor()
        select_query="""select * from doctor where hospital_id=%s"""
        cursor.execute(select_query,(hospital_id,))
        records=cursor.fetchall()

        print("----------------------------------------------")
        print("printing Doctors of ",hospital_name," doctors")
        print("----------------------------------------------")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
            print("-------------------------")
        close_connection(connection)
    except (Exception,psycopg2.Error) as error:
        print("Error while getting data",error)

print("Question 4: Get a list of doctors from a given hospital")
get_doctors(2)





