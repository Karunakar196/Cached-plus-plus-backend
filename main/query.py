import psycopg2
class Query:
    def __init__(self,db_name,user,password,host,port):
        self.conn = psycopg2.connect(database=db_name, user=user, password=password, host=host, port=port)
        self.cursor = self.conn.cursor()
        print('Connected to DB!')
        
    def exec_query(self,query_string):
        pass
    
    def close(self):
        self.conn.commit()
        self.conn.close()
        print('Closed connection successfully!')