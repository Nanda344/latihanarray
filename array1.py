# Deklarasi array untuk meyimpan angka
angka =[]

# meminta input pengguna
for i in range(5):
    elemen = int(input(f"masukkan angka ke-{i+1}: "))
    angka.append(elemen)

#meghitung frekuensi kemunculan
frekuensi = {}
for elemen in angka:
    if elemen in frekuensi:
        frekuensi[elemen] += 1
    else:
        frekuensi[elemen] = 1

# menampilkan hasil
for elemen, jumlah in frekuensi.items():
    print(f"amgka {elemen} muncul sebanyak {jumlah} kali.")
