import math
# Import module math yang digunakan untuk menghitung nilai akar kuadrat

def jump_search(arr, target):
    n = len(arr)
    # Menentukan panjang array
    jump_size = int(math.sqrt(n))
    # Menentukan ukuran lompatan dengan menggunakan nilai akar kuadrat dari panjang array
    prev = 0
    # Menetapkan variabel prev sebagai indeks awal dari lompatan
    while arr[min(jump_size, n)-1] < target:
        prev = jump_size
        jump_size += int(math.sqrt(n))
        # Menambah nilai jump_size dengan akar kuadrat dari panjang array
        if prev >= n:
            return -1
        # Jika prev lebih besar atau sama dengan panjang array, maka target tidak ditemukan
    while arr[prev] < target:
        # Melakukan pencarian linear di dalam jarak yang dilompati
        prev += 1
        if prev == min(jump_size, n):
            return -1
        
    if arr[prev] == target:
        return prev
    # Jika nilai elemen pada indeks prev sama dengan target, maka kembalikan indeks prev
    return -1
    # Jika target tidak ditemukan, maka kembalikan nilai -1

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# 1. Cari Arsel, Avivah, dan Daiva
print(f"1. {var[0]} di Index 0, {var[1]} di Index 1, {var[2]} di Index 2")
# Menampilkan pesan yang menunjukkan indeks dari tiga elemen pertama dalam daftar var

# 2. Cari Wahyu di Index 3 pada kolom 0
wahyu_index = jump_search(var[3], "Wahyu")
if wahyu_index != -1:
    print(f"2. Wahyu di Index 3 pada kolom 0")
else:
    print("2. Wahyu tidak ditemukan di Index 3 pada kolom 0")

# 3. Cari Wibi di Index 3 pada kolom 1
wibi_index = jump_search(var[3], "Wibi")
if wibi_index != -1:
    print(f"3. Wibi di Index 3 pada kolom 1")
else:
    print("3. Wibi tidak ditemukan di Index 3 pada kolom 1")
