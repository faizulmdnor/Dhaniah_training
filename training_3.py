"""
RUMUSAN:
Program ini menunjukkan cara menggunakan senarai dua dimensi (kotak dalam kotak).
Ia juga menunjukkan cara menggunakan gelung (loop) untuk membaca setiap nilai.
Bahagian pertama guna 'while' untuk baca nombor.
Bahagian kedua guna 'for' untuk baca nama dan kira jumlah semua nama.
"""

"""
Baris ini buat satu senarai besar bernama 'a'.
Dalam 'a' ada beberapa senarai kecil (seperti kotak dalam kotak).
"""
a = [[100, 2, 34, 4,],
     [5, 641, '', 8],
     [9, 410, 101, 12],
     [21, 23, 56, 24]]

"""
Kita mula dengan nombor 0.
Ini untuk tunjuk baris pertama.
"""
i = 0

"""
Selagi i lebih kecil daripada jumlah baris,
program akan terus ulang.
"""
while i < len(a):

    """
    Mula dengan lajur pertama dalam setiap baris.
    """
    j = 0

    """
    Selagi j lebih kecil daripada jumlah nombor dalam baris itu,
    ulang lagi.
    """
    while j < len(a[i]):

        """
        Papar nilai dalam kotak berdasarkan baris (i) dan lajur (j).
        """
        print(f"Nilai dikedudukan [{i}][{j}]: {a[i][j]}")

        """
        Pergi ke nombor seterusnya dalam baris yang sama.
        """
        j += 1

    """
    Pergi ke baris seterusnya.
    """
    i += 1


"""
Ini satu lagi senarai, tapi mengandungi nama-nama.
Juga dalam bentuk kotak dalam kotak.
"""
names = [['Hamzah', 'Nur Ramadhaniah', 'Siti Hawa', 'Siti Khadijah'],
        ['Hani Soffiah', 'Hani Dalilah', 'Ain Hanani'],
        ['Abdul Rahman', 'Muaz', 'Safiyah', 'Ramadhan']]

"""
Pemboleh ubah untuk kira berapa banyak nama.
Mula dengan 0.
"""
count = 0

"""
Ulang setiap baris dalam senarai nama.
"""
for n in range(len(names)):

    """
    Ulang setiap nama dalam baris tersebut.
    """
    for m in range(len(names[n])):

        """
        Papar nama bersama nombor baris dan lajur.
        """
        print(names[n][m], n, m)

        """
        Tambah kiraan nama sebanyak 1.
        """
        count += 1

"""
Akhir sekali, paparkan jumlah semua nama.
"""
print(f"Total Names: {count}")

"""
ALTERNATIF 1: Guna for each (tanpa indeks)
Cara ini lebih senang sebab tak perlu guna i dan j.

RUMUSAN:
Cara ini lebih mudah kerana kita tidak perlu kira nombor baris dan lajur.
Kita terus ambil nilai dari dalam senarai.
"""

a = [[100, 2, 34, 4],
     [5, 641, '', 8],
     [9, 410, 101, 12],
     [21, 23, 56, 24]]

"""
Ulang setiap baris dalam 'a'.
"""
for row in a:

    """
    Ulang setiap nilai dalam baris tersebut.
    """
    for value in row:

        """
        Papar nilai sahaja.
        """
        print("Nilai:", value)

"""
ALTERNATIF 2: Guna enumerate (masih ada nombor posisi)
Kalau nak tahu kedudukan (index) dengan cara lebih kemas:

RUMUSAN:
Guna enumerate untuk dapat nombor baris dan lajur secara automatik.
Tak perlu tambah sendiri i atau j.
"""

a = [[100, 2, 34, 4],
     [5, 641, '', 8],
     [9, 410, 101, 12],
     [21, 23, 56, 24]]

"""
Dapatkan baris dan nombor baris sekali gus.
"""
for i, row in enumerate(a):

    """
    Dapatkan nilai dan nombor lajur sekali gus.
    """
    for j, value in enumerate(row):

        print(f"Nilai di [{i}][{j}] = {value}")
