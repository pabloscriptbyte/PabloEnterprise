import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# PENYESUAIAN DIREKTORI UNTUK ANDROID
# ==========================================
# Mendeteksi apakah berjalan di Android (misal via Pydroid/Kivy/Buildozer)
if "ANDROID_ARGUMENT" in os.environ or "ANDROID_ROOT" in os.environ:
    # Arahkan penyimpanan ke folder Download di penyimpanan internal Android
    SAVE_DIR = "/storage/emulated/0/Download/"
else:
    # Jika di PC, simpan di folder yang sama dengan script
    SAVE_DIR = ""

order = []
nama_order = ""

# ==========================================
# FUNGSI UMUM
# ==========================================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def waktu():
    return datetime.now().strftime("%d-%m-%Y %H:%M")

# ==========================================
# HEADER
# ==========================================
def header():
    clear()
    print(r"""
     ██████╗  █████╗ ██████╗ ██╗      ██████╗
     ██╔══██╗██╔══██╗██╔══██╗██║     ██╔═══██╗
     ██████╔╝███████║██████╔╝██║     ██║   ██║
     ██╔═══╝ ██╔══██║██╔══██╗██║     ██║   ██║
     ██║     ██║  ██║██████╔╝███████╗╚██████╔╝
     ╚═╝     ╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝
""")
    print("                PABLO ENTERPRISE")
    print("             Digital Printing System")
    print("               Version 1.1 (Mobile)")
    print()

# ==========================================
# DASHBOARD
# ==========================================
def dashboard():
    while True:
        header()
        print("="*58)
        print(" 1. Harga Print")
        print(" 2. Harga Fotokopi")
        print(" 3. Cetak Amplop")
        print(" 4. Cek Harga Banner")
        print(" 5. Laminating")
        print(" 6. Cetak Stiker")
        print(" 7. Cetak Foto")
        print(" 8. Hitung Total Pesanan")
        print(" 9. Pengaturan Sistem")
        print("10. Keluar")
        print("="*58)
        print("\n> Tips : Cek kembali pesanan sebelum mencetak.\n")
        print("="*58)
        print(f"USER   : ADMIN")
        print(f"TOKO   : PABLO DIGITAL PRINT")
        print(f"STATUS : READY")
        print(f"WAKTU  : {waktu()}")
        print("="*58)

        menu = input("\nby PABLO > ")

        if menu == "1":
            harga_print()
        elif menu == "2":
            harga_fotokopi()
        elif menu == "3":
            harga_amplop()
        elif menu == "4":
            harga_banner()
        elif menu == "5":
            harga_laminating()
        elif menu == "6":
            harga_stiker()
        elif menu == "7":
            harga_foto()
        elif menu == "8":
            buat_order()
        elif menu == "9":
            print("\nPengaturan belum tersedia oleh ADMIN.")
            input("\nENTER...")
        elif menu == "10":
            break

# ==========================================
# MODUL PRINT, FOTOKOPI, AMPLOP, BANNER, LAMINATING, STIKER, FOTO
# ==========================================
# (Fungsi-fungsi ini sama persis dengan aslinya karena hanya memproses perhitungan matematis)

def harga_print():
    header()
    print("HARGA PRINT\n")
    print("1. Print Satu Sisi")
    print("2. Print Bolak Balik")
    pilih = input("Pilih : ")
    
    if pilih == "1":
        print("Mode     : SATU SISI")
    elif pilih == "2":
        print("Mode     : BOLAK BALIK")
    else:
        print("pilihan salah")
        input()
        return

    lembar = input("Jumlah Lembar : ")
    if not lembar.isdigit():
        print ("masukan angka saja")
        input()
        return

    lembar = int(lembar)

    if pilih == "1":
        if lembar < 10:
            harga = 800
        else:
            harga = 500
    elif pilih == "2":
        harga = 800

    total = harga * lembar

    print("\n----------------------------")
    print("Jenis        : PRINT")
    if pilih == "1":
        print("Mode         : SATU SISI")
    else:
        print("Mode         : BOLAK BALIK")
    print(f"Lembar       : {lembar}")
    print(f"Harga/Lembar : Rp {harga:,}")
    print(f"TOTAL        : Rp {total:,}")
    print("----------------------------")
    input("\nENTER...")

