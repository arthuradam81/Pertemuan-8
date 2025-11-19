data_mahasiswa = []

while True:
    print("\n=== Input Data Mahasiswa ===")
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    # Hitung nilai akhir
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    # Simpan ke list sebagai dictionary
    data_mahasiswa.append({
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": nilai_akhir
    })

    lanjut = input("Tambah data lagi (y/t)? ").lower()
    if lanjut == "t":
        break

# Tampilkan data
print("\n=== Daftar Nilai Mahasiswa ===")
for mhs in data_mahasiswa:
    print(f"{mhs['nama']} - Tugas: {mhs['tugas']}, UTS: {mhs['uts']}, UAS: {mhs['uas']}, Nilai Akhir: {mhs['akhir']:.2f}")