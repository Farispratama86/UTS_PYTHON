def jadwal_hari(hari):  
    """Menampilkan jadwal kuliah berdasarkan hari."""  
    
    jadwal = [
        ["Senin", "Algoritma"],
        ["Selasa", "Basis Data"],
        ["Rabu", "Jaringan Komputer"],
        ["Kamis", "Pemrograman Python"],
        ["Jumat", "Sistem Operasi"]
    ]
    
    for item in jadwal:
        if item[0] == hari:
            # Kembalikan teks jadwal hari tersebut
            return f"Jadwal hari {hari}: {item[1]}"
    
    # Jika tidak ada hari yang cocok dalam list
    return "Hari tidak ditemukan"


# Contoh pemanggilan fungsi dengan argumen "Senin"
print(jadwal_hari("Senin"))

# Contoh pemanggilan fungsi dengan hari yang tidak ada di daftar
print(jadwal_hari("Minggu"))
