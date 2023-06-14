import pymysql

class DatabaseMaria:

    def __init__(self, host, port, user, password, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
    
    def connect_db(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset
        )
        return conn
    
    def menuAdd(self, input_value):
        try:
            with self.connect_db() as conn:
                with conn.cursor() as cur:
                    sql = '''
                    INSERT INTO
                        menu (menu)
                    VALUES
                        (%s)
                    '''
                    cur.execute(sql, (input_value))
                    conn.commit()
        except Exception as e:
            print("예외 : ", str(e))
        return 1
    
    def getMenuList(self,):
        try:
            with self.connect_db() as conn:
                with conn.cursor() as cur:
                    sql = '''
                        SELECT 
                            *
                        FROM 
                            menu m ;
                    '''
                    cur.execute(sql)
                    result = cur.fetchall()
                    return result
        except Exception as e:
            print("예외 : ", str(e))

    def delMenu(self, num):
        try:
            with self.connect_db() as conn:
                with conn.cursor() as cur:
                    sql = '''
                        DELETE 
                        FROM 
                            menu 
                        WHERE 
                            num = %s
                    '''
                    cur.execute(sql, (num))
                    conn.commit()
                    return 1
        except Exception as e:
            print("예외 : ", str(e))