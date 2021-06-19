import os
clear = lambda : os.system('cls')

ulang = "y"
while ulang=="y" or ulang=="Y":

    kode =[1,2,3,4,5]
    produk = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]

    inp = 1
    while inp < 5:
        clear()
        print ("=====================================================================")
        print("                         BENGKEL MOTOR UD ")
        print ("=====================================================================")
        print(" Kode :",kode[0],"|",produk[0],"     | Hrg : Rp",format(harga[0],',.2f'))
        print(" Kode :",kode[1],"|",produk[1],"  | Hrg : Rp",format(harga[1],',.2f'))
        print(" Kode :",kode[2],"|",produk[2],"| Hrg : Rp",format(harga[2],',.2f'))
        print(" Kode :",kode[3],"|",produk[3],"          | Hrg : Rp",format(harga[3],',.2f'))
        print(" Kode :",kode[4],"|",produk[4],"             | Hrg : Rp",format(harga[4],',.2f'))
        print ("=====================================================================")
        pil = int(input(" Masukkan Kode Barang (1-5) = "))
        inp = pil
        if inp <= 5 :
            idx = 0
            while idx >= 0 and idx < 5 :
                idx = idx + 1
                if idx == 0 :
                    pil = 1
                    break
                else:
                    idx = pil - 1
                    break 

            qty = input(" Masukkan Jumlah Barang     = ")
            print("=====================================================================")
            print("                         Detail Transaksi ")
            print("=====================================================================")
            print(" Kode Barang                = " + str(kode[idx]))
            print(" Nama Barang                = " + produk[idx])
            print(" Jumlah Barang              = " + str(qty) + " Pcs")
            print(" Harga Barang               = Rp " + format(harga[idx], ",.2f"))
            print("=====================================================================")

            fixqty = int(qty)
            fixharga = harga[idx]
            subtotal = fixqty * fixharga

            print(" SubTotal Barang            = Rp " + format(subtotal, ",.2f"))

            if subtotal >= 200000:
                diskon = 0.05
            else: 
                diskon = 0

            hitungdiskon = subtotal * diskon
            totaldiskon = subtotal - hitungdiskon

            if diskon > 0:
                print(" Diskon (5%)                = Rp " + format(hitungdiskon, ",.2f"))

            ppn = 0.01
            hitungppn = totaldiskon * ppn
            totalppn = totaldiskon + hitungppn

            print(" PPN (1%)                   = Rp " + format(hitungppn, ",.2f"))
            print("=====================================================================")
            print(" Total Bayar                = Rp " + format(totalppn, ",.2f"))
            print("=====================================================================")

            print("")
            ulang = input(' Buat Transaksi Baru? (y/t) : ')
            if ulang == 't' or ulang == 'T':
                break
        else:
            break
    
    
            
        