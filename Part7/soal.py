import random
from os import system as cmd
from rich import print as cetak
from rich.panel import Panel as panel

###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
lol = random.choice([M2, H2, K2, B2, P2])
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
    |___/\___/ \__,_|_|\n""", width=60, title=f"BANNER", style=f"{color_panel}"))


class Program:
    def __init__(self):
        self.menu()

    def clearscr(self):
        cmd("cls")  # Change 'clear' to 'cls' for Windows

    def menu(self):
        blok()
        cetak(panel(f'[bold blue][[bold purple]01[/][bold blue]][/] [bold blue]Soal Part 7.5\n[bold blue][[bold purple]02[/][bold blue]][/] [bold blue]Soal Ujian 7', width=60, title=f"[bold blue]List Menu", style=f"bold blue"))
        cs = input('Pilih Menu Soal : ')
        if cs == '1' or cs == '01':
            self.tujul_lima()
        elif cs == '2' or cs == '02':
            self.tujuh()

    def tujul_lima(self):
        self.clearscr()
        blok()
        cetak(panel(f'[bold blue][[bold purple]01[/][bold blue]][/] [bold blue]Tugas 1\n[bold blue][[bold purple]02[/][bold blue]][/] [bold blue]Tugas 2\n[bold blue][[bold purple]03[/][bold blue]][/] [bold blue]Tugas 3', width=60, title=f"[bold blue]List Menu", style=f"bold blue"))
        cs = input('Pilih Menu Soal : ')
        if cs == '1' or cs == '01':
            print(SoalTujuh().shotOut())
        elif cs == '2' or cs == '02':
            nub1 = int(input("Masukkan angka pertama: "))
            nub2 = int(input("Masukkan angka kedua: "))
            print(SoalTujuh().calculate(nub1, nub2))
        elif cs == '3' or cs == '03':
            name = input("Masukkan nama: ")
            age = input("Masukkan umur: ")
            address = input("Masukkan alamat: ")
            hobby = input("Masukkan hobi: ")
            print(SoalTujuh().processSentence(name, age, address, hobby))

    def tujuh(self):
        self.clearscr()
        blok()
        cetak(panel(f'[bold blue][[bold purple]01[/][bold blue]][/] [bold blue]Tugas ujian 1\n[bold blue][[bold purple]02[/][bold blue]][/] [bold blue]Tugas ujian 2\n[bold blue][[bold purple]03[/][bold blue]][/] [bold blue]Tugas ujian 3\n[bold blue][[bold purple]04[/][bold blue]][/] [bold blue]Tugas ujian 4', width=60, title=f"[bold blue]List Menu", style=f"bold blue"))
        cs = input('Pilih Menu Soal : ')
        if cs == '1' or cs == '01':
            print(SoalTujuh().bandingkan_angka(5, 8))
            print(SoalTujuh().bandingkan_angka(5, 3))
            print(SoalTujuh().bandingkan_angka(4, 4))
            print(SoalTujuh().bandingkan_angka(3, 3))
            print(SoalTujuh().bandingkan_angka(17, 2))
        elif cs == '2' or cs == '02':
            print(SoalTujuh().balik_kata('Hello World and Coders'))
            print(SoalTujuh().balik_kata('John Doe'))
            print(SoalTujuh().balik_kata('I am a bookworm'))
            print(SoalTujuh().balik_kata('Coding is my hobby'))
            print(SoalTujuh().balik_kata('Super'))
        elif cs == '3' or cs == '03':
            print(SoalTujuh().konversi_menit(63))
            print(SoalTujuh().konversi_menit(124))
            print(SoalTujuh().konversi_menit(53))
            print(SoalTujuh().konversi_menit(88))
            print(SoalTujuh().konversi_menit(120))
        elif cs == '4' or cs == '4':
            print(SoalTujuh().xo('xoxoxo'))
            print(SoalTujuh().xo('oxooxo'))
            print(SoalTujuh().xo('oxo'))
            print(SoalTujuh().xo('xxxooo'))
            print(SoalTujuh().xo('xoxooxxo'))


class SoalTujuh:

    # soal no 1
    def shotOut(self):
        return "hello Function"

    # soal no 2
    def calculate(self, nub1, nub2):
        return nub1 * nub2

    # soal no 3
    def processSentence(self, name, age, address, hobby):
        sentence = f"Nama saya {name}, umur saya {age} tahun, alamat saya di {address}, dan hobi saya adalah {hobby}."
        return sentence

    # soal ujian 1
    def bandingkan_angka(self, angka1, angka2):
        if angka1 < angka2:
            return True
        elif angka1 > angka2:
            return False
        else:
            return -1

    # soal ujian 2
    def balik_kata(self, string):
        reversed_string = ""
        for char in reversed(string):
            reversed_string += char
        return reversed_string

    # soal ujian 3
    def konversi_menit(self, menit):
        jam = menit // 60
        detik = menit % 60
        return f"{jam:02}:{detik:02}"

    # soal ujian 4
    def xo(self, string):
        count_x = string.lower().count('x')
        count_o = string.lower().count('o')
        return count_x == count_o


# Run the program
Program()
