    
# Sebuah aplikasi memiliki fitur registrasi dan login user. 
# Untuk menjaga keamanan data user, password tidak boleh disimpan dalam bentuk asli.
# SHA-256 digunakan untuk mengubah password menjadi hash sebelum disimpan.

# Program harus dapat:
# 1. Melakukan registrasi user 
# 2. Mengubah password menjadi hash SHA-256 
# 3. Menyimpan username dan hash password 
# 4. Menampilkan hasil Hash Password
# 5. Melakukan login 
# 6. Memverifikasi password login 
# 7. Menampilkan status login

        #   Tugas 3 Keamanan Sistem
        #   nama : Emil Rahmat
        #   Nim : 105841119124 
        #   Kelas: 4F 
        #   No absen: 11

import hashlib
database_user = {}
def registrasi():
    print("\n=== SISTEM REGISTRASI ===")
    username = input("Masukkan username baru: ")
    if username in database_user:
        print("Username sudah terdaftar! Silakan coba yang lain.")
        return
    password_asli = input("Masukkan password: ")
    password_sha256 = hashlib.sha256(password_asli.encode()).hexdigest()
    database_user[username] = password_sha256
    print("\n--- Registrasi Berhasil ---")
    print(f"Username disave  : {username}")
    print(f"Hash Password    : {password_sha256}")
def login():
    print("\n=== SISTEM LOGIN ===")
    username = input("Masukkan username: ")
    input_password = input("Masukkan password login: ")
    if username in database_user:
        input_hash = hashlib.sha256(input_password.encode()).hexdigest()
        if input_hash == database_user[username]:
            print("\n>>> Status: Login Berhasil! Selamat datang,", username)
        else:
            print("\n>>> Status: Login Gagal! Password salah.")
    else:
        print("\n>>> Status: Login Gagal! Username tidak ditemukan.")
def main():
    while True:
        print("\n" + "="*30)
        print("MENU UTAMA KEAMANAN SISTEM")
        print("1. Registrasi User")
        print("2. Login User")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        if pilihan == '1':
            registrasi() 
        elif pilihan == '2':
            login()      
        elif pilihan == '3':
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")
if __name__ == "__main__":
    main()