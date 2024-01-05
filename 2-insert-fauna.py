import sqlite3
conn = sqlite3.connect('database_fauna.db')
cur = conn.cursor()
for i in range(10):
    input_nama_fauna = input("NAMA FAUNA : ")
    input_jenis = input("JENIS : ")
    input_asal = input("ASAL: ")
    input_jml_skrng = input("JUMLAH SAAT INI: ")
    input_thn_ditemukan = input("TAHUN TERAKHIR DITEMUKAN : ")
    insert_data = '''
                INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
                VALUES(?,?,?,?,?)
    '''

    try:
        cur.execute(insert_data, (input_nama_fauna, input_jenis, input_asal, input_jml_skrng, input_thn_ditemukan))
        conn.commit()
        print("data berhasil tambah")
    except Exception as e:
        print("input error")

conn.close()