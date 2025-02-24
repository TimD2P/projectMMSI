import psycopg2
host = "localhost"
port = 8000
dbname = "postgres"
user = "postgres"
password = "Son40788"
mmsi=303294060
hour=1
try:
    connection = psycopg2.connect(host=host, port=port, database=dbname, user=user, password=password)
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute("insert into vesselinfo VALUES(303294060, 'ship1', 40, 40, 30.1, 287, 50, 13.6, 'ussr', 'html');")
        print('Done')
    with connection.cursor() as cursor:
        cursor.execute("insert into vesselmap VALUES(303294060, 39.11292, -89.72122, timestamp '2025-09-10 00:00:00');")
        print('Done')
    with connection.cursor() as cursor:
        cursor.execute(f"select * from vesselinfo where mmsi_pk = {mmsi};")
        print(cursor.fetchall())

except Exception as _ex:
    print('error:',_ex)
finally:
    if connection:
        connection.close()
        print('Connection closed')