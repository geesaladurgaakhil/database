import psycopg2

def deleteData(mobileId):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="root",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="akhil")
        cursor = connection.cursor()
        # deleting a single record
        sql_delete_query = """Delete from mobile where id=%s """
        cursor.execute(sql_delete_query,(mobileId, ))
        connection.commit()
        count=cursor.rowcount
        print(count,"Record deleted successfully")
    except(Exception,psycopg2.Error) as error:
        print("Error in delete operation",error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgresSql connection closed")

id4=4
id5=5
deleteData(id4)
deleteData(id5)