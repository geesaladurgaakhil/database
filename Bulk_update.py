import psycopg2

def bulkUpdate(records):
    try:
        connecion=psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="akhil")
        cursor=connecion.cursor()

        sql_update_query="""UPDATE mobile SET price=%s where id=%s"""
        cursor.executemany(sql_update_query,records)
        connecion.commit()
        count=cursor.rowcount
        print(count,"records updated successfully")

    except(Exception, psycopg2.Error) as error:
        print("Error while Updating record",error)

    finally:
        if(connecion):
            cursor.close()
            connecion.close()
            print("PostgresSql connection closed")

tuple= [(211, 1),(333, 4)]
bulkUpdate(tuple)