# Modul Matematika Dasar

def ganjil_genap(angka):
    if angka % 2 == 0:
        return f"{angka} adalah Bilangan GENAP"
    else:
        return f"{angka} adalah Bilangan GANJIL"

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        return "Tidak bisa dibagi 0!"
    return a / b
