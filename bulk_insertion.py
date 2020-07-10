import psycopg2

def bulkInsert(records):
    try:
        connection=psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="akhil")
        cursor=connection.cursor()

        # insert bulk records
        sql_insert_query="""INSERT INTO mobile(id, model, price) values (%s,%s,%s) """
        # executemany() to insert multiple rows rows
        result=cursor.executemany(sql_insert_query,records)
        connection.commit()
        print(cursor.rowcount,"Records inserted into mobile Table successfully")


    except(Exception,psycopg2.Error) as error:
        print("Failed Inserting bulk records into mobile table", error)


    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgresSql Connection is closed")


records_to_insert=[(4,'Blackberry',58000),(5,'Microsoft',66600),(8,'RealMe6',55004)]
bulkInsert(records_to_insert)
