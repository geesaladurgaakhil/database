# Questions 3: Get the list Of doctors as per the given specialty and salary
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

def get_specialist_doctors_list(speciality, salary):
    try:
        connection=get_connection()
        cursor=connection.cursor()
        select_query="""select * from doctor where Speciality=%s and Salary > %s"""
        cursor.execute(select_query,(speciality,salary))
        records=cursor.fetchall()
        print("printing doctors whose specialty is", speciality, "and salary greater than",salary)
        print("------------------------")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
            print("----------------------")
        close_connection(connection)
    except (Exception,psycopg2.Error) as error:
        print("Error while getting data",error)

print("Questions 3: Get the list Of doctors as per the given specialty and salary")
print("--------------------------------------------")
get_specialist_doctors_list("Garnacologist",30000)
