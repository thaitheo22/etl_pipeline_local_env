import psycopg2
from sqlalchemy import create_engine

# connect to postgresql 
def pg_connection():
    
    database = 'postgres'
    user = 'postgres'
    host = 'localhost'
    password = '123'
    port = 5432
        
    #psycopg2 method
    pg_connect = psycopg2.connect(
        database = database,
        user = user,
        host = host,
        password = password,
        port = port
    )
    
    # sqlachemy method 
    conn_str = fr'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
    engine_connect = create_engine(conn_str)
    
    return pg_connect, engine_connect 



'''
cursor = pg_connect.cursor()
cursor.execute('SQL query')
row = cursor.fetchall() -> use to fetch rows like SELECT (UPDATE, DELETE, ALTER, CREATE TABLE, INSERT)

connect.commit() -> if only use for fetch -> no need to use commit()
cursor.close()
connect.close()
'''



