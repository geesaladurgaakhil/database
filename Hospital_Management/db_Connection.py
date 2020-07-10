# Question 1: Connect to your database server and print its version
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

def get_database_version():
    try:
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute("SELECT version();")
        db_version=cursor.fetchone()
        print("You are connected to PostgresSql version :",db_version)
        close_connection(connection)
    except (Exception,psycopg2.Error) as error:
        print("Error while getting data",error)

print("Question1 : Printing database version ")
get_database_version()


