# Capstone Project 
# Membuat Restaurant Management System untuk client "Capstone Resto & Bar"
from tabulate import tabulate

# Menu Capstone Resto & Bar
produk = {
    'Nasi': {
        'Nasi Goreng Kambing': [10, 10000, 200],
        'Nasi Goreng Mawut' : [15, 25000, 300],
        'Nasi Goreng Spesial Capstone': [10, 50000, 500]
    },
    'Mie': {
        'Mie Goreng Kambing': [10, 20000, 200], 
        'Mie Goreng Spesial Capstone': [10, 50000, 200]
    },
    'Bihun': {
        'Bihun Goreng Sapi': [10, 20000, 200], 
        'Bihun Goreng Spesial Capstone': [10, 60000, 200]
    }, 
    'Minuman': {
        'Es Teh': [20, 3000, 0], 
        'Teh Hangat': [30, 2000, 0],
        'Es Kelapa Muda':[20, 15000, 10]
    }
}

#Deskripsi menu
deskripsi_menu = {

    'Nasi Goreng Kambing': 'Nasi goreng dengan kecap dan bumbu spesial dilengkapi dengan paduan nikmatnya daging kambing muda yang lembut',
    'Nasi Goreng Mawut': 'Nasi goreng dipadukan dengan nikmatnya mie goreng kenyal dan dilengkapi dengan topping daging ayam pilihan',
    'Nasi Goreng Spesial Capstone': 'Nasi goreng spesial dengan tambahan topping premium seperti udang, ayam, dan telur',
    'Mie Goreng Kambing': 'Mie goreng dengan bumbu khas dan daging kambing yang empuk',
    'Mie Goreng Spesial Capstone': 'Mie goreng premium dengan tambahan seafood dan ayam panggang',
    'Bihun Goreng Sapi': 'Bihun goreng dengan daging sapi pilihan dan sayuran segar',
    'Bihun Goreng Spesial Capstone': 'Bihun goreng spesial dengan topping udang, sapi, dan ayam',
    'Es Teh': 'Teh dingin yang menyegarkan dengan daun teh pilihan',
    'Teh Hangat': 'Teh hangat dengan aroma khas yang menenangkan',
    'Es Kelapa Muda': 'Segarnya air kelapa muda dengan es batu agar tetap menjaga kesegarannya'
}

# 1. menampilkan menu (all access)
def show_menu():
    print('Silakan pilih tampilan menu yang diinginkan:\n1. Menampilkan semua menu\n2. Menampilkan deskripsi spesifik menu\n0. Kembali ke menu sebelumnya')
    while True:
        try:
            show_option = int(input('Masukkan index menu yang diinginkan: '))
            if show_option == 1:
                menu_resto()
                show_menu()
            elif show_option == 2:
                menu_desc()
                show_menu()
            elif show_option == 0:
                main_menu()
            else:
                print("Indeks tidak ditemukan.")
                show_menu()
        except ValueError:
            print("Harap masukkan angka yang valid.")

# 1.1 menampilkan semua menu (all access)
def menu_resto():
    index = 1  # Menambahkan index untuk tabel
    menu_index = {}  # Menyimpan mapping index ke nama menu
    print('Berikut adalah menu makanan dan minuman di Capstone Resto')
    for jenis_menu, nama_menu in produk.items():
        tabel_data = []
        for topping, detail in nama_menu.items():
            stok, harga, kalori = detail  # Unpack nilai dari list
            tabel_data.append([index, topping, stok, harga, kalori])
            menu_index[index] = topping  # Simpan mapping index ke nama menu
            index += 1  # Tambah index

        # Header tabel
        headers = ["Index", "Nama Menu", "Stok", "Harga", "Kalori"]
        
        # Cetak header kategori
        print(f"\n=== {jenis_menu} ===")
        
        # Cetak tabel menggunakan tabulate
        print(tabulate(tabel_data, headers=headers, tablefmt="grid"))
    
    return menu_index  # Kembalikan mapping index ke menu

# 1.2 menampilkan spesifik menu dan deskripsi menu (all access)
def menu_desc():
    menu_index = menu_resto()  # Dapatkan mapping index-menu
    while True:    
        try:
            pilihan = int(input("\nMasukkan nomor indeks menu untuk melihat deskripsi: "))
            if pilihan in menu_index:
                menu = menu_index[pilihan]
                print(f"\nDeskripsi {menu}: {deskripsi_menu.get(menu, 'Deskripsi tidak tersedia')}")
                print()
                break  # Keluar dari loop jika indeks ditemukan
            else:
                print("Indeks tidak ditemukan. Silakan coba lagi.")
                continue  # Kembali meminta input jika indeks tidak valid
        except ValueError:
            print("Harap masukkan angka yang valid.")