def harga_fotokopi():
    header()
    print("HARGA FOTOKOPI\n")
    lembar = int(input("Jumlah Lembar : "))
    if lembar > 10:
        harga = 400
    else:
        harga = 500
    total = harga * lembar
    print("\n----------------------------")
    print("Jenis        : FOTOKOPI")
    print(f"Lembar       : {lembar}")
    print(f"Harga/Lembar : Rp {harga:,}")
    print(f"TOTAL        : Rp {total:,}")
    print("----------------------------")
    input("\nENTER...")

def harga_amplop():
    header()
    print("CETAK AMPLOP\n")
    print("1. KECIL  110 x 70")
    print("2. SEDANG 152 x 96")
    print("3. BESAR  162 x 114")
    pilih = input("\nPilih Ukuran : ")
    dus = int(input("Jumlah Box : "))

    if pilih == "1":
        ukuran = "KECIL 110 x 70"
        harga = 20000
    elif pilih == "2":
        ukuran = "SEDANG 152 x 96"
        harga = 25000
    elif pilih == "3":
        ukuran = "BESAR 162 x 114"
        harga = 32000
    else:
        print("Pilihan tidak tersedia.")
        input("\nENTER...")
        return

    total = harga * dus
    print("\n----------------------------")
    print("Jenis        : CETAK AMPLOP")
    print("Ukuran       :", ukuran)
    print("Jumlah Box   :", dus)
    print("Harga/Box    : Rp {:,}".format(harga))
    print("TOTAL        : Rp {:,}".format(total))
    print("----------------------------")
    input("\nENTER...")

def harga_banner():
    header()
    print("CEK HARGA BANNER\n")
    print("1. Indoor")
    print("2. Outdoor")
    pilih = input("\nJenis : ")
    meter = float(input("Jumlah Meter : "))

    if pilih == "1":
        jenis = "INDOOR"
        harga = 23000
    elif pilih == "2":
        jenis = "OUTDOOR"
        harga = 25000
    else:
        print("Pilihan salah.")
        input("\nENTER...")
        return

    total = harga * meter
    print("\n----------------------------")
    print("Jenis        :", jenis)
    print("Meter        :", meter)
    print("Harga/Meter  : Rp {:,}".format(harga))
    print("TOTAL        : Rp {:,.0f}".format(total))
    print("----------------------------")
    input("\nENTER...")

def harga_laminating():
    header()
    print("LAMINATING\n")
    lembar = int(input("Jumlah Lembar : "))
    harga = 4000
    total = harga * lembar
    print("\n----------------------------")
    print("Lembar       :", lembar)
    print("Harga/Lembar : Rp {:,}".format(harga))
    print("TOTAL        : Rp {:,}".format(total))
    print("----------------------------")
    input("\nENTER...")

def harga_stiker():
    header()
    print("CETAK STIKER\n")
    print("1. Vinyl A3")
    print("2. Chromo A3")
    pilih = input("\nMedia : ")
    lembar = int(input("Jumlah Lembar : "))

    if pilih == "1":
        media = "VINYL"
        harga = 25000
    elif pilih == "2":
        media = "CHROMO"
        harga = 20000
    else:
        print("Pilihan salah.")
        input("\nENTER...")
        return

    cutting = input("Cutting? (Y/N) : ").upper()
    total = harga * lembar

    if cutting == "Y":
        total += 7000 

    print("\n----------------------------")
    print("Media        :", media)
    print("Lembar       :", lembar)
    print("Harga/Lembar : Rp {:,}".format(harga))
    print("TOTAL        : Rp {:,}".format(total))
    print("----------------------------")
    input("\nENTER...")

def harga_foto():
    header()
    print("CEK HARGA CETAK FOTO\n")
    print("1. 3x2")
    print("2. 4x6")
    print("3. Paket A 5pcs 3x2 ")
    print("4. Paket B 5pcs 4x6 ")
    print("5. 2R")
    print("6. 3R")
    print("7. 4R")
    print("8. 5R")
    print("9. 6R")

    pilih = input("\nPilih : ")
    data = {
        "1": ("3x2", 1000),
        "2": ("4x6", 1500),
        "3": ("Paket A 5pcs 3x2 ", 4000),
        "4": ("Paket B 5pcs 4x6 ", 7000),
        "5": ("2R", 3000),
        "6": ("3R", 4000),
        "7": ("4R", 5000),
        "8": ("5R", 6000),
        "9": ("6R", 7000)
    }

    if pilih not in data:
        print("Pilihan salah.")
        input("\nENTER...")
        return

    jumlah = int(input("Jumlah : "))
    nama, harga = data[pilih]
    total = harga * jumlah
    print("\n----------------------------")
    print("Jenis        :", nama)
    print("Jumlah       :", jumlah)
    print("Harga        : Rp {:,}".format(harga))
    print("TOTAL        : Rp {:,}".format(total))
    print("----------------------------")
    input("\nENTER...")

