"""
Penerangan 1:
    Print: Mencetak teks statik ke skrin tanpa perubahan.
"""
print('My name is Nur Ramadhaniah Binti Faizul')


"""
Penerangan 2:
    variable: "name"
    - Menyimpan teks nama penuh sebagai string.
    - Digunakan semula dalam operasi seterusnya.
"""
name = 'Nur Ramadhaniah Binti Faizul'


"""
Penerangan 3: list
    - Menukar string kepada senarai aksara.
    - Setiap huruf, termasuk ruang kosong, menjadi elemen dalam list.
"""
name_ls = list(name)


"""
Penerangan 4: for
    - Mengulangi setiap aksara dalam senarai name_ls.
    - Mencetak aksara satu per satu secara menegak.
"""
for char in name_ls:
    print(char)


"""
Penerangan 5: split + slicing
    - name.split(): Memecahkan nama kepada senarai perkataan.
    - Print forward: mencetak perkataan asal.
    - Print backward: mencetak perkataan terbalik menggunakan slicing [::-1].
"""
for word in name.split():
    print(f"Print forward: {word}")
    print(f"Print backward: {word[::-1]}")


"""
Penerangan 6: list comprehension
    - Menghasilkan senarai tuple (perkataan, perkataan_terbalik).
    - w: perkataan asal.
    - w[::-1]: perkataan terbalik.
"""
result = [(w, w[::-1]) for w in name.split()]
print(result)
