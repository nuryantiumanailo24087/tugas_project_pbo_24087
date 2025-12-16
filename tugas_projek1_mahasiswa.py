# ==============================
# PROJEK PBO PYTHON
# Sistem Informasi Nilai Mahasiswa
# ==============================

# Class Mahasiswa
class Mahasiswa:
    def __init__(self, nama, npm, jurusan):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan


# Class Nilai
class Nilai:
    def __init__(self, mata_kuliah, nilai):
        self.mata_kuliah = mata_kuliah
        self.nilai = nilai


# Class Sistem Nilai (Program Utama)
class SistemNilai:
    def __init__(self):
        self.data = []

    def tambah_data(self):
        print("\n=== Tambah Data Mahasiswa ===")
        nama = input("Nama        : ")
        npm = input("NPM         : ")
        jurusan = input("Jurusan     : ")
        matkul = input("Mata Kuliah : ")
        nilai_angka = int(input("Nilai       : "))

        mahasiswa = Mahasiswa(nama, npm, jurusan)
        nilai = Nilai(matkul, nilai_angka)

        self.data.append((mahasiswa, nilai))
        print(">> Data berhasil ditambahkan")

    def tampilkan_data(self):
        print("\n=== Data Nilai Mahasiswa ===")
        if not self.data:
            print("Belum ada data mahasiswa.")
        else:
            for i, (mhs, nilai) in enumerate(self.data, start=1):
                print(f"\nMahasiswa ke-{i}")
                print("Nama        :", mhs.nama)
                print("NPM         :", mhs.npm)
                print("Jurusan     :", mhs.jurusan)
                print("Mata Kuliah :", nilai.mata_kuliah)
                print("Nilai       :", nilai.nilai)

    def jalankan(self):
        while True:
            print("\n=== MENU SISTEM INFORMASI NILAI MAHASISWA ===")
            print("1. Tambah Data Mahasiswa")
            print("2. Tampilkan Data Mahasiswa")
            print("0. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.tambah_data()
            elif pilihan == "2":
                self.tampilkan_data()
            elif pilihan == "0":
                print("Program selesai. Terima kasih.")
                break
            else:
                print("Pilihan tidak valid!")


# Menjalankan Program
app = SistemNilai()
app.jalankan()