import sqlite3
import backend
def connect():
    conn=sqlite3.connect("molds.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mold (id INTEGER PRIMARY KEY,orders integer,location text, \
    quantity integer,alloy text)")
    conn.commit()
    conn.close()

def insert(orders,location,quantity,alloy):
    conn=sqlite3.connect("molds.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO mold VALUES(NULL,?,?,?,?)",(orders,location,quantity,alloy))
    conn.commit()
    conn.close()
        
      
                  
def view():
    conn=sqlite3.connect("molds.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM mold")
    rows=cur.fetchall()
    
  
    conn.close()
    return rows

def search(orders="",location="",quantity="",alloy=""):
    conn=sqlite3.connect("molds.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM mold where orders=? OR location=? OR quantity=? OR alloy=?",\
    (orders,location,quantity,alloy))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("molds.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM mold WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
def update(id,orders,location,quantity,alloy):
    conn=sqlite3.connect("molds.db")
    cur=conn.cursor()
    cur.execute("UPDATE mold SET orders=?,location=?,quantity=?,alloy=? WHERE id=?",(orders,location,quantity,alloy,id))
    conn.commit()
    conn.close()
    
    
#comments below are uncommented for testing
#insert(174333,"big Line",33,"CD4MCU")
#print(view())
#print(search(alloy="CD4MCU"))

     
    
    
connect()
