"""Nomor 1"""
alas = 30
tinggi = 4
luas_segi3 = 1/2 * (alas*tinggi)
print("Sebuah segitiga memiliki alas sebesar %s cm dan tinggi %s cm. Luasnya adalah %s cm \n"%(alas,tinggi,luas_segi3))

"""Nomor 2"""
import math
pi = round(math.pi,2)

def luas(pi,r):
    la = pi*r**2
    print("luas lingkaran dengan jari-jari %s cm adalah %s cm2 \n"%(r,la))

    
def keliling(pi,r):
    kel = 2*pi*r
    print("keliling lingkaran dengan jari-jari %s cm adalah %s cm \n"%(r,kel))

def main_menu():
    while True:
        print("1. keliling lingkaran \n2. luas lingkaran \n3. Keluar")
        menu = int(input("pilihan anda :"))
        if menu==1:
            r = int(input("masukkan nilai r :"))
            keliling(pi,r)
        elif menu==2:
            r = int(input("masukkan nilai r :"))
            luas(pi,r)
        else:
            print("Goodbye! \n")
            break

main_menu()


"""Nomor 3"""

while True:
    nama = input("masukkan nama:\t")
    print("Nama saya %s \n"%(nama))
    if nama == "python":
        print("Goodbye Python\n")
        break


"""Nomor 4"""

hari_pertama = {"keju","tepung","garam","gula","coklat"}
hari_kedua = {"garam","gula","coklat","kecap"}

print("a. hari pertama = %s \n   hari kedua = %s"%(hari_pertama,hari_kedua))
b = hari_kedua.add("keju") #menambahkan elemen/kata keju ke dalam set
print("b. hari kedua tambah keju =",hari_kedua)
c = hari_pertama and hari_kedua #mencari irisan diantara 2 set(himpunan)
print("c. barang yang sama =",c)
d = hari_pertama - hari_kedua #mencari selisih A-B
print("d. brg yg dibeli hari pertama tidak dibeli hari kedua =",d)
e = hari_pertama.discard("garam") #menghapus elemen didalam set
print("e. hari pertama hapus garam =",hari_pertama) #
f = hari_kedua - hari_pertama #mencari selisih B -A
print("f. brg yg dibeli hari kedua tdk dibeli hari pertama =",f)
g = hari_pertama ^ hari_kedua #mencari elemen yang berbeda
print("g. barang yang tidak sama =",g)
h = print("h. hari pertama =",hari_pertama)
i = print("i. hari kedua =",hari_kedua)