print ("ketik 1 untuk menghitung penjumlahan")
print ("ketik 2 untuk menghitung pegurangan")
print ("ketik 3 untuk menghitung perkalian")
print ("ketik 4 untuk menghitung pembagian")
print ("ketik 5 untuk menghitung sisa hasil bagi")
print ("ketik 6 untuk menghitung pemangkatan")
e = int(input("masukan pilihan anda:"))
r = int(input("masukan bilangan pertama:"))
t = int(input("masukan bilangan kedua:"))
if e== 1 :
    jumlah = r+t
    print ("hasil dari",r,"dijumlahkan dengan",t,"adalah",jumlah)
elif e== 2 :
    jumlah = r-t
    print ("hasil dari",r,"dikurangi dengan",t,"adalah",jumlah)
elif e== 3 :
    jumlah = r*t
    print ("hasil dari",r,"dikali dengan",t,"adalah",jumlah)
elif e== 4 :
    jumlah = r/t
    print ("hasil dari",r,"dibagi dengan",t,"adalah",jumlah)
elif e== 5 :
    jumlah = r%t
    print ("hasil dari",r,"sisa bagi dengan",t,"adalah",jumlah)
elif e== 6 :
    jumlah = r**t
    print ("hasil dari",r,"dipangkatkan dengan",t,"adalah",jumlah)
else :
    print ("ramasokk")