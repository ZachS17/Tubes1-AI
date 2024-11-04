# Tubes1-AI

# Deskripsi
Diagonal magic cube adalah variasi dari magic cube (kubus ajaib) di mana jumlah angka di sepanjang diagonal dari setiap bidang atau dimensi kubus tersebut menghasilkan jumlah yang sama. Secara umum, magic cube adalah susunan angka dalam bentuk kubus 3D (biasanya berukuran nnn ketika jumlah angka pada setiap baris, kolom, dan tiang (baik secara horizontal, vertikal, maupun tiang) sama.
Dalam diagonal magic cube, aturan ini diperluas dengan menambahkan syarat bahwa jumlah angka di sepanjang diagonal bidang setiap lapisan dan diagonal ruang dari kubus juga harus sama. Ini membuat diagonal magic cube lebih kompleks daripada magic cube biasa karena tidak hanya memenuhi kondisi untuk baris, kolom, dan lapisan, tetapi juga untuk diagonal-diagonalnya pada setiap potongan sisi 2 dimensi serta diagonal ruang.
Pada tugas ini diminta untuk menyelesaikan persoalan diagonal magic cube berukuran   555 (orde 5) dengan mengimplementasikan algoritma local search. Algoritma-algoritma local search yang harus diimplementasikan, yaitu: algoritma hill-climbing, simulated annealing, dan genetic algorithm. Untuk algoritma-algoritma tersebut, ditentukan nilai state awal dan akhir dari kubus, nilai objective function akhir yang diperoleh, visualisasi nilai objective function terhadap banyaknya iterasi yang dilakukan, serta durasi proses pencarian yang telah dilakukan. Untuk setiap iterasi yang dilakukan, langkah yang dapat diambil adalah menukar posisi dari dua buah angka pada kubus tersebut, yang mana dua buah angka yang ditukar tidak harus berada bersebelahan.

# Solusi
Program ini menelusuri penyelesaian _diagonal magic cube_ dengan 4 pendekatan : _sideways_, _simulated annealing_, _stochastic_, dan _genetic algorithm_ didukung dengan visualisasi sederhana menggunakan matplotlib.

# Dependencies
- Python 3.12
- Matplotlib
- Numpy
- Time
- Random

# Compile
- Open home directory
- Run src.gui.visualizer

# Anggota
13522016 	Zachary Samuel Tobing
10321009	Sahabista Arkitanego Armantara