# ==========================================
# MEMBUAT ORDER BARU
# ==========================================
def buat_order():
    global nama_order
    global order
    order = []
    header()
    print("="*45)
    print("STATUS ORDER : RUN")
    print("DATE :", waktu())
    print("="*45)
    nama_order = input("\nInput Nama Klien : ")
    proses_order()

# ==========================================
# PROSES ORDER
# ==========================================
def proses_order():
    while True:
        header()
        print("="*45)
        print("STATUS ORDER : PROCESS")
        print("DATE :", waktu())
        print("="*45)
        print("Nama Order :", nama_order)
        print("""
1 Print
2 Fotokopi
3 Amplop
4 Banner
5 Laminating
6 Sticker
7 Foto
""")
        pilih = input("Pilih : ")

        if pilih == "1":
            jenis = input("Print (S=Single / B=Bolak Balik) : ").upper()
            lembar = input("Jumlah Lembar : ")
            if not lembar.isdigit():
                print("masukan angka saja")
                input()
                continue
            lembar = int(lembar)
            if lembar <= 0:
                 print("jumlah harus lebih dari 0 !")
                 input()
                 continue
            if jenis == "S":
                if lembar < 10:
                    harga = 800
                else:
                    harga = 500
            elif jenis == "B":
                harga = 800
            else:
                print("Pilihan anda salah.")
                input()
                continue
            subtotal = harga * lembar
            order.append({
                "nama":"PRINT",
                "qty":lembar,
                "subtotal":subtotal
            })

        elif pilih == "2":
            lembar = int(input("Jumlah Lembar : "))
            if lembar > 10:
                harga = 400
            else:
                harga = 500
            subtotal = harga * lembar
            order.append({
                "nama":"FOTOKOPI",
                "qty":lembar,
                "subtotal":subtotal
            })

        elif pilih == "3" :
            print("\n=== CETAK AMPLOP ===")
            print("1. KECIL 110x70")
            print("2. SEDANG 152x96")
            print("3. BESAR 162x114")
            ukuran = input("Pilih : ")
            if ukuran == "1":
                nama = "Amplop 110x70"
                harga = 20000
            elif ukuran == "2":
                nama = "Amplop 152x96"
                harga = 25000
            elif ukuran == "3":
                nama = "Amplop 162x114"
                harga = 32000
            else:
                print("pilihan anda salah.")
                input()
                continue
            box = int(input("Jumlah Box : "))
            subtotal = harga * box
            order.append({
                "nama": nama,
                "qty": box,
                "subtotal": subtotal
            })

        elif pilih == "4" :
            print("\n=== BANNER ===")
            print("1. Indoor")
            print("2. Outdoor")
            jenis = input("Pilih : ")
            if jenis == "1":
                nama = "Banner Indoor"
                harga = 23000
            elif jenis == "2":
                nama = "Banner Outdoor"
                harga = 25000
            else:
                print("pilihan anda salah.")
                input()
                continue
            meter = float(input("Jumlah Meter : "))
            subtotal = harga * meter
            order.append({
                "nama": nama,
                "qty": meter,
                "subtotal": subtotal
            })

        elif pilih == "5":
            lembar = int(input("Jumlah Lembar : "))
            subtotal = lembar * 4000
            order.append({
                "nama": "Laminating",
                "qty": lembar,
                "subtotal": subtotal })

        elif pilih == "6":
            print("1. Vinyl")
            print("2. Chromo")
            media = input("Pilih : ")
            if media == "1":
                nama = "Sticker Vinyl"
                subtotal_perlembar = 25000
            elif media == "2":
                nama = "Sticker Chromo"
                subtotal_perlembar = 20000
            else:
                print("pilihan anda salah.")
                input()
                continue
            lembar = int(input("Jumlah Lembar : "))
            subtotal = subtotal_perlembar * lembar
            cutting = input("Cutting (Y/N) : ").upper()
            if cutting == "Y":
                subtotal += lembar * 7000
                nama += " + Cutting"
            elif cutting == "N":
                pass
            else:
                print("pilihan anda salah.")
                input()
                continue
            order.append({
                "nama": nama,
                "qty": lembar,
                "subtotal": subtotal
            })

        elif pilih == "7":
            data = {
              "1": ("Foto 3x2",1000),
              "2": ("Foto 4x6",1500),
              "3": ("Paket A 5pcs (3x2)",4000),
              "4": ("Paket B 5pcs (4x6)",7000),
              "5": ("Foto 2R",3000),
              "6": ("Foto 3R",4000),
              "7": ("Foto 4R",5000),
              "8": ("Foto 5R",6000),
              "9": ("Foto 6R",7000)
            }
            print("""
        1.3x2
        2.4x6
        3.Paket A 5pcs 3x2
        4.Paket B 5pcs 4x6
        5.2R
        6.3R
        7.4R
        8.5R
        9.6R
        """)
            pilih_foto = input("pilih : ")
            if pilih_foto not in data:
                print("Pilihan salah.")
                input("\nENTER...")
                continue 
            jumlah = int(input("Jumlah : "))
            nama, harga = data[pilih_foto]
            subtotal = harga * jumlah
            order.append({
                 "nama": nama,
                 "qty": jumlah,
                 "subtotal": subtotal
            })
        
        print("\nSubtotal : Rp {:,}".format(subtotal))
        print("""
==========================
X = Tambah Pesanan
Y = Selesaikan
==========================
""")
        lanjut = input("> ").upper()
        if lanjut == "Y":
            invoice()
            return

