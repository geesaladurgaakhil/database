import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="akhil")
    cursor=connection.cursor()

    postgres_insert_query=""" INSERT INTO mobile (ID, MODEL, PRICE) values (%s,%s,%s)"""
    record_to_insert=(7, 'oppo', 20000)
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()
    count=cursor.rowcount
    print(count,"Records inserted successfully into mobile table")

except(Exception,psycopg2.Error) as error:
    if(connection):
        print("Failed to insert the record into mobile table",error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgresSql connection is closed")