# Import library pandas (walaupun tidak digunakan dalam contoh ini)
import pandas as pd


# Penerangan:
#   Function tambah_dua_number menerima dua nombor bulat (a dan b)
#   dan mengembalikan hasil tambah kedua-duanya.
def tambah_dua_number(a: int, b: int):
    c = a + b          # Operasi tambah
    return c           # Pulangkan nilai c kepada pemanggil function


# Penerangan:
#   Function darab_dua_number menerima dua nombor bulat
#   dan mengembalikan hasil darab kedua-duanya.
def darab_dua_number(a: int, b: int):
    c = a * b          # Operasi darab
    return c           # Pulangkan nilai c


# Penerangan:
#   Function tolak_dua_number menerima dua nombor bulat
#   dan mengembalikan hasil tolak (a - b).
def tolak_dua_number(a: int, b: int):
    c = a - b          # Operasi tolak
    return c           # Pulangkan nilai c


# Penerangan:
#   Function bahagi_dua_number menerima dua nombor bulat
#   dan mengembalikan hasil bahagi (a / b).
def bahagi_dua_number(a: int, b: int):
    c = a / b          # Operasi bahagi
    return c           # Pulangkan nilai c


# Penerangan:
#   Function pai tidak menerima parameter.
#   Ia hanya memulangkan nilai 2.17 (contoh nilai pi).
def pai():
    p = 2.17           # Tetapkan nilai pi
    return p           # Pulangkan nilai p


# Penerangan:
#   Minta pengguna masukkan nombor bulat pertama.
num1 = int(input('Masukkan nombor bulat: '))

# Penerangan:
#   Minta pengguna masukkan nombor bulat kedua.
num2 = int(input('Masukkan nombor bulat: '))


# Penerangan:
#   Panggil function tambah_dua_number dan simpan hasilnya.
tambah_result = tambah_dua_number(num1, num2)
print(tambah_result)   # Paparkan hasil tambah


# Penerangan:
#   Panggil function darab_dua_number dan simpan hasilnya.
darab_result = darab_dua_number(num1, num2)
print(darab_result)    # Paparkan hasil darab


# Penerangan:
#   Panggil function tolak_dua_number dan simpan hasilnya.
tolak_result = tolak_dua_number(num1, num2)
print(tolak_result)    # Paparkan hasil tolak


# Penerangan:
#   Panggil function bahagi_dua_number dan simpan hasilnya.
bahagi_result = bahagi_dua_number(num1, num2)
print(bahagi_result)   # Paparkan hasil bahagi


# Penerangan:
#   Panggil function pai dan simpan nilai pi.
pi = pai()
print(pi)              # Paparkan nilai pi
