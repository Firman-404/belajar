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

def menu():
    blok()
    cetak(panel(f'[bold blue][[bold purple]01[/][bold blue]][/] [bold blue]Melakukan Looping Menggunakan While\n[bold blue][[bold purple]02[/][bold blue]][/] [bold blue]Melakukan Looping Menggunakan For\n[bold blue][[bold purple]03[/][bold blue]][/] [bold blue]Angka Ganjil dan Genap\n[bold blue][[bold purple]04[/][bold blue]][/] [bold blue]counter kelipatan\n[bold blue][[bold purple]05[/][bold blue]][/] [bold blue]Bintang asteriks',width=60,title=f"[bold blue]List Menu",style=f"bold blue"))
    cs = input('Pilih Menu Soal : ')
    if cs == '1' or cs == '01':
        whilee()
    elif cs == '2' or cs == '02':
        foree()
    elif cs == '3' or cs == '03':
        angk()
    elif cs == '4' or cs == '04':
        bg()
    elif cs == '5' or cs == '05':
        kp()

# soal no 1
def whilee():
    # Looping 1
    print("Looping 1")
    i = 1
    while i <= 7:
        print(i)
        i += 1

    # Looping 2
    print("Looping 2")
    j = 7
    while j >= 1:
        print(j)
        j -= 1

#soal no 2
def foree():
    # Looping 1
    print("Looping 1")
    for i in range(1, 8):
        print(i)

    # Looping 2
    print("Looping 2")
    for i in range(7, 0, -1):
        print(i)

#soal no 3
def angk():
    for i in range(101):
        if i % 2 == 0:
            print(f"{i} Genap")
        else:
            print(f"{i} Ganjil")

#soal no 4
def bg():
    # Counter 2
    print('Counter 2:')
    for i in range(1, 101, 2):
        if i % 3 == 0:
            print(f"{i} - Kelipatan 3")
    print()

    # Counter 5
    print('Counter 5:')
    for i in range(1, 101, 5):
        if i % 6 == 0:
            print(f"{i} - Kelipatan 6")
    print()

    # Counter 9
    print('Counter 9:')
    for i in range(1, 101, 9):
        if i % 10 == 0:
            print(f"{i} - Kelipatan 10")
    print('Done!')

#soal no 5
def kp():
    pattern = ""
    for i in range(1, 10):
        for j in range(1, i + 1):
            pattern += "*"
        pattern += "\n"

    print(pattern)
menu()
