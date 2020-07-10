# Question 2: Fetch Hospital and Doctor Information using hospital Id and doctor Id
import psycopg2
def get_connection():
    connection=psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="python_db")
    return connection

def close_connection(connection):
    if connection:
        connection.close()
        print("PostgresSql connection closed")

def get_hospital_details(hospital_Id):
    try:
        connection=get_connection()
        cursor=connection.cursor()
        select_query="""SELECT * FROM hospital where hospital_id=%s"""
        cursor.execute(select_query,(hospital_Id,))
        records=cursor.fetchall()
        print("printing hospital records")
        print("--------------------------")
        for row in records:
            print("Hospital Id:",row[0])
            print("Hospital Name:",row[1])
            print("Bed Count:",row[2])
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("error while getting the records ",error)

def get_doctor_details(doctor_id):
    try:
        connection=get_connection()
        cursor=connection.cursor()
        select_query="""select * from doctor where doctor_id=%s"""
        cursor.execute(select_query,(doctor_id,))
        records=cursor.fetchall()
        print("printing Doctor records")
        print("------------------------")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data",error)


print("Question 2: Fetch Hospital and Doctor Information using hospital Id and doctor Id")
print("-------------------------")
get_hospital_details(2)
print("-------------------------")
get_doctor_details(102)



