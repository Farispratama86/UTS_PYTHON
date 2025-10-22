# Program Koperasi - Setoran Mingguan

setoran1 = int(input("Masukkan setoran pertama: "))
setoran2 = int(input("Masukkan setoran kedua: "))
setoran3 = int(input("Masukkan setoran ketiga: "))

if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
    print("Input tidak valid")
else:
    total = setoran1 + setoran2 + setoran3

    if total <= 300000:
        print("Kategori: rendah")
    elif total < 600000:
        print("Kategori: sedang")
    else:
        print("Kategori: tinggi")

