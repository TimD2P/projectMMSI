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
        for hours in range(0,24):
            cursor.execute(f"select * from vesselmap where extract(hour from ship_time) = {hours};")
            for ship_map in cursor.fetchall():
                print(ship_map[0])
                cursor.execute(f"select * from vesselinfo where mmsi_pk =  {ship_map[0]};")
                ship_info=cursor.fetchone()
                print(ship_info[10])

except Exception as _ex:
    print('error:',_ex)
finally:
    if connection:
        connection.close()
        print('Connection closed')