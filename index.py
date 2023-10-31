# Looping Algoritma
# total=0
# bagi=0
# a=int(input("Masukkan batas atas bilangan :"))
# for i in range(0,a,1):
#     if i%2==1:
#         print(i)
#         total=total+i
#         bagi=bagi+1
# print(f"Total : {total}")
# print(f" Jml data : {bagi}")
# print(f"Rata : {total/bagi}")

for i in range(10):
    bil=int(input(f"Masukkan Bilangan ke-{i+1} :"))
    if(i==0):
        besar=bil
        kecil=bil
    else:
        if (bil>besar):
            besar=bil
        if(bil<kecil):
            kecil=bil
print("Bilangan terbesar :", besar)
print("Bilangan terkecil :", kecil)