a = [[100, 2, 34, 4,],
     [5, 641, '', 8],
     [9, 410, 101, 12],
     [21, 23, 56, 24]]

i = 0
while i < len(a):

    j = 0
    while j < len(a[i]):
        print(f"Nilai dikedudukan [{i}][{j}]: {a[i][j]}")

        j += 1
    i += 1

names = [['Hamzah', 'Nur Ramadhaniah', 'Siti Hawa', 'Siti Khadijah'],
        ['Hani Soffiah', 'Hani Dalilah', 'Ain Hanani'],
        ['Abdul Rahman', 'Muaz', 'Safiyah', 'Ramadhan']]

count = 0
for n in range(len(names)):
    for m in range(len(names[n])):
        print(names[n][m], n, m)
        count += 1

print(f"Total Names: {count}")
