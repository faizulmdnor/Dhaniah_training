"""
Penerangan 1:
    String: Data berbentuk teks, mesti berada dalam tanda petik.
"""
name = "Ramadhaniah"   # contoh string


"""
Penerangan 2:
    Int (integer): Nombor bulat tanpa titik perpuluhan.
"""
age = 25               # contoh integer


"""
Penerangan 3:
    Float: Nombor perpuluhan, ada titik (.)
"""
height = 160.5         # contoh float


"""
Penerangan 4:
    Print: Mencetak nilai pembolehubah ke skrin.
"""
print("Nama:", name)
print("Umur:", age)
print("Tinggi:", height)


"""
Penerangan 5:
    Operasi matematik:
    - int + int → int
    - float + float → float
    - int + float → float (Python automatik tukar kepada float)
"""
year_of_birth = 2026 - age
print("Tahun lahir (anggaran):", year_of_birth)


"""
Penerangan 6:
    Gabungan string + string:
    - Hanya boleh tambah string dengan string.
    - Tidak boleh tambah string dengan int/float tanpa tukar jenis data.
"""
full_sentence = "Nama saya " + name
print(full_sentence)


"""
Penerangan 7:
    Type casting:
    - Tukar int kepada string: str()
    - Tukar float kepada string: str()
"""
info = "Umur saya ialah " + str(age) + " tahun."
print(info)
