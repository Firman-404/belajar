def data_handling(input_data):
    input_data[1] = "Roman Alamsyah Elsharawy"
    input_data[2] = "Provinsi Bandar Lampung"
    input_data[4:5] = ["Pria", "SMA Internasional Metro"]

    tanggal = input_data[3].split('/')
    bulan = int(tanggal[1])

    bulan_dict = {
        1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei', 6: 'Juni',
        7: 'Juli', 8: 'Agustus', 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
    }
    bulan_str = bulan_dict[bulan]

    tanggal_formatted = '-'.join([tanggal[2], tanggal[0], tanggal[1]])
    nama = input_data[1][:15]

    print(input_data)
    print(bulan_str)
    print([tanggal[2], tanggal[0], tanggal[1]])
    print(tanggal_formatted)
    print(nama)

input_data = ["0001", "Roman Alamsyah ", "Bandar Lampung", "21/05/1989", "Membaca"]

data_handling(input_data)
def data_handling(array_referensi):
    hasil = ''
    for elemen in array_referensi:
        hasil += f"Nomor ID: {elemen[0]}\n"
        hasil += f"Nama Lengkap: {elemen[1]}\n"
        hasil += f"TTL: {elemen[2]} {elemen[3]}\n"
        hasil += f"Hobi: {elemen[4]}\n\n"
    return hasil

input_data = [
    ["0001", "Roman Alamsyah", "Bandar Lampung", "21/05/1989", "Membaca"],
    ["0002", "Dika Sembiring", "Medan", "10/10/1992", "Bermain Gitar"],
    ["0003", "Winona", "Ambon", "25/12/1965", "Memasak"],
    ["0004", "Bintang Senjaya", "Martapura", "6/4/1970", "Berkebun"]
]

print(data_handling(input_data))
