# Fungsi perhitungan ongkir RapidSend
def hitung_ongkir(berat_kg, kota, asuransi=False):
    """Menghitung ongkos kirim berdasarkan kota, berat, dan opsi asuransi."""
    tarif_dasar = {"Jakarta": 10000, "Bandung": 12000, "Surabaya": 15000}
    ongkir = tarif_dasar[kota] + 2000 * berat_kg
    if asuransi:
        ongkir += 3000
    return ongkir


# Contoh pemanggilan fungsi
print(hitung_ongkir(3, "Jakarta"))
print(hitung_ongkir(5, "Surabaya", True))

#perhitungan

#tarif_dasar[kota] → biaya awal

#+ 2000 * berat_kg → tambahan per kilogram

#+ 3000 → jika asuransi=True