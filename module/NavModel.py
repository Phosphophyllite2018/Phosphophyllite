import sqlite3
db = sqlite3.connect("./private/phosphophyllite.db")
cursor = db.cursor()
def getUsername() :
    sql = "SELECT username FROM blog WHERE id = 0;"
    result = cursor.execute(sql)
    return result.fetchone()[0]