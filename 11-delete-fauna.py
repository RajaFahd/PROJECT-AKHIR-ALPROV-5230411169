import sqlite3

conn = sqlite3.connect('database_fauna.db')
cur = conn.cursor()

asal_del ='Kalimantan'

delete_data = "DELETE FROM FAUNA WHERE asal = ?"

conn.execute(delete_data, (asal_del, ))
conn.commit()
conn.close()