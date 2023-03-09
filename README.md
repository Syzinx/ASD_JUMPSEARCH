# POSTEST2 ALOGARITMA DAN STRUTUR DATA

Nama : chandra perdana phang

NIM : 2209116025

# PENJELASAN JUMP SEARCH

Jump search adalah salah satu algoritma pencarian pada struktur data yang terurut seperti array atau list. Algoritma ini bekerja dengan cara membagi data menjadi beberapa blok dengan ukuran yang sama, kemudian mencari blok yang memungkinkan data yang dicari terletak di dalamnya, dan kemudian melakukan pencarian linier pada blok tersebut.

Langkah-langkah dalam jump search adalah sebagai berikut:

1. Tentukan ukuran blok yang akan digunakan untuk membagi data. Ukuran blok haruslah kurang dari atau sama dengan akar dari panjang data.

2. Pilih blok pertama dan lakukan pencarian linier pada blok tersebut hingga ditemukan data yang dicari atau batas blok tersebut melebihi data yang dicari.

3. Jika data yang dicari belum ditemukan, pindah ke blok berikutnya dengan menambahkan ukuran blok pada indeks terakhir blok sebelumnya. Kemudian lakukan pencarian
   linier pada blok tersebut.

4. Ulangi langkah 3 hingga data yang dicari ditemukan atau batas blok melebihi data yang dicari.

Keuntungan dari jump search adalah efisiensinya yang relatif tinggi dalam mencari data pada array yang terurut, terutama jika data yang dicari berada di bagian depan array atau list. Namun, jump search membutuhkan data yang terurut dan tidak dapat digunakan pada struktur data yang tidak terurut. Selain itu, algoritma ini juga memerlukan beberapa variabel tambahan untuk menyimpan indeks dan batas blok.

# FUNGSI JUMP SEARCH

Jump search digunakan untuk mencari elemen tertentu pada array yang sudah terurut dengan lebih efisien daripada pencarian linier. Algoritma ini mengambil keuntungan dari fakta bahwa array terurut memungkinkan untuk memperkirakan lokasi elemen yang dicari dalam array dengan menggunakan indeks dan nilai elemen pada indeks tersebut.

Fungsi jump search secara umum adalah:

1. Mengambil ukuran blok yang digunakan untuk membagi array dan menentukan indeks awal dan akhir blok pertama.

2. Mencari blok yang memungkinkan elemen yang dicari terletak di dalamnya dengan memeriksa nilai elemen pada indeks awal dan akhir blok.

3. Jika nilai elemen pada indeks akhir blok kurang dari elemen yang dicari, maka pindah ke blok berikutnya dengan menambahkan ukuran blok pada indeks awal dan akhir blok sebelumnya.

4. Jika nilai elemen pada indeks akhir blok lebih besar atau sama dengan elemen yang dicari, maka lakukan pencarian linier pada blok tersebut dengan memeriksa setiap elemen pada blok secara berurutan.

5. Jika elemen yang dicari ditemukan, kembalikan indeks elemen tersebut.

6. Jika elemen yang dicari tidak ditemukan hingga batas blok terakhir, kembalikan nilai -1 sebagai tanda bahwa elemen tidak ditemukan pada array.

Fungsi jump search dapat membantu meningkatkan kinerja pencarian pada array yang terurut dengan mengurangi jumlah operasi pencarian linier yang diperlukan untuk menemukan elemen yang dicari.

# CONTOH PENERAPAN PADA PROGRAM YANG SAYA BUAT

![image](https://user-images.githubusercontent.com/126861865/223981730-e7edf78e-ee94-4e64-9834-71e332317684.png)


1.	import math : Mengimpor modul math yang berisi fungsi matematika seperti fungsi sqrt() yang digunakan untuk menghitung akar kuadrat.
2.	def jump_search(arr, target): : Mendefinisikan fungsi jump_search yang menerima dua parameter, yaitu sebuah array (arr) dan nilai target (target) yang ingin dicari dalam array tersebut.
3.	n = len(arr) : Menentukan panjang array arr.
4.	jump_size = int(math.sqrt(n)) : Menentukan ukuran lompatan dengan menghitung akar kuadrat dari panjang array arr dan mengonversinya menjadi integer. Ukuran lompatan ini digunakan dalam algoritma Jump Search untuk mengurangi jumlah perbandingan antara nilai target dengan nilai-nilai dalam array.
5.	prev = 0 : Menetapkan variabel prev sebagai indeks awal untuk melakukan lompatan dalam pencarian nilai target.


![image](https://user-images.githubusercontent.com/126861865/223982393-4217dc2f-5c87-4a89-922f-b4ba1b704489.png)


6.	while arr[min(jump_size, n)-1] < target: : Melakukan loop while untuk melakukan lompatan dalam pencarian nilai target. Loop akan terus berjalan selama nilai array pada indeks jump_size atau n-1 (tergantung mana yang lebih kecil) masih kurang dari nilai target. Jika nilai array pada indeks tersebut lebih besar atau sama dengan target, maka loop berhenti dan dilanjutkan ke langkah selanjutnya.
7.	prev = jump_size : Menetapkan nilai variabel prev dengan nilai jump_size.
8.	jump_size += int(math.sqrt(n)) : Menambahkan nilai jump_size dengan ukuran lompatan (yang merupakan akar kuadrat dari panjang array) untuk melanjutkan lompatan selanjutnya.
9.	if prev >= n: : Jika nilai prev lebih besar atau sama dengan panjang array n, maka nilai target tidak ditemukan dalam array dan fungsi akan mengembalikan nilai -1.


![image](https://user-images.githubusercontent.com/126861865/223983464-1b3b73db-b505-49f4-94b3-ad8a13388a2c.png)


10.	while arr[prev] < target: : Melakukan loop while untuk melakukan pencarian linear di dalam jarak yang dilompati. Loop akan terus berjalan selama nilai array pada indeks prev masih kurang dari nilai target. Jika nilai array pada indeks tersebut sama dengan nilai target, maka pencarian berhenti dan indeks prev akan dikembalikan sebagai output dari fungsi.
11.	prev += 1 : Menambahkan nilai prev dengan 1 untuk mencari nilai target pada indeks berikutnya dalam array.
12.	if prev == min(jump_size, n): : Jika nilai prev sama dengan nilai jump_size atau n-1 (tergantung mana yang lebih kecil), maka nilai target tidak ditemukan dalam array dan fungsi akan mengembalikan nilai -1.
13.	if arr[prev] == target: : Jika nilai array pada indeks prev sama dengan nilai target, maka indeks prev akan dikembalikan sebagai output dari fungsi.
14.	return -1 : Jika target tidak ditemukan, maka fungsi akan mengembalikan nilai -1.


![image](https://user-images.githubusercontent.com/126861865/223985545-c1528938-47d7-4371-86d1-bf63d61081cd.png)


15.	var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]] : Membuat sebuah list var yang berisi empat elemen
16.	Setelah itu, program akan mencetak pesan yang menunjukkan indeks dari tiga elemen pertama dalam daftar var menggunakan f-string dan akses indeks masing-masing elemen pada daftar var.


![image](https://user-images.githubusercontent.com/126861865/223985878-f10cbadb-4a23-4040-bb85-18d25b5275f9.png)


17.	Kemudian, program akan memanggil fungsi jump_search untuk mencari "Wahyu" di kolom 0 pada indeks 3 di dalam daftar var[3]. Hasil pencarian akan disimpan dalam variabel wahyu_index.
18.	Jika nilai wahyu_index tidak sama dengan -1 (yaitu, nilai yang mengindikasikan bahwa target tidak ditemukan), program akan mencetak pesan yang menunjukkan bahwa "Wahyu" ditemukan di indeks 3 pada kolom 0.
19.	Jika nilai wahyu_index sama dengan -1 (yaitu, nilai yang mengindikasikan bahwa target tidak ditemukan), program akan mencetak pesan yang menunjukkan bahwa "Wahyu" tidak ditemukan di indeks 3 pada kolom 0.


![image](https://user-images.githubusercontent.com/126861865/223986311-29cd9caf-57bf-4056-b2cf-4047d2cc9168.png)


20.	Program kemudian akan memanggil fungsi jump_search untuk mencari "Wibi" di kolom 1 pada indeks 3 di dalam daftar var[3]. Hasil pencarian akan disimpan dalam variabel wibi_index.
21.	Jika nilai wibi_index tidak sama dengan -1 (yaitu, nilai yang mengindikasikan bahwa target tidak ditemukan), program akan mencetak pesan yang menunjukkan bahwa "Wibi" ditemukan di indeks 3 pada kolom 1.
22.	Jika nilai wibi_index sama dengan -1 (yaitu, nilai yang mengindikasikan bahwa target tidak ditemukan), program akan mencetak pesan yang menunjukkan bahwa "Wibi" tidak ditemukan di indeks 3 pada kolom 1.
23.	Program kemudian berakhir.
