import psycopg2

def bulkDelete(records):
    try:
        connecion=psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="akhil")
        cursor=connecion.cursor()

        sql_delete_query="""Delete from mobile where id=%s"""
        cursor.executemany(sql_delete_query,records)
        connecion.commit()
        count=cursor.rowcount
        print(count,"records deleted successfully")

    except(Exception, psycopg2.Error) as error:
        print("Error while deleting record",error)

    finally:
        if(connecion):
            cursor.close()
            connecion.close()
            print("PostgresSql connection closed")

delete=[(1,),(4,)]
bulkDelete(delete)
