# Penentuan berdasarkan Rukyatul Hilal 🌙
Hilal adalah **bulan sabit muda** yang muncul setelah terjadinya **konjungsi** (ijtimak), yaitu saat matahari, bulan, dan bumi berada dalam satu garis lurus. Hilal ini menjadi penanda awal bulan baru dalam kalender Hijriyah, seperti awal Ramadhan atau Syawal.

## 🚀 Kenapa Program Ini Dibuat?

Program ini dibuat untuk:
1. **Memahami konsep hilal** secara astronomi.
2. **Menentukan awal puasa** atau Hari Raya Idul Fitri dengan metode hisab.
3. **Membantu pengamatan hilal** dengan perhitungan yang akurat.


## 🔍 Parameter Penting dalam Pengamatan Hilal

### 1. **Selisih Altitude (Ketinggian Bulan di Atas Matahari)**
- **Altitude** adalah tinggi suatu benda langit di atas horizon (cakrawala).
- **Selisih altitude > 0** artinya bulan lebih tinggi dari matahari saat matahari terbenam.
- Kenapa penting? Karena jika bulan di bawah matahari, cahaya matahari akan "menenggelamkan" cahaya bulan, sehingga hilal tidak terlihat.

### 2. **Umur Bulan**
- **Umur bulan** adalah waktu yang berlalu sejak konjungsi (ijtimak) sampai saat pengamatan.
- **Umur bulan > 8 jam** adalah standar umum untuk memastikan cahaya bulan cukup terang untuk dilihat.
- Kenapa penting? Karena jika umur bulan masih terlalu muda, cahaya bulan masih terlalu lemah untuk terlihat.




### 3. **Sudut Elongasi (Jarak sudut bulan dari matahari)**
- Formula dari code adalah penurunan dari `cosinus law spherical` 

- Kenapa penting? Karena elongasi dapat menentukan seberapa jauh Bulan dari Matahari. Jika elongasi terlalu kecil bulan akan terlalu dekat dengan Matahari.


## 📌 Penurunan Rumus Jarak Sudut antara Dua Objek di Langit  

Rumus untuk menghitung jarak sudut $\theta$ antara dua objek di langit berasal dari **hukum kosinus bola**.  

### 1️⃣ Representasi Vektor dalam Sistem Koordinat Bola  

Misalkan dua objek memiliki koordinat:  
- **Objek 1**: $(\text{alt}_1, \text{az}_1)$  
- **Objek 2**: $(\text{alt}_2, \text{az}_2)$  

Vektor posisi dalam koordinat kartesian diberikan oleh:

$$
x = \cos(\text{alt}) \cdot \cos(\text{az})
$$

$$
y = \cos(\text{alt}) \cdot \sin(\text{az})
$$

$$
z = \sin(\text{alt})
$$

Maka untuk kedua objek:

$$
(x_1, y_1, z_1) = (\cos(\text{alt}_1) \cos(\text{az}_1), \cos(\text{alt}_1) \sin(\text{az}_1), \sin(\text{alt}_1))
$$

$$
(x_2, y_2, z_2) = (\cos(\text{alt}_2) \cos(\text{az}_2), \cos(\text{alt}_2) \sin(\text{az}_2), \sin(\text{alt}_2))
$$

### 2️⃣ Menggunakan Hukum Kosinus  

Jarak sudut $\theta$ antara dua vektor dapat dihitung dengan **dot product**:

$$
\cos(\theta) = x_1 x_2 + y_1 y_2 + z_1 z_2
$$

Substitusi nilai $x$, $y$, dan $z$ dari kedua objek:

$$
\cos(\theta) = (\cos(\text{alt}_1) \cos(\text{az}_1)) (\cos(\text{alt}_2) \cos(\text{az}_2)) + (\cos(\text{alt}_1) \sin(\text{az}_1)) (\cos(\text{alt}_2) \sin(\text{az}_2)) + (\sin(\text{alt}_1) \sin(\text{alt}_2))
$$

Gunakan identitas trigonometri:

$$
\cos(A - B) = \cos A \cos B + \sin A \sin B
$$

Maka hasil akhirnya:

$$
\cos(\theta) = \sin(\text{alt}_1) \sin(\text{alt}_2) + \cos(\text{alt}_1) \cos(\text{alt}_2) \cos(\text{az}_1 - \text{az}_2)
$$
