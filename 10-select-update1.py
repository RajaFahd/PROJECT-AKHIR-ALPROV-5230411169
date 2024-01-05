import sqlite3
conn = sqlite3.connect('database_fauna.db')

cur = conn.cursor()

id_fauna = 10
jml_skrng_baru = 650

cur.execute(f"UPDATE FAUNA SET jml_skrng = {jml_skrng_baru} WHERE id_fauna = {id_fauna} ")
conn.commit()

if cur.rowcount > 0:
    print(f"Data dengan ID {id_fauna} berhasil diubah")

else:
    print(f"Tidak ada data Fauna dengan ID {id_fauna}!")
    
conn.close()