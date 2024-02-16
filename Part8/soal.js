/*
Buatlah sebuah fungsi dengan nama dataHandling dengan sebuah parameter untuk menerima argumen. Argumen yang akan diterima adalah sebuah array yang berisi beberapa array sejumlah n.
Tugas kamu adalah mengimplementasikan fungsi dataHandling agar dapat menampilkan data-data pada dari argumen seperti di bawah ini:
*/
function dataHandling(data) {
    for (let i = 0; i < data.length; i++) {
        console.log("Nomor ID:  " + data[i][0]);
        console.log("Nama Lengkap:  " + data[i][1]);
        console.log("TTL:  " + data[i][2] + " " + data[i][3]);
        console.log("Hobi:  " + data[i][4]);
        console.log(); // Memberikan baris kosong antara setiap entri
    }
}

let input1 = [
    ["0001", "Roman Alamsyah", "Bandar Lampung", "21/05/1989", "Membaca"],
    ["0002", "Dika Sembiring", "Medan", "10/10/1992", "Bermain Gitar"],
    ["0003", "Winona", "Ambon", "25/12/1965", "Memasak"],
    ["0004", "Bintang Senjaya", "Martapura", "6/4/1970", "Berkebun"]
];

dataHandling(input1);
/*
pada soal yg kedua, kalian harus belajar method split secara mandiri, pada soal dibawah ini, method .split() cukup powerfull loh
*/
let input = ["0001", "Roman Alamsyah ", "Bandar Lampung", "21/05/1989", "Membaca"];

function dataHandling2(input) {
  // Mengganti data pada index ke-1 dengan Roman Alamsyah Elsharawy
  input.splice(1, 1, "Roman Alamsyah Elsharawy");

  // Mengganti data pada index ke-2 dengan Provinsi Bandar Lampung
  input.splice(2, 1, "Provinsi Bandar Lampung");

  // Mengganti data pada index ke-3 dengan Pria
  input.splice(4, 0, "Pria");

  // Mengganti data pada index ke-5 dengan SMA Internasional Metro
  input.splice(5, 0, "SMA Internasional Metro");

  // Menampilkan array setelah modifikasi
  console.log(input);

  // Mengambil bulan dari tanggal pada index ke-3
  let tanggal = input[3].split("/");
  let bulan = '';
  switch (tanggal[1]) {
    case '01':
      bulan = 'Januari';
      break;
    case '02':
      bulan = 'Februari';
      break;
    case '03':
      bulan = 'Maret';
      break;
    case '04':
      bulan = 'April';
      break;
    case '05':
      bulan = 'Mei';
      break;
    case '06':
      bulan = 'Juni';
      break;
    case '07':
      bulan = 'Juli';
      break;
    case '08':
      bulan = 'Agustus';
      break;
    case '09':
      bulan = 'September';
      break;
    case '10':
      bulan = 'Oktober';
      break;
    case '11':
      bulan = 'November';
      break;
    case '12':
      bulan = 'Desember';
      break;
    default:
      bulan = 'Bulan tidak valid';
  }
  console.log(bulan);

  // Mengurutkan tanggal
  let tanggalSort = tanggal.slice().sort((a, b) => b - a);
  console.log(tanggalSort);

  // Format tanggal
  let tanggalFormat = tanggal.join("-");
  console.log(tanggalFormat);

  // Memotong nama jika lebih dari 15 karakter
  let nama = input[1];
  if (nama.length > 15) {
    nama = nama.slice(0, 15);
  }
  console.log(nama);
}

dataHandling2(input);


