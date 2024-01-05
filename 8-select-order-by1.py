import sqlite3
conn = sqlite3.connect('database_fauna.db')

cur = conn.cursor()

cur.execute("SELECT *FROM FAUNA ORDER BY nama_fauna ASC ")

row_table = cur.fetchall()

print('DATA FAUNA')
print("="*140)
print("{:<10} {:<30} {:<20} {:<20} {:<20} {:<20}".format("ID FAUNA", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("="*140)

# menampilkan data dengan perulangan
for row in row_table:
    print("{:<10} {:<30} {:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    
conn.close()