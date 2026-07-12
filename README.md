# 🔐 Tugas 3 Keamanan Sistem — Password Hashing SHA-256

Simulasi sistem **registrasi & login** dengan penyimpanan password yang aman:
password tidak pernah disimpan dalam bentuk asli, melainkan di-hash dengan **SHA-256**.

## ✨ Fitur

- Registrasi user baru dengan pengecekan username unik
- Password di-hash SHA-256 sebelum disimpan ke database (dictionary in-memory)
- Login dengan verifikasi hash — hash input dibandingkan dengan hash tersimpan
- Menu CLI interaktif (registrasi / login / keluar)

## 🚀 Cara Menjalankan

```bash
python TugasKriptografi.py
```

Tanpa dependency eksternal — hanya modul `hashlib` bawaan Python.

## ⚠️ Catatan Keamanan

Program ini untuk tujuan pembelajaran. Pada sistem produksi, gunakan algoritma
hash khusus password seperti **bcrypt** atau **argon2** yang memakai *salt* dan
*work factor*, bukan SHA-256 polos.
