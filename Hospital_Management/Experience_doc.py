# Question 5: Update doctor experience in years
import psycopg2
import datetime
from dateutil.relativedelta import relativedelta

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

# Update Doctor Experience in Years
def update_doctor_experience(doctor_id):
    try:
        # get joining date
        connection=get_connection()
        cursor=connection.cursor()
        select_query="""select joining_date from doctor where doctor_id=%s"""
        cursor.execute(select_query, (doctor_id,))
        joining_date=cursor.fetchone()

        # calculate experience in years
        joining_date_1=datetime.datetime.strptime(''.join(map(str, joining_date)), '%Y-%m-%d')
        today_date=datetime.datetime.now()
        experience = relativedelta(today_date, joining_date_1).years

        # Update doctor's Experience now
        connection=get_connection()
        cursor=connection.cursor()
        sql_select_query="""update doctor set Experience=%s where Doctor_id=%s"""
        cursor.execute(select_query,(experience,doctor_id))
        connection.commit()
        print("Doctor_id ",doctor_id," Experience Updated to",experience," years")
        close_connection(connection)
    except (Exception,psycopg2.Error) as error:
        print("Error while updating the experience",error)

print("Question 5: Update doctor experience in years")
update_doctor_experience(101)






