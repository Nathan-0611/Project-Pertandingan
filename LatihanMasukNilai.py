import os
import random
import string
data = dict()
while True:
    os.system("cls")
    print( f" {'DATA PERTANDINGAN BOLA BASKET' :_^35}" )
    KeyFinal = "".join(random.choice(string.ascii_uppercase)for i in range(3))
    NamaTim = input("Enter Nama Tim\t\t:")
    KelompokUmur = input("Enter Kelompok Umur\t\t:")
    AsalKota = input("Enter Asal Kota\t:")
    data[KeyFinal] = {'namatimkey' : NamaTim, 'kelompokumurkey' : KelompokUmur, 'asalkotakey' : AsalKota  }
    opsi = input("Ingin input data LAGI GAK (y/t) :").lower()
    if opsi =='t':
        break
print("-"*60)
print(f"Key\t Nama Tim\t Kelompok Umur\t Asal Kota")
print("-"*60)
for key, value in data.items():
    print(f"{key}.\t{data[key]['namatimkey']}\t {data[key]['kelompokumurkey']}\t \t{data[key]['asalkotakey']}")