# ==========================================
# INVOICE
# ==========================================
def invoice():
    header()
    print("="*45)
    print("STATUS ORDER : FINAL")
    print("DATE :", waktu())
    print("="*45)
    print("Nama :", nama_order)
    print()
    total = 0
    nomor = 1

    for item in order:
        print(f"{nomor}. {item['nama']}")
        print(f"   Qty      : {item['qty']}")
        print(f"   Subtotal : Rp {item['subtotal']:,}")
        print()
        total += item["subtotal"]
        nomor += 1

    print("="*45)
    print("TOTAL : Rp {:,}".format(total))
    print("="*45)

    export_resi()
    input("\nENTER...")

# ==========================================
# EXPORT RESI KE PNG
# ==========================================
def export_resi():
    total = sum(item["subtotal"] for item in order)
    lebar = 700
    tinggi = 1000 + (len(order) * 60)

    img = Image.new("RGB", (lebar, tinggi), "white")
    draw = ImageDraw.Draw(img)

    try:
        font_judul = ImageFont.truetype("arial.ttf", 28)
        font = ImageFont.truetype("arial.ttf", 20)
        font_bold = ImageFont.truetype("arialbd.ttf", 22)
    except:
        font_judul = ImageFont.load_default()
        font = ImageFont.load_default()
        font_bold = ImageFont.load_default()

    y = 30
    draw.text((180, y), "PABLO DIGITAL PRINT", fill="black", font=font_judul)
    y += 40
    draw.text((20, y), f"Tanggal : {waktu()}", fill="black", font=font)
    y += 30
    draw.text((20, y), f"Customer : {nama_order}", fill="black", font=font)
    y += 35
    draw.line((20, y, 680, y), fill="black")
    y += 20
    nomor = 1

    for item in order:
        draw.text((20, y), f"{nomor}. {item['nama']}", fill="black", font=font_bold)
        y += 28
        draw.text((40, y), f"Qty : {item['qty']}", fill="black", font=font)
        draw.text((450, y), f"Rp {item['subtotal']:,}", fill="black", font=font)
        y += 40
        nomor += 1

    draw.line((20, y, 680, y), fill="black")
    y += 25
    draw.text((20, y), "TOTAL", fill="black", font=font_bold)
    draw.text((450, y), f"Rp {total:,}", fill="black", font=font_bold)
    y += 60
    draw.text((120, y), "Terima kasih telah menggunakan", fill="black", font=font)
    y += 25
    draw.text((180, y), "PABLO DIGITAL PRINT", fill="black", font=font_bold)

    # Menambahkan variabel direktori Android agar gambar tersimpan di folder yang bisa diakses
    nama_file = f"{SAVE_DIR}Resi_{nama_order.replace(' ','_')}.png"

    try:
        img.save(nama_file)
        print(f"\nResi berhasil disimpan di:")
        print(nama_file)
    except Exception as e:
        print(f"\nGagal menyimpan resi: {e}")
        print("Pastikan aplikasi memiliki izin Storage.")
        
    input("\nENTER...")

# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    dashboard()
