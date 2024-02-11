import random
from os import system as cmd
from sys import exit as exit
from rich import print as cetak
from rich.panel import Panel as panel
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
lol = random.choice([M2,H2,K2,B2,P2])
###----------[ CEK WARNA TEMA ]---------- ###

color_text = "[#00FF00]"
color_panel = "#00C8FF"

def clearscr():
    cmd("cls")  # Change 'clear' to 'cls' for Windows

def blok():
    clearscr()
    cetak(panel("""                     _ 
                    | |
     ___  ___   __ _| |
    / __|/ _ \ / _` | | ( Di Buat oleh Firman404 )
    \__ \ (_) | (_| | | Tahun Pembuatan : 2024-02-9
    |___/\___/ \__,_|_|\n""",width=60,title=f"BANNER",style=f"{color_panel}"))

mancing = ""  # Assigning 'mancing' here
yokbisayok = ""
tanggal = 12
bulan = 9  # Mengubah bulan menjadi integer
tahun = 2009


def menu():
    blok()
    cetak(panel(f'[bold blue][[bold purple]01[/][bold blue]][/] [bold blue]Soal Part 5\n[bold blue][[bold purple]02[/][bold blue]][/] [bold blue]Soal Part 5.5',width=60,title=f"[bold blue]List Menu",style=f"bold blue"))
    cs = input('Pilih Menu Soal : ')
    if cs == '1' or cs == '01':
        gifalok()
    elif cs == '2' or cs == '02':
        btth()
def gifalok():
    clearscr()
    blok()
    cetak(panel(f'[bold blue][[bold purple]01[/][bold blue]][/] [bold blue]CS Game\n[bold blue][[bold purple]02[/][bold blue]][/] [bold blue]CS Tanggal',width=60,title=f"[bold blue]List Menu",style=f"bold blue"))
    soal = input('Pilih Menu : ')
    if soal == '1' or soal == '01':
        mancing() 
    elif soal == '2' or soal == '02':
        format_tanggal(12, 9, 2009)  

def btth():
    clearscr()
    blok()
    cetak(panel(f'[bold blue][[bold purple]01[/][bold blue]][/] [bold blue]Sentence\n[bold blue][[bold purple]02[/][bold blue]][/] [bold blue]Index Accessing - 1 by 1\n[bold blue][[bold purple]03[/][bold blue]][/] [bold blue]Breaking Sentence (Again) using Substring\n[bold blue][[bold purple]04[/][bold blue]][/] [bold blue]Breaking Sentence (yet Again) and Count Each Length',width=60,title=f"[bold blue]List Menu",style=f"bold blue"))
    siap = input('Pilih Menu : ')
    if siap == '1' or siap == '01':
        sentence() 
    elif siap == '2' or siap == '02':
        word2() 
    elif siap == '3' or siap == '03':
        word3() 
    elif siap == '4' or siap == '04':
        word4() 
    else:
        print("Pilihan menu tidak valid")

def mancing():
    global mancing  # Added to indicate modification of global variable
    if mancing == "":
        print("silakan isi nama dulu")
    else:
        mancing = "battle through the heavens"
        print(f"lanjutkan pemilihan peran mu {mancing}")

    yokbisayok = input("pilih peranmu (ksatria/tabib/penyihir): ")

    if yokbisayok == "ksatria":
        print(f"halo Ksatria {mancing} , kamu dapat menyerang dengan senjatamu!")
    elif yokbisayok == "tabib":
        print(f"halo Tabib {mancing} , kamu akan membantu temanmu yang terluka")
    elif yokbisayok == "penyihir":
        print(f"halo Penyihir {mancing} , ciptakan keajaiban yang membantu kemenanganmu!")
    else:
        print("peran tidak valid, silakan pilih peran yang lain")

def format_tanggal(tanggal, bulan, tahun):
    bulan_dict = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember"
    }

    if bulan in bulan_dict:
        bulan_str = bulan_dict[bulan]
        print(f"{tanggal} {bulan_str} {tahun}")
    else:
        print("Format bulan tidak valid")

format_tanggal(tanggal, bulan, tahun)

def sentence():
    word = "JavaScript"
    second = "is"
    third = "awesome"
    fourth = "and"
    fifth = "I"
    sixth = "love"
    seventh = "it!"

    # Menggabungkan string dengan menambahkan spasi di antara setiap kata
    sentence = word + " " + second + " " + third + " " + fourth + " " + fifth + " " + sixth + " " + seventh

    # Mencetak kalimat yang terbentuk
    print(sentence)

def word2():
    word2  = "wow JavaScript is so cool"

    # Mendapatkan setiap kata menggunakan akses satu per satu karakter dari string
    first_word = word2[0] + word2[1] + word2[2]
    second_word = word2[4:11]
    third_word = word2[15:17]
    fourth_word = word2[18:20]
    fifth_word = word2[21:25]

    # Menampilkan setiap kata yang terbentuk
    print("First Word:", first_word)
    print("Second Word:", second_word)
    print("Third Word:", third_word)
    print("Fourth Word:", fourth_word)
    print("Fifth Word:", fifth_word)

def word3():
    word3 = "wow JavaScript is so cool"
    first_word = word3[:3]
    second_word = word3[4:14]
    third_word = word3[15:17]
    fourth_word = word3[18:20]
    fifth_word = word3[21:25]

    print("First Word:", first_word)
    print("Second Word:", second_word)
    print("Third Word:", third_word)
    print("Fourth Word:", fourth_word)
    print("Fifth Word:", fifth_word)

def word4():
    word4 = "wow JavaScript is so cool"
    first_word = word4[:3]
    second_word = word4[4:14]
    third_word = word4[15:17]
    fourth_word = word4[18:20]
    fifth_word = word4[21:25]

    print("First Word:", first_word, ", with length:", len(first_word))
    print("Second Word:", second_word, ", with length:", len(second_word))
    print("Third Word:", third_word, ", with length:", len(third_word))
    print("Fourth Word:", fourth_word, ", with length:", len(fourth_word))
    print("Fifth Word:", fifth_word, ", with length:", len(fifth_word))
menu()
