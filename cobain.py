import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.  
bonus = 0.05  
bonus_gaji = lambda gaji: bonus * gaji
df['Bonus'] = df['Gaji'].apply(bonus_gaji)
for index, z in df.iterrows():
    df.at[index, 'gaji_bonus'] = z['Gaji'] + bonus_gaji(z['Gaji'])
print()
# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
# bonus_gaji yaitu fungsi lambda untuk menghitung gaji * bonus
# menggunakan for untuk melakukan penjumlahan Gaji dengan fungsi lambda bonus_gaji
# yang akan menghasilkan kolom baru yaitu gaji_bonus dengan nilai gaji baru yang sudah ditambah dengan bonus
print(df) 

# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

usia_tua = lambda gaji: gaji * 0.02
for index, x in df.iterrows():
    bonus_plus = bonus_gaji(x['Gaji']) 
    if x['Usia'] > 30: 
        bonus_plus += usia_tua(x['gaji_bonus'])        
    df.at[index, 'bonus_baru'] = bonus_plus 
    df.at[index, 'gaji_bonus_baru'] = x['Gaji'] + bonus_plus
print()
# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
# fungsi lambda usia_tua menghitung bonus tambahan (2% dari gaji terbaru) jika usia karyawan diatas 30 tahun.
# perulangan sebanyak dataframe, bonus_plus yaitu bonus gaji dari sebelumnya.
# jika usia lebih dari 30 maka bonus_plus akan bertambah sesuai dengan fungsi usia_tua yaitu 2% dari gaji saat ini
# membuat 2 kolom baru bonus_baru isi data bonus baru dan gaji_bonus_baru isi data gaji + bonus baru
print(df)

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://gitlab.com/itenas/tugas_pemdas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.