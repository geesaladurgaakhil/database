import psycopg2

def updateTable(mobileId, model, price):
    try:
        connection=psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="akhil")
        cursor=connection.cursor()

        print("Table Before Updating record:")
        sql_select_query="""select * from mobile where id = %s """
        cursor.execute(sql_select_query,(mobileId, ))
        record=cursor.fetchone()
        print(record)

        # now update a single record
        sql_update_query="""UPDATE mobile SET model= %s ,price= %s where Id= %s"""
        cursor.execute(sql_update_query,(model, price, mobileId))
        connection.commit()
        count=cursor.rowcount
        print(count,"Record updated successfully ")

        print("Table after updating record")
        sql_select_query="""select * from mobile where id=%s """
        cursor.execute(sql_select_query,(mobileId,))
        record=cursor.fetchone()
        print(record)


    except(Exception,psycopg2.Error) as error:
        print("Error in update operation ",error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgresSql connection closed")

mobileId = 7
model = 'viov V6'
price=33000
updateTable(mobileId,model,price)






