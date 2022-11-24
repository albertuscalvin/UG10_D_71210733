def kalkulator():   
    cont = "m"
    while cont.lower() == "m":
        print("Select operation\n1.tambah\n2.kurang\n3.kali\n4.bagi")

        pilihan = input("masukkan pilihan(1/2/3/4/5/6):")

        satu = int(input("Enter first number: "))
        dua = int(input("Enter second number: "))
        

        if pilihan == '1':
            print(satu,"+",dua,"=", (satu + dua))

        elif pilihan == '2':
            print(satu,"-",dua,"=", (satu - dua))

        elif pilihan == '3':
            print(satu,"*",dua,"=", (satu * dua))

        elif pilihan == '4':
            print(satu,"/",dua,"=", (satu / dua))
        elif pilihan == '5':
            print(satu,"%",dua,"=", (satu % dua))
        elif pilihan == '6'
            print(satu,"**",dua,"=",(satu ** dua ))
        else:
            print("Invalid input")
        cont = input("press q to stop:")
        if cont == "q":
            break

star = input("tekan q untuk memulai = ")
if star == "q":
    kalkulator()