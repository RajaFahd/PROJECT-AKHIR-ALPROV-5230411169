import sqlite3
conn = sqlite3.connect('database_fauna.db')

cur = conn.cursor()

cur.execute("SELECT SUM(jml_skrng) FROM FAUNA ")
total_populasi = cur.fetchone()[0]

print(f"Jumlahkan total populasi hewan langka saat ini = {total_populasi}")

conn.close()