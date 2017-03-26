import sqlite3
#conn = sqlite3.connect('mydb.db')
#c = conn.cursor()
#c.execute("Select * from users")
#print c.fetchone()
#conn.commit()
#conn.close()

class db():
    def __init__(self):
        "creating db object"
        self.conn = sqlite3.connect('data.db') 
        self.c = self.conn.cursor()

    def query(self, sqlite_query, values=None):
        self.c.execute(sqlite_query, values)
        self.conn.commit()
        return self.c.fetchall()        
    def close(self):
        self.conn.close() #TODO MAKE SOMETHING TO CLOSE CONNECTION
#db().query("UPDATE stats set visits = visits +1y
#print db().query("SELECT visits FROM stats")[0][0]
