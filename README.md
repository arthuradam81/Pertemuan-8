# Pertemuan-8

# Flowchart
    
         ┌──────────────┐
         │   MULAI      │
         └──────┬───────┘
                │
                ▼
      ┌───────────────────┐
      │  Inisialisasi     │
      │  list data        │
      └────────┬──────────┘
               │
               ▼
     ┌────────────────────┐
     │   Input Nama       │
     │   Input Tugas      │
     │   Input UTS        │
     │   Input UAS        │
     └─────────┬──────────┘
               │
               ▼
     ┌────────────────────┐
     │ Hitung Nilai Akhir │
     └─────────┬──────────┘
               │
               ▼
     ┌────────────────────┐
     │ Simpan ke List     │
     └─────────┬──────────┘
               │
               ▼
     ┌────────────────────┐
     │ Tambah data? y/t   │
     └───────┬────────────┘
             │y
             ▼
        (Kembali ke input)
             │
             t
             ▼
   ┌────────────────────────┐
   │ Tampilkan Semua Data   │
   └─────────┬──────────────┘
             │
             ▼
        ┌─────────┐
        │ SELESAI │
        └─────────┘

# Penjelasan-Program

1. Inisialisasi List
Program membuat list kosong data_mahasiswa = []
List ini akan menyimpan semua data mahasiswa dalam bentuk dictionary.
2. Perulangan Input
Program memakai while True: agar user bisa memasukkan data sebanyak-banyaknya.
Setiap loop, program meminta:
Nama
Nilai tugas
Nilai UTS
Nilai UAS
3. Menghitung Nilai Akhir
Rumus:
Nilai Akhir = (Tugas × 30%) + (UTS × 35%) + (UAS × 35%)
4. Menyimpan Data
Data dimasukkan ke list sebagai dictionary:
{
  "nama": "...",
  "tugas": ...,
  "uts": ...,
  "uas": ...,
  "akhir": ...
}
5. Pertanyaan Tambah Data
Program menampilkan:
Tambah data lagi (y/t)?
Jika user menjawab t, program berhenti mengulang dan menampilkan seluruh data.
6. Menampilkan Semua Data
Setelah input selesai, program menampilkan data mahasiswa satu per satu.
