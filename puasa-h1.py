import math

class ElongasiCalculator:
    def __init__(self):
        self.alt_matahari = None
        self.az_matahari = None
        self.alt_bulan = None
        self.az_bulan = None
    
    def hitung_elongasi(self, alt1, az1, alt2, az2):
        """
        Menghitung elongasi (jarak sudut) antara dua objek di langit.
        
        Parameters:
            alt1 (float): Altitude objek pertama (dalam derajat).
            az1 (float): Azimuth objek pertama (dalam derajat).
            alt2 (float): Altitude objek kedua (dalam derajat).
            az2 (float): Azimuth objek kedua (dalam derajat).
        
        Returns:
            float: Elongasi dalam derajat.
        """
        # Konversi derajat ke radian
        alt1_rad = math.radians(alt1)
        alt2_rad = math.radians(alt2)
        az_diff_rad = math.radians(abs(az1 - az2))  # Selisih azimuth
        
        # Hitung jarak sudut menggunakan rumus spherical law
        cos_theta = (math.sin(alt1_rad) * math.sin(alt2_rad)) + \
                    (math.cos(alt1_rad) * math.cos(alt2_rad) * math.cos(az_diff_rad))
        
        # Hitung theta dalam radian, lalu konversi ke derajat
        theta_rad = math.acos(cos_theta)
        theta_deg = math.degrees(theta_rad)
        
        return theta_deg
    
    def input_data(self):
        # Input data dari pengguna
        print("Masukkan data Matahari:")
        self.alt_matahari = float(input("Altitude Matahari (derajat): "))
        self.az_matahari = float(input("Azimuth Matahari (derajat): "))
        
        print("\nMasukkan data Bulan:")
        self.alt_bulan = float(input("Altitude Bulan (derajat): "))
        self.az_bulan = float(input("Azimuth Bulan (derajat): "))
    
    def run(self):
        # Jalankan program
        self.input_data()
        elongasi = self.hitung_elongasi(self.alt_matahari, self.az_matahari, self.alt_bulan, self.az_bulan)
        print(f"\nElongasi antara Bulan dan Matahari: {elongasi:.2f}°")
        if elongasi > 6:
            print('esok dah puase 🤗')
        else:
            print('masih lusa puasanya 😑')

# Jalankan program
if __name__ == "__main__":
    calculator = ElongasiCalculator()
    calculator.run()


# Data perhitungan ilmu falak, LF PBNU menunjukkan keadaan hilal sudah berada di atas ufuk, tepatnya + 2 derajat 04 menit 12 detik dan lama hilal 9 menit 49 detik,
#  dengan markaz Kantor PBNU, Jalan Kramat Raya 164, Jakarta, koordinat 6º 11’ 25” LS 106º 50’ 50” BT. 
# Sementara konjungsi atau ijtimak bulan terjadi pada Jumat Pahing 1 April 2021 pukul 13:25:54 WIB.  

# Sumber: https://www.nu.or.id/nasional/ini-alasan-kriteria-imkanur-rukyah-jadi-3-derajat-tinggi-hilal-dan-6-4-derajat-elongasi-CHNmU
