def bio():
    print('\nNama \t\t: ',nama[1])
    print('NIK \t\t: ',nik[1])
    print('Alamat \t\t: ',alamat[1])

def data():
    nama.insert(1,daftar['nama'])
    nik.insert(1,daftar['NIK'])
    alamat.insert(1,daftar['Alamat'])


print('\n---- Program pinjaman online -----\n')

nama = ['-']
nik = ['-']
alamat = ['-']
nominalpinjam = ['-']

PilihLain = 'Y'
while PilihLain.capitalize() == 'Y' :
    while True:
        print('\nPilihan awal : ')
        print('1. menu ')
        print('2. Menutup Program ')
        pilih = int(input('\nMasukkan pilihan : '))
        if pilih == 1 :
            print('\n Masukkan data  -- ')
            daftar = {
                'nama' : str(input('\nMasukkan Nama \t\t\t: ')) ,
                'NIK' : int(input('Masukkan  NIK \t\t\t: ')), 
                'Alamat' : str(input('Masukkan alamat anda \t\t: ')),}  

            rubah = str(input('\nApakah ingin merubah data teersebut (Y/N) ?: '))
            if rubah.capitalize() == 'Y':
                daftar['nama'] = str(input('Masukkan Nama \t\t\t: '))
                daftar['NIK'] = int(input('Masukkan  NIK \t\t\t: '))
                daftar['Alamat'] = str(input('Masukkan alamat anda \t\t: '))
                print('\ndalam proses .....')
                print('Data telah tersimpan -- \n')
                data()

            else :
                print('\ndalam proses .....')
                print('Data telah tersimpan --')
                data()
                
            
            menu = 'Y'
            while menu.capitalize() == 'Y':
                while True :
                    print ('\n\t\tSelamat datang di Alpa.pinjol ---- ')
                    print('\n\tAlur PINJOL : ')
                    print('\n\t1. Melakukan pinjaman')
                    print('\n\t2. Melakukan Pembayaran')
                    print('\n\t3. menghapus data')
                    print('\n\t4. kembali ke menu awal')

                                
                    pilih = int(input('\n\tMasukkan urutan : '))
                    if pilih == 1 :
                        bio()
                        Pinjam ={'pinjam' : int(input('Masukkan nominal Peminjaman : Rp '))}
                        if Pinjam['pinjam'] == 0 :
                            print('Uang harus lebih dari 0 ..')
                            break
                        if Pinjam['pinjam'] > 0 :
                            nominalpinjam.insert(1,Pinjam['pinjam'])
                            bunga = nominalpinjam[1]*10/100
                            hasil = Pinjam['pinjam'] + bunga
                            print('Bunga = 10%')
                            print('\nNominal tagihan = Rp ',hasil)

                            rbh = str(input('rubah (Y/N) ? : '))
                            if rbh.capitalize() == 'Y':
                                Pinjam['pinjam'] = int(input('Masukkan nminal pnjam : '))
                                nominalpinjam.insert(1,Pinjam['pinjam'])
                                bunga = nominalpinjam[1]*10/100
                                hasil = Pinjam['pinjam'] + bunga
                                print('Bunga = 10%')
                                print('\nNominal tagihan = Rp ',hasil)


                            tanya = str(input('\nApakah ingin cancel (Y/N) ? : '))
                            if tanya.capitalize() == 'Y':
                                exit('\nPinjaman dibatalkan ------ ')

                            elif tanya.capitalize() == 'N':
                                print('\nPinjaman telah disetujui --- \n')
                                bio()
                                print('Pinjaman = Rp ',nominalpinjam[1])
                                print('Tagihan = Rp ',hasil)
                                print('\nNB : Pembayaran maksimal selama 120 hari , telat 1 hari denda Rp 100.000')
                                print('===================================')
                                break

                            else :
                                print('Kode salah , coba lagi ')
                        

                    elif pilih == 2 :
                        print('\nProses Pembayaran ---- \n')
                        bio()
                        print('Pinjaman \t: Rp ',nominalpinjam[1])
                        print('Tagihan \t: Rp ',hasil)
                        denda = int(input('\nJarak peminjaman dengan pembayaran (hari) : '))
                        if denda > 120 :
                            hari = denda - 120
                            BayarDenda = hari * 100000
                            totalTghn = hasil + BayarDenda
                            print('Anda terlambat ', hari , 'hari')
                            print('Maka total tagihan yang harus anda bayar = Rp ', totalTghn)
                            pay = int(input('\nMasukkan uang anda : Rp '))
                            if pay > totalTghn :
                                kembalian = pay - totalTghn
                                print('\n\nUang anda : Rp ', pay)
                                print('Kembalian : Rp ', kembalian)
                                struk = str(input('\nApakah anda ingin mencetak struk (Y/N) ? : '))
                                if struk.capitalize() == 'Y':
                                    print('\n******************* STRUK PEMBAYARAN *******************')
                                    bio()
                                    print('\nJumlah tagihan = Rp ',hasil)
                                    print('Nominal Uang Customer = Rp ',pay)
                                    print('Uang kembalian = Rp ',kembalian)
                                    print('\n********************** THANK YOU ***********************')
                                break
                            if pay < totalTghn :
                                kurang = totalTghn - pay
                                print('Uang anda kurang ---')
                                print('Uang anda kurang Rp ',kurang)
                                break
                            if pay == totalTghn :
                                print('Uang anda pas')
                                print('\n******************* STRUK PEMBAYARAN *******************')
                                bio()
                                print('\nJumlah tagihan = Rp ',hasil)
                                print('Nominal Uang Customer = Rp ',pay)
                                print('Uang kembalian = Rp ',kembalian)
                                print('\n********************** THANK YOU ***********************')
                                break
                            else :
                                print('Thank you')

                            break

                        else : 
                            print('Anda Bebas dari Denda ---- ')
                            pay = int(input('\nMasukkan uang anda : Rp '))
                            if pay > hasil :
                                kembalian = pay - hasil
                                print('\n\nUang anda : Rp ', pay)
                                print('Kembalian : Rp ', kembalian)
                                struk = str(input('\nApakah anda ingin mencetak struk (Y/N) ? : '))
                                if struk.capitalize() == 'Y':
                                    print('\n******************* STRUK PEMBAYARAN *******************')
                                    bio()
                                    print('\nJumlah tagihan = Rp ',hasil)
                                    print('Nominal Uang Customer = Rp ',pay)
                                    print('Uang kembalian = Rp ',kembalian)
                                    print('\n********************** THANK YOU ***********************')
                                    break
                                else :
                                    print('-----\n')
                                    break

                            if pay < hasil :
                                kurang = hasil - pay
                                print('Uang anda kurang ---')
                                print('Uang anda kurang ',kurang)
                                break
                            if pay == hasil :
                                kembali = pay - hasil
                                print('Uang anda pas -')
                                print('\n******************* STRUK PEMBAYARAN *******************')
                                bio()
                                print('\nJumlah tagihan = Rp ',hasil)
                                print('Nominal Uang Customer = Rp ',pay)
                                print('Uang kembalian = Rp ', kembali)
                                print('\n********************** THANK YOU ***********************')
                                break

                    elif pilih == 3 :
                        print('\nPenghapusan data --- \n')
                        hapus = str(input('\nApakah anda ingin menghapus data (Y/N) ? : '))
                        if hapus.capitalize() == 'Y' :
                            nomor = int(input('\nmasukkan nik anda : '))
                            a = nik[1]
                            if nomor == a : 
                                bio()
                                print('=================================\n')
                                konfirm = str(input('Konfirmasi hapus data(Y/N) : '))
                                if konfirm.capitalize() == 'Y' :
                                    del nama[1]
                                    del nik[1]
                                    del alamat[1]
                                    print('Data telah dihapus')

                                    cek = str(input('Apakah ingin cek data ? : '))
                                    if cek.capitalize() == 'Y':
                                        print('nama \t\t: ',nama)
                                        print('nik \t\t: ',nik)
                                        print('alamat \t\t: ',alamat)
                                        print('data telah dihapus --- ')
                                        exit('\nProgram terhenti ,  -- ')
                                        
                                    else :
                                        print('Thankyou -- ')
                                        exit('\nProgram terhenti ,  -- ')
                                else :
                                    print('Hapus data dibatalkan -- \n')
                                    break
                            else :
                                print('NIK salah ,..')
                                break
                        else :
                            print('\nData anda tidak dihapus --')
                            break

                    elif pilih == 4 :
                        print('\nKeluar dari program ')
                        print('Thank you -- ')
                        print('Ketik n untuk logout\n')
                        break

                    else :
                        print('Pilihan tidak terdeteksi , coba lagi ... ')

                menu = str(input('\nKembali ke menu (Y/N) ? : '))
                                   
        elif pilih == 2 :
            exit('Program telah selesai ')

        else :
            print('Pilihan tidak ditemukan , coba lagi...')