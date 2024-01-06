import cv2
import numpy as np
import pandas as pd
import argparse

# Membuat parser argumen (import argparse) untuk mengambil path gambar dari baris perintah di terminal
ap = argparse.ArgumentParser()
# run with "python.exe .\main.py --image .\images\flowers.jpg"
ap.add_argument("-i", "--image", required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args["image"]

# Membaca gambar dengan library opencv
img = cv2.imread(img_path)

# mendeklarasikan variabel secara global (digunakan nanti)
clicked = False
r = g = b = xpos = ypos = 0

# Membaca file csv dengan lib panda dan memberi nama pada setiap kolom
index = ["color", "color_name", "hex", "R", "G", "B"]
# berfungsi untuk menghitung jarak minimum dari semua warna dan mendapatkan warna yang paling cocok
csv = pd.read_csv("colors.csv", names=index, header=None)


# Mendefinisikan fungsi getColorName dengan tiga parameter R, G, dan B
def getColorName(R, G, B):
    # Inisialisasi variabel minimum dengan nilai yang sangat besar
    minimum = 10000
    # Melakukan iterasi pada setiap baris di file csv
    for i in range(len(csv)):
        # Menghitung jarak antara warna yang dicari dengan warna pada baris i di file csv menggunakan rumus Manhattan distance
        distance = (
            abs(R - int(csv.loc[i, "R"]))
            + abs(G - int(csv.loc[i, "G"]))
            + abs(B - int(csv.loc[i, "B"]))
        )
        # Jika jarak yang dihitung lebih kecil dari nilai minimum saat ini, maka update nilai minimum dan nama warna
        if distance <= minimum:
            minimum = distance
            cname = csv.loc[i, "color_name"]
    # Mengembalikan nama warna yang paling cocok
    return cname


# fungsi untuk mendapatkan koordinat x,y dari double klik mouse
def draw_function(event, x, y, flags, param):
    # Periksa apakah tombol kiri mouse diklik dua kali
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Deklarasikan variabel global untuk menyimpan nilai warna dan posisi piksel yang diklik
        global b, g, r, xpos, ypos, clicked
        # Setel flag clicked menjadi True
        clicked = True
        # Simpan koordinat x dan y dari piksel yang diklik
        xpos = x
        ypos = y
        # Dapatkan nilai warna dari piksel yang diklik
        b, g, r = img[y, x]
        # Konversi nilai warna menjadi bilangan bulat
        b = int(b)
        g = int(g)
        r = int(r)


# Membuat jendela dengan nama 'image'
cv2.namedWindow("image")
# Menetapkan fungsi 'draw_function' sebagai callback untuk peristiwa mouse pada jendela 'image'
cv2.setMouseCallback("image", draw_function)


# Ini adalah loop while yang akan terus berjalan selama kondisinya benar.
while True:
    cv2.imshow("image", img)
    # Ini adalah loop while yang akan terus berjalan selama kondisinya benar.
    if clicked:
        """
        Di bawah ini menggambar persegi panjang yang diisi pada gambar menggunakan library OpenCV. Persegi panjang didefinisikan oleh dua titik: (20, 20) dan (750, 60), yang mewakili sudut kiri atas dan sudut kanan bawah dari persegi panjang. Warna persegi panjang ditentukan oleh tupel (b, g, r), di mana b, g, dan r mewakili saluran warna biru, hijau, dan merah, masing-masing. Akhirnya, argumen -1 menentukan bahwa persegi panjang harus diisi sepenuhnya.
        """
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        """
        Ini mengambil nama warna berdasarkan nilai RGB dan menyimpannya dalam variabel text. Variabel ini juga berisi nilai R, G, dan B.
        """
        text = getColorName(r, g, b) + " R=" + str(r) + \
            " G=" + str(g) + " B=" + str(b)

        """
        Ini menambahkan teks ke gambar menggunakan library OpenCV. Teks yang ditambahkan adalah variabel text yang telah didefinisikan sebelumnya. Teks ini ditempatkan pada koordinat (50, 50) pada gambar. Ukuran font adalah 2 dan ketebalan font adalah 0,8. Warna teks adalah putih.
        """
        cv2.putText(img, text, (50, 50), 2, 0.8,
                    (255, 255, 255), 2, cv2.LINE_AA)

        """
        Ini menambahkan teks ke gambar jika nilai total R, G, dan B lebih besar atau sama dengan 600. Teks ini ditempatkan pada koordinat (50, 50) pada gambar. Ukuran font adalah 2 dan ketebalan font adalah 0,8. Warna teks adalah hitam. 
        """
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        """Ini mengatur variabel clicked menjadi False sehingga loop while dapat berjalan lagi."""
        clicked = False

    # Break the loop ketika pengguna menekan tombol 'esc'
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
