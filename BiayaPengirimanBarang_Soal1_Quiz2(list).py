import os
clear = lambda : os.system('cls')

ulang = "y"
while ulang=="y" or ulang=="Y":

    kode =[1,2]
    kota = ['Surabaya','Bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]

    inp = 1
    while inp < 2:
        clear()
        print ("=====================================================================")
        print("                     TRANSKASI BIAYA EKSPEDISI ")
        print ("=====================================================================")
        print(" Kode :",kode[0],"| Kota :", kota[0], "| Jarak :",jarak[0]," Km | Ongkir : Rp",format(ongkirperkm[0],',.2f'))
        print(" Kode :",kode[1],"| Kota :", kota[1], " | Jarak :",jarak[1]," Km | Ongkir : Rp",format(ongkirperkm[1],',.2f'))
        print ("=====================================================================")
        pil = int(input("Masukkan Kode Tujuan (1-2) = "))
        inp = pil
        if inp <= 2 :
            idx = 0
            while idx >= 0 and idx < 2 :
                idx = idx + 1
                if idx == 0 :
                    pil = 1
                    break
                else:
                    idx = pil - 1
                    break 

            ongkir = jarak[idx] * ongkirperkm[idx]         
            print('=====================================================================')
            print('Kota         = ',kota[idx])
            print('Jarak        = ',jarak[idx],'Km')
            print('Ongkir PerKm =  Rp',format(ongkirperkm[idx],',.2f'))
            print('=====================================================================')
            print('Total Harga  =  Rp',format(ongkir,',.2f'))          
            print('=====================================================================')
            print("")
            ulang = input('Buat Transaksi Baru? (y/t) : ')
            if ulang == 't' or ulang == 'T':
                break
        else:
            break
    
    
            
        