# 2. tambah menu (admin resto)
def tambah_menu():
    menu_resto()
    while True:
        try:
            jenis_menu = input("Masukkan jenis menu yang ingin ditambah: ").capitalize()
            nama_menu = input("Masukkan nama menu: ").title()
            
            # Cek apakah menu sudah ada
            if jenis_menu in produk and nama_menu in produk[jenis_menu]:
                print(f'Nama Menu {nama_menu} sudah ada. Silakan pilih menu berikut:\n1. Menambah menu lain\n0. Kembali ke Menu Utama')
                print()
                try:
                    option = int(input('Silakan masukkan menu yang diinginkan: '))
                    if option == 1:
                        continue
                    else:
                        main_menu()  # Keluar dari fungsi jika kembali ke menu utama
                except ValueError:
                    print("Harap masukkan angka yang valid.")
                    continue
            
            # Input data menu baru
            while True:
                try:
                    stok = int(input("Masukkan jumlah stok: "))
                except ValueError:
                    print("Harap masukkan angka yang valid.")
                    continue
                while True:
                    try:
                        harga = int(input("Masukkan harga: "))
                    except ValueError:
                        print("Harap masukkan angka yang valid.")
                        continue    
                    while True:
                        try:    
                            kalori = int(input("Masukkan jumlah kalori: "))
                        except ValueError:
                            print("Harap masukkan angka yang valid.")
                            continue     
            
                        deskripsi = input("Masukkan deskripsi menu: ").capitalize()
            
                        # Jika jenis menu belum ada, buat dictionary baru
                        if jenis_menu not in produk:
                            produk[jenis_menu] = {}
            
                        # Menyimpan data menu
                        produk[jenis_menu][nama_menu] = [stok, harga, kalori]
                        deskripsi_menu[nama_menu] = deskripsi

                        print(f"\nMenu '{nama_menu}' berhasil ditambahkan!")
                        menu_resto()

                        while True:
                            lanjut = input("Apakah ingin menambah menu lain? (ya/tidak): ").strip().lower()
                            if lanjut == "ya":
                                tambah_menu()  # Mengulang loop
                            elif lanjut == "tidak":
                                main_menu()
                            # Keluar dari fungsi setelah menambahkan menu
                            else:
                                print('harap masukkan input jawaban yang benar')
                            continue
        except ValueError:
            print("Harap masukkan angka yang valid.")
            continue

# 3. menghapus menu (admin resto)
def delete_menu():
    menu_index = menu_resto()
    while True:
        try:
            pilihan = int(input("Masukkan nomor indeks menu yang ingin dihapus: "))
            if pilihan in menu_index:
                menu = menu_index[pilihan]
                for jenis_produk, variant in produk.items():
                    if menu in variant:
                        del produk[jenis_produk][menu]
                        if menu in deskripsi_menu:
                            del deskripsi_menu[menu]
                        print(f"\nMenu '{menu}' berhasil dihapus!")
                        menu_resto()
                        while True:
                            lanjut = input("Apakah ingin menghapus menu lain? (ya/tidak): ").strip().lower()
                            if lanjut == "ya":
                                break  # Mengulang loop
                            elif lanjut == "tidak":
                                main_menu()
            else:
                print("Indeks tidak ditemukan.")
                continue
        except ValueError:
            print("Harap masukkan angka yang valid.")

# 4. update menu (admin resto)
def update_menu():
    menu_index = menu_resto()
    while True:
        try:
            pilihan = int(input("Masukkan nomor indeks menu yang ingin diubah: "))
            if pilihan in menu_index:
                menu = menu_index[pilihan]
                for jenis_produk, variant in produk.items():
                    if menu in variant:
                        print(f"Pilih data {menu} yang ingin diubah:")
                        print("1. Nama Menu")
                        print("2. Stok Menu")
                        print("3. Harga ")
                        print("4. Kalori Menu")
                        print("5. Deskripsi Menu")
                        pilihan_ubah = int(input("Masukkan pilihan: "))
                        
                        if pilihan_ubah == 1:
                            new_topping = input("Masukkan nama menu baru: ").title()
                            if new_topping in produk[jenis_produk]:
                                print("Nama menu sudah ada, silakan pilih nama lain.")
                                continue
                
                            # Simpan urutan lama dalam list
                            ordered_items = [(key, value) for key, value in produk[jenis_produk].items()]
                
                            # Ganti nama menu dalam list
                            for i, (key, value) in enumerate(ordered_items):
                                if key == menu:
                                    ordered_items[i] = (new_topping, value)
                
                            # Konversi kembali ke dictionary
                            produk[jenis_produk] = dict(ordered_items)
                            
                            # Perbarui deskripsi menu
                            deskripsi_menu[new_topping] = deskripsi_menu.pop(menu, "Deskripsi tidak tersedia")
                            menu_index[pilihan] = (jenis_produk, new_topping)
                        elif pilihan_ubah == 2:
                            produk[jenis_produk][menu][0] = int(input("Masukkan stok baru: "))
                            
                        elif pilihan_ubah == 3:
                            produk[jenis_produk][menu][1] = int(input("Masukkan harga baru: "))
                        elif pilihan_ubah == 4:
                            produk[jenis_produk][menu][2] = int(input("Masukkan jumlah kalori baru: "))
                        elif pilihan_ubah == 5:
                            deskripsi_menu[menu] = input("Masukkan deskripsi baru: ").capitalize()
                        else:
                            print("Pilihan tidak valid.")
                        
                        menu_resto()

                        print(f"\nMenu '{menu}' berhasil diperbarui!")

                        while True:
                            lanjut = input("Apakah ingin memperbaharui menu lain? (ya/tidak): ").strip().lower()
                            if lanjut == "ya":
                                update_menu()  # Mengulang loop
                            elif lanjut == "tidak":
                                main_menu()
            print("Indeks tidak ditemukan.")
            continue
        except ValueError:
            print("Harap masukkan angka yang valid.")
            

# 5. Pembelian menu (customer only)
def order_menu():
    print('Silakan pilih tampilan menu yang diinginkan:\n1. Menambahkan Pesanan\n2. Menampilkan Semua Pesanan dan Bayar \n0. Kembali ke menu sebelumnya')
    while True:
        try:
            show_option = int(input('Masukkan index menu yang diinginkan: '))
            if show_option == 1:
                beli_menu()
            elif show_option == 2:
                semua_pesanan()
            elif show_option == 0:
                main_menu()
            else:
                print("Indeks tidak ditemukan.")
                order_menu()
        except ValueError:
            print("Harap masukkan angka yang valid.")
            order_menu()

# 5.1 menambah pesanan
pesanan = []
def beli_menu():  # Menyimpan semua pesanan
    menu_index = menu_resto()
    global pesanan
    while True:
        try:
            pilihan = int(input("Masukkan nomor indeks menu yang ingin dibeli: "))
            if pilihan in menu_index:
                menu = menu_index[pilihan]
                
                # Mencari menu dalam kategori produk
                for jenis_produk, variant in produk.items():
                    if menu in variant:
                        stok, harga, kalori = variant[menu]

                        while True:
                            jumlah = int(input(f"Masukkan jumlah porsi untuk '{menu}': "))
                            
                            if jumlah > stok:
                                print("Maaf, stok tidak mencukupi. Silakan pesan sesuai jumlah stok.")
                                continue  # Kembali ke pemilihan menu

                            sub_total = jumlah * harga

                            # Mengurangi stok
                            produk[jenis_produk][menu][0] -= jumlah

                            # Simpan pesanan ke dalam list
                            pesanan.append([menu, jumlah, harga, sub_total])

                            headers = ["Nama Menu", "Porsi", "Harga", "Sub Total"]
                            print(tabulate(pesanan, headers=headers, tablefmt="grid"))

                            # Tanya pengguna apakah ingin menambah pesanan lagi
                            while True:
                                tambah_lagi = input("Apakah ingin menambah menu lain? (ya/tidak): ").lower()
                                if tambah_lagi == 'tidak':
                                # Menampilkan semua pesanan dalam bentuk tabel
                                    print("\n=== Semua Pesanan ===")
                                    headers = ["Nama Menu", "Porsi", "Harga", "Sub Total"]
                                    print(tabulate(pesanan, headers=headers, tablefmt="grid"))
                                    print()
                                    print("====Pesanan telah dikonfirmasi! Terima kasih telah membeli====")
                                    print()
                                    order_menu()
                                elif tambah_lagi == 'ya':
                                    print("\nSilakan pilih menu berikutnya.")
                                    beli_menu() # Menampilkan stok kembali
                                      # Kembali ke pemilihan menu di loop utama
                                else:
                                    print('Jawaban yang diinput tidak valid. Harap input jawaban yang sesuai')
                                    continue
            else:
                print("Indeks tidak ditemukan. Silakan pilih indeks yang sesuai.")
                continue
        except ValueError:
            print("Harap masukkan angka yang valid.")
            continue

# 5.2 menampilkan semua pesanan -> bayar -> rating makanan
def semua_pesanan():
    """ Menampilkan semua pesanan yang telah dibuat """
    if not pesanan:
        print("\nBelum ada pesanan yang dibuat. Silakan tambahkan pesanan dulu dengan pilih menu 1")
        print()
        order_menu()

    print("\n=== Semua Pesanan ===")
    
    total_harga = sum(item[3] for item in pesanan)

    headers = ["Nama Menu", "Porsi", "Harga", "Sub Total"]
    print(tabulate(pesanan, headers=headers, tablefmt="grid"))
    print(f"\nTotal yang harus dibayar: Rp {total_harga:,}")
    confirm = (input('Ada yang mau dipesan lagi atau ingin lanjut bayar? [pesan lagi/bayar]: ')).lower()
    while True:
        try:
            if confirm == 'pesan lagi':
                beli_menu()
            elif confirm == 'bayar':
                payment = int(input('Masukkan uang pembayaran: '))
                if payment >= total_harga:
                    kembalian = payment - total_harga
                    print(f'Uang kembali anda: Rp {kembalian:,}')
                    print('====Terima kasih sudah mengunjungi Capstone Resto n Bar!===')
                    print()
                else:
                    print("Uang tidak cukup. Masukkan jumlah uang yang cukup.")
                    continue
                
                print('Ayo berikan rating untuk menu yang telah dipesan')
                headers = ['Nama Menu', 'Porsi', 'Harga']
                print(tabulate(pesanan, headers=headers, tablefmt="grid"))
                print()
                for item in pesanan:
                    while True:
                        try:
                            rating = int(input(f'Masukkan rating untuk {item[0]} (1-5): '))
                            if 1 <= rating <= 5:
                                item.append(rating)
                                break
                            else:
                                print("Rating harus dalam rentang 1-5. Silakan coba lagi.")
                        except ValueError:
                            print("Input harus berupa angka. Silakan coba lagi.")
                headers.append("Rating")
                print("\nHasil Rating:")
                print(tabulate(pesanan, headers=headers, tablefmt="grid"))
                main_menu()
            else:
                print("Input yang dimasukkan salah. Silakan masukkan kembali.")
                semua_pesanan()
        except ValueError:
            print("Harap masukkan angka yang valid.")
            

#6. Saran dan Masukkan (customer only)
def saran():
    print('Halo Pelanggan Capstone Resto n Bar yang Terhormat, \nSaran dan masukan sangat berarti untuk Capstone Resto n Bar agar semakin lebih baik dalam melayani pelanggan.')
    
    kategori_dict = {
        1: "Pelayanan",
        2: "Keramahan Staff",
        3: "Kebersihan Resto",
        4: "Makanan",
        5: "Masukkan Lainnya"
    }

    kotak_saran = []  # List untuk menyimpan saran
    indeks = 1  # Nomor urut saran
    
    while True:
        # Menampilkan pilihan kategori
        print("\nSilakan pilih kategori yang ingin diberikan saran:")
        for key, value in kategori_dict.items():
            print(f"{key}. {value}")

        try:
            pilihan = int(input("Masukkan nomor kategori: "))
            if pilihan not in kategori_dict:
                print("Kategori tidak ditemukan. Silakan pilih kembali.")
                continue

            kategori = kategori_dict[pilihan]
            masukan_saran = input("Silakan masukkan saran Anda: ").strip()

            # Simpan ke dalam list
            kotak_saran.append([indeks, kategori, masukan_saran])
            indeks += 1  # Tambahkan nomor urut

            print("\n=== Kotak Saran ===")
            headers = ["Nomor", "Kategori", "Saran"]
            print(tabulate(kotak_saran, headers=headers, tablefmt="grid"))

            # Tanya apakah ingin menambahkan saran lagi
            while True:
                komen_lagi = input("Apakah ingin menambahkan saran lain? (ya/tidak): ").strip().lower()
                if komen_lagi == "tidak":
                    main_menu()  # Keluar dari loop jika tidak ingin menambah lagi
                elif komen_lagi == 'ya':
                    saran()
                else:
                    print('Silakan input jawaban yang sesuai')
                    continue  

        except ValueError:
            print("Harap masukkan angka yang valid.")

# Menu Utama
def main_menu():
    print()
    print('Selamat datang di Capstone Resto n Bar')
    print('Berikut adalah menu yang bisa dipilih:\n1. Menampilkan menu\n2. Menambahkan menu baru\n3. Menghapus menu\n4. Mengubah menu yang ada\n5. Pembelian menu\n6. Saran dan Masukkan\n7. Keluar dari menu')
   
    while True:
        try:
            pilih_menu = int(input("\nMasukkan nomor indeks menu yang diinginkan: "))
            if pilih_menu == 1:
                show_menu()
            elif pilih_menu == 2:
                tambah_menu()
            elif pilih_menu == 3:
                delete_menu()
            elif pilih_menu == 4:
                update_menu()
            elif pilih_menu == 5:
                order_menu()
            elif pilih_menu == 6:
                saran()
            elif pilih_menu == 7:
                print('Terima kasih telah mengunjungi Capstone Resto n Bar 😁😁🙏🏻')
                exit()
            else:
                print('Indeks tidak valid silakan masukkan angka indeks yang sesuai')
                main_menu()
        except ValueError:
            print("Harap masukkan angka yang valid.")
            main_menu()
    
main_menu()

