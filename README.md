# **Capstone-Modul-1**
Capstone Modul 1: Abednego Andries
Capstone Resto n Bar

# Deskripsi Umum
Aplikasi sederhana untuk menampilkan dan mengelola menu restoran. Program ini memungkinkan pengguna untuk melihat daftar menu, menambahkan item baru, mengedit, dan menghapus menu.

# Business Background
Manajemen sebuah restoran membutuhkan suatu sistem yang terstruktur untuk kebutuhan operasional dan administrasi restoran dan juga untuk mempermudah proses customer journey.

# Business Purpose
Sistem ini dirancang untuk membantu restoran dalam mengelola menu mereka secara efisien. Dengan adanya sistem ini, pemilik restoran dapat dengan mudah memperbarui menu, menyesuaikan harga, dan menghapus item yang tidak lagi tersedia. Selain itu, pelanggan dapat mengakses daftar menu dengan lebih cepat dan akurat, meningkatkan pengalaman mereka dalam memilih makanan.

# Ruang Lingkup Fitur
1. Menampilkan daftar menu restoran: `show_menu`
    - Menampilkan seluruh menu dalam restoran beserta dengan data `menu_resto`:
        - jenis menu: kategori bahan dasar yang disajikan dalam menu (nasi, mie, bihun, minuman)
        - nama menu: jenis menu yang memadukan bahan dasar yang telah diolah dan disajikan dengan topping dan resep spesial restoran (nasi goreng kambing, nasi goreng capstone)
        - stok: jumlah stok atau porsi makanan yang tersedia untuk masing-masing nama menu
        - harga: harga dalam satuan Rupiah untuk setiap porsi nama menu
        - kalori: jumlah kalori yang terkandung dalam 1 porsi nama menu
    - Menampilkan deskripsi menu untuk masing-masing nama menu dalam restoran berdasarkan indeks nama menu yang diinput user `menu_desc`
2. Menambahkan menu baru: `add_menu`
    - Menu khusus untuk admin restoran, sehingga membutuhkan password khusus admin
    - User input data-data yang dibutuhkan untuk menambahkan menu baru: 
        - jenis menu (dapat input jenis menu yang sudah ada atau jenis menu baru)
        - nama menu
        - stok
        - harga
        - kalori
        - deskripsi
3. Menghapus data dalam menu: `delete_menu`
    - Menu khusus untuk admin restoran, sehingga membutuhkan password khusus admin
    - User input indeks nama menu yang ingin dihapus dari daftar `menu_resto`
4. Mengubah data dalam menu yang sudah ada: `update_menu`
    - Menu khusus untuk admin restoran, sehingga membutuhkan password khusus admin
    - User input data-data menu yang sudah ada: 
        - nama menu
        - stok
        - harga
        - kalori
        - deskripsi
5. Memesan menu: `order_menu`
    - User dapat menambah pesanan dari daftar menu resto menggunakan menu `buy_menu` dengan input data:
        - indeks nama menu yang ingin dipesan
        - jumlah porsi nama menu yang ingin dipesan 
    - Setelah pesanan tersimpan, user dapat melihat kembali pesanan akhir dan melakukan pembayaran dengan menu `payment_menu`
    - Setelah melakukan pembayaran, user dapat input rating dari menu-menu yang telah dipesan
6. Memberikan saran dan masukkan: `feedback`
    - User dapat memberikan saran dan masukkan untuk setiap aspek dalam restoran:
        - Pelayanan
        - Keramahan Staff
        - Makanan
        - Masukkan lainnya

# Struktur Data dan Sistem
1. Data awal yang digunakanterdiri dari menu makanan dan minuman yang terdapat dalam restoran yang tersimpan dalam dictionary `produk` dikombinasikan dengan deskripsi dari setiap produk dalam dictionary `deskripsi_menu`
2. Selanjutnya data akan terupdate sesuai dengan tahapan berjalannya sistem dan sesuai dengan input dari user yang dimasukkan ke dalam sistem

# Implementasi
Implementasi sistem ini dilakukan dalam sebuah skrip Python yang mencakup semua fungsi yang diperlukan untuk mengelola menu restoran, mulai dari penambahan hingga pemesanan dan pembayaran.

# Metode Pengujian
Pengujian difokuskan pada verifikasi fungsionalitas fitur yang telah diimplementasikan, memastikan bahwa sistem memenuhi tujuan dan persyaratan yang telah ditetapkan.

# Kesimpulan
Proyek ini bertujuan untuk menyederhanakan proses manajemen menu restoran, meningkatkan efisiensi operasional, dan meningkatkan kepuasan pelanggan melalui sistem yang terstruktur dan otomatis. Dengan mengatasi kendala yang ada, solusi yang diusulkan akan membantu restoran dalam mengelola menu dengan lebih baik serta meningkatkan efektivitas operasional secara keseluruhan.

# Have Fun and Have a Nice Day!

Best Regards,
Abednego Andries


