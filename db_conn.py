import psycopg2
import psycopg2.extras

#DB-Connection Params
DB_HOST = 'localhost'
DB_NAME = 'totemiq_db'
DB_USER = 'postgres'
DB_PASS = 'niarfe+456'
DB_PORT =  5433

try:
	conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST , port=DB_PORT)
	cur = conn.cursor()
	#conn properties
	print (conn.get_dsn_parameters(),"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    if(conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")    