def penjumlahan (angka1, angka2):
    jumlah = angka1 + angka2
    hasil = jumlah
    print(hasil)

def pengurangan (angka1,angka2):
    kurang = angka1 - angka2
    hasil = kurang
    print (hasil)

def perkalian (angka1, angka2):
    kali = angka1 * angka2
    hasil = kali
    print (hasil)

def pembagian (angka1, angka2):
    bagi = angka1/angka2
    hasil = bagi
    print(hasil)



def masukkan ():
    print(""" pilih perhitungan yang tersedia 
    1. penjumlahan
    2. pengurangan
    3. perkalian
    4. pembagian""")
    opsi = input("Silahkan pilih perhitungan => ")
    angka1 = int(input("Masukkan nilai ke 1 => "))
    angka2 = int(input("Masukkan Nilai ke 2 => "))

    if opsi == "1":
        penjumlahan(angka1,angka2)
    elif opsi == "2":
        pengurangan(angka1,angka2)
    elif opsi == "3":
        perkalian(angka1,angka2)
    elif opsi == "4":
        pembagian(angka1,angka2)
    else:
        print("bukan opsi yan tersedia !")


while True:
    try:
        masukkan()
    except ZeroDivisionError:
        print("Masukkan nilai lebih dari 0")
    except ValueError:
        print("Masukkan Angka, bukan huruf !")
    else:
        print("program telah berhenti")
        break
 