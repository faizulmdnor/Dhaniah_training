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