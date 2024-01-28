"""
PROJECT TITLE: Library Management System
NAME: Ahmad Khaled Samim
GITHUB & EDX USERNAME: https://github.com/itkhld1 & itkhld
PLACE: Denizli/Turkey
VIDEO RECORD DATE: 26 JAN 2024
"""

import os

class Kitap:
    def __init__(self, kitapNo, isim, yazar, sayfaSayisi):
        self.kitapNo = kitapNo
        self.isim = isim
        self.yazar = yazar
        self.sayfaSayisi = sayfaSayisi

class Kullanici:
    def __init__(self, kullaniciNo, isim, soyisim, dogumTarihi):
        self.kullaniciNo = kullaniciNo
        self.isim = isim
        self.soyisim = soyisim
        self.dogumTarihi = dogumTarihi

class Odunc:
    def __init__(self, kullaniciNo, kitapNo, baslangicTarihi, bitisTarihi, oduncNo):
        self.kullaniciNo = kullaniciNo
        self.kitapNo = kitapNo
        self.baslangicTarihi = baslangicTarihi
        self.bitisTarihi = bitisTarihi
        self.oduncNo = oduncNo

def open_files():
    global kitap_dosyasi, kullanici_dosyasi, odunc_dosyasi
    kitap_dosyasi = open("kitaplar.txt", "a+")
    kullanici_dosyasi = open("kullanicilar.txt", "a+")
    odunc_dosyasi = open("odunc.txt", "a+")

    if kitap_dosyasi is None or kullanici_dosyasi is None or odunc_dosyasi is None:
        print("Error opening files.")
        exit(os.EX_OSERR)

def close_files():
    if kitap_dosyasi is not None:
        kitap_dosyasi.close()
    if kullanici_dosyasi is not None:
        kullanici_dosyasi.close()
    if odunc_dosyasi is not None:
        odunc_dosyasi.close()

def odunc_al():
    pass

def kitapOduncAlindiMi(kitapNo):
    pass

def main():
    global kitap_dosyasi, kullanici_dosyasi, odunc_dosyasi
    secim = -1
    open_files()

    print("\n                  【 𝑾 𝑬 𝑳 𝑪 𝑶 𝑴 𝑬  𝑻 𝑶  𝑳 𝑰 𝑩 𝑬 𝑹 𝑨 𝑹 𝒀 ! 】")
    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
    print("                             🂡 𝑴 𝑨 𝑰 𝑵  𝑴 𝑬 𝑵 𝑼 🂡")
    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n")

    while secim != 0:
        print("1. Book Transactions")
        print("2. User Transactions")
        print("3. Borrowing Procedures")
        print("0. Exit")
        secim = int(input("Make Your Selection: "))
        print("_______________________________")

        if secim == 1:
            print("\nBook Transactions")
            print("1. Add Book")
            print("2. List the Books")
            print("3. Update the Books")
            print("4. Delete Book")
            print("5. Search Book")
            print("0. Return to Main Menu")
            secim = int(input("Make Your Selection: "))
            print("_______________________________")

            if secim == 1:
                kitap_ekle()
            elif secim == 2:
                kitap_listele()
            elif secim == 3:
                kitap_guncelle()
            elif secim == 4:
                kitap_sil()
            elif secim == 5:
                kitap_ara()
            elif secim == 0:
                pass
            else:
                print("Invalid selection!\n")

        elif secim == 2:
            print("\nUser Transactions")
            print("1. Add User")
            print("2. List the Users")
            print("3. Update the Users")
            print("4. Delete User")
            print("5. Search User")
            print("0. Return to Main Menu")
            secim = int(input("Make Your Selection: "))
            print("_______________________________")

            if secim == 1:
                kullanici_ekle()
            elif secim == 2:
                kullanici_listele()
            elif secim == 3:
                kullanici_guncelle()
            elif secim == 4:
                kullanici_sil()
            elif secim == 5:
                kullanici_ara()
            elif secim == 0:
                pass
            else:
                print("Invalid selection!\n")

        elif secim == 3:
            print("\nBorrowing Procedures")
            print("1. Borrowing ")
            print("2. Bringing Back Book")
            print("3. Loan Listing")
            print("0. Return to Main Menu")
            secim = int(input("Make your Selection: "))
            print("_______________________________")

            if secim == 1:
                odunc_al()
            elif secim == 2:
                kitap_geri_getir()
            elif secim == 3:
                odunc_listele()
            elif secim == 0:
                pass
            else:
                print("Invalid selection!\n")

        elif secim == 0:
            print("\nPROGRAM CLOSED...\n\n")

        else:
            print("Invalid selection!\n")

    close_files()

def kitap_ekle():
    class Kitap:
        def __init__(self, kitapNo, isim, yazar, sayfaSayisi):
            self.kitapNo = kitapNo
            self.isim = isim
            self.yazar = yazar
            self.sayfaSayisi = sayfaSayisi

    # Create an instance of Kitap to store information about the new book
    yeniKitap = Kitap(0, "", "", 0)

    # Prompt the user to enter the name of the book and store it in yeniKitap.isim
    yeniKitap.isim = input("\nBook Name: ")

    # Prompt the user to enter the author of the book and store it in yeniKitap.yazar
    yeniKitap.yazar = input("Author: ")

    # Prompt the user to enter the number of pages in the book and store it in yeniKitap.sayfaSayisi
    yeniKitap.sayfaSayisi = int(input("Number of Pages: "))

    # Generate a unique book number using the hash of the book's name and author
    yeniKitap.kitapNo = hash(yeniKitap.isim + yeniKitap.yazar)

    # Write the information about the new book to the document (kitaplar.txt)
    with open("kitaplar.txt", "a") as kitapDosyasi:
        kitapDosyasi.write(f"{yeniKitap.kitapNo} {yeniKitap.isim} {yeniKitap.yazar} {yeniKitap.sayfaSayisi}\n")

    # Print a success message indicating that the book has been successfully added
    print("\nBook Successfully Added.\n")

def kitap_listele():
    # Read from the document and print on the screen
    with open("kitaplar.txt", "r") as kitapDosyasi:
        print("\nBooks: ")
        for line in kitapDosyasi:
            kitapNo, isim, yazar, sayfaSayisi = map(str, line.split())
            print(f"NO: {kitapNo},  NAME: {isim},  AUTHOR: {yazar},  NUMBER OF PAGES: {sayfaSayisi}")
        print("_______________________________\n")

def kitap_guncelle():
    # Declare variables
    arananKitapNo = 0  # To store the book number to be updated
    guncelKitap = None  # To store the updated book information
    bulundu = False  # Flag to indicate whether the book is found in the file

    # Prompt user to input the book number to be updated
    arananKitapNo = int(input("\nBook Number to be Updated: "))

    # Read the existing content from the file
    with open("kitaplar.txt", "r") as kitapDosyasi:
        lines = kitapDosyasi.readlines()

    # Loop through each record in the file until the end of the file is reached
    for i, line in enumerate(lines):
        kitapNo, isim, yazar, sayfaSayisi = map(str, line.split())
        kitapNo = int(kitapNo)

        # Check if the current book number matches the one to be updated
        if kitapNo == arananKitapNo:
            bulundu = True  # Set the flag to indicate the book is found

            # Prompt user to input new information for the book
            guncelKitap = Kitap(kitapNo, "", "", 0)
            guncelKitap.isim = input("\nNew Book Name: ")
            guncelKitap.yazar = input("New Author: ")
            guncelKitap.sayfaSayisi = int(input("New Number of Pages: "))

            # Update the existing content with the new information
            lines[i] = f"{guncelKitap.kitapNo} {guncelKitap.isim} {guncelKitap.yazar} {guncelKitap.sayfaSayisi}\n"

            # Print a success message and exit the loop
            print("\nThe book has been updated successfully.\n")
            break

    # Check if the book was not found in the file
    if not bulundu:
        print("The Book Not Found.\n")

    # Write the updated content back to the file
    with open("kitaplar.txt", "w") as kitapDosyasi:
        kitapDosyasi.writelines(lines)

def kitap_sil():
    # Declare variables
    silinecekKitapNo = 0  # To store the book number to be deleted
    bulundu = False  # Flag to indicate whether the book is found in the file

    # Prompt user to input the book number to be deleted
    silinecekKitapNo = int(input("\nBook Number to be Deleted: "))
    print("")

    # Read the existing content from the file
    with open("kitaplar.txt", "r") as kitapDosyasi:
        lines = kitapDosyasi.readlines()

    # Open a temporary file for writing
    with open("temp.txt", "w") as tempFile:
        # Loop through each record in the file until the end of the file is reached
        for line in lines:
            kitapNo, isim, yazar, sayfaSayisi = map(str, line.split())
            kitapNo = int(kitapNo)

            # Check if the current book number matches the one to be deleted
            if kitapNo == silinecekKitapNo:
                bulundu = True  # Set the flag to indicate the book is found

                # Check if the book is not currently borrowed
                if not kitapOduncAlindiMi(silinecekKitapNo):
                    # Skip the line effectively deleting it from the output
                    continue
                else:
                    # Print a message indicating the book cannot be deleted as it is currently borrowed
                    print("Deletion cannot be done because the book is currently on loan.\n")

            # Write the book information to the temporary file (if it's not the one to be deleted)
            tempFile.write(f"{kitapNo} {isim} {yazar} {sayfaSayisi}\n")

    # Check if the book was not found in the file
    if not bulundu:
        print("The Book Not Found.\n")

    # Remove the original file and rename the temporary file to the original file's name
    os.remove("kitaplar.txt")
    os.rename("temp.txt", "kitaplar.txt")

def kitap_odunc_alindi_mi(kitapNo):
    with open("odunc.txt", "r") as oduncDosyasi:
        for line in oduncDosyasi:
            kNo, bNo, baslangicTarihi, bitisTarihi = map(str, line.split())
            kNo, bNo = int(kNo), int(bNo)
            if bNo == kitapNo:
                return True  # Book is borrowed

    return False  # The book is not borrowed

def kitap_ara():
    # Declare variables
    aramaKelimesi = ""  # To store the search keyword
    bulundu = False  # Flag to indicate whether any book is found

    # Prompt user to input the search keyword
    aramaKelimesi = input("\nSearch Word: ")

    # Read the existing content from the file
    with open("kitaplar.txt", "r") as kitapDosyasi:
        # Loop through each record in the file until the end of the file is reached
        for line in kitapDosyasi:
            kitapNo, isim, yazar, sayfaSayisi = map(str, line.split())

            # Check if the search keyword is found in the book name
            if aramaKelimesi.lower() in isim.lower():
                bulundu = True  # Set the flag to indicate a book is found

                # Print information about the found book
                print(f"NO: {kitapNo},  NAME: {isim},  AUTHOR: {yazar},  NUMBER OF PAGES: {sayfaSayisi}")

    # Check if no book is found
    if not bulundu:
        print("The Book Not Found.\n")

# Function prototypes for getting user and book information, and checking if a book is borrowed
def kullanici_bilgisi_getir(kullaniciNo):
    # Function to get user information based on user number
    class Kullanici:
        def __init__(self, kullaniciNo, isim, soyisim, dogumTarihi):
            self.kullaniciNo = kullaniciNo
            self.isim = isim
            self.soyisim = soyisim
            self.dogumTarihi = dogumTarihi

    with open("kullanicilar.txt", "r") as kullaniciDosyasi:
        for line in kullaniciDosyasi:
            kNo, isim, soyisim, dogumTarihi = map(str, line.split())
            kNo = int(kNo)
            if kNo == kullaniciNo:
                return Kullanici(kNo, isim, soyisim, dogumTarihi)

    return None

def kitap_bilgisi_getir(kitapNo):
    # Function to get book information based on book number
    class Kitap:
        def __init__(self, kitapNo, isim, yazar, sayfaSayisi):
            self.kitapNo = kitapNo
            self.isim = isim
            self.yazar = yazar
            self.sayfaSayisi = sayfaSayisi

    with open("kitaplar.txt", "r") as kitapDosyasi:
        for line in kitapDosyasi:
            bNo, isim, yazar, sayfaSayisi = map(str, line.split())
            bNo = int(bNo)
            if bNo == kitapNo:
                return Kitap(bNo, isim, yazar, sayfaSayisi)

    return None

# Function to add a new user
def kullanici_ekle():
    # Declare a variable to store information about the new user
    class Kullanici:
        def __init__(self, kullaniciNo, isim, soyisim, dogumTarihi):
            self.kullaniciNo = kullaniciNo
            self.isim = isim
            self.soyisim = soyisim
            self.dogumTarihi = dogumTarihi

    # Create an instance of Kullanici to store information about the new user
    yeniKullanici = Kullanici(0, "", "", "")

    # Prompt the user to input the name
    yeniKullanici.isim = input("\nName: ")

    # Prompt the user to input the surname
    yeniKullanici.soyisim = input("Surname: ")

    # Prompt the user to input the birthdate (in DD.MM.YYYY format)
    yeniKullanici.dogumTarihi = input("Birth Date (DD.MM.YYYY): ")

    # Generate a unique user number (assuming hash produces a unique value)
    yeniKullanici.kullaniciNo = hash(yeniKullanici.isim + yeniKullanici.soyisim)

    # Write the user information to the document
    with open("kullanicilar.txt", "a") as kullaniciDosyasi:
        kullaniciDosyasi.write(f"{yeniKullanici.kullaniciNo} {yeniKullanici.isim} {yeniKullanici.soyisim} {yeniKullanici.dogumTarihi}\n")

    # Print a success message
    print("\nUser added successfully.\n")

# Function to list users
def kullanici_listele():
    class Kullanici:
        def __init__(self, kullaniciNo, isim, soyisim, dogumTarihi):
            self.kullaniciNo = kullaniciNo
            self.isim = isim
            self.soyisim = soyisim
            self.dogumTarihi = dogumTarihi

    with open("kullanicilar.txt", "r") as kullaniciDosyasi:
        print("\nUsers:\n")
        for line in kullaniciDosyasi:
            kNo, isim, soyisim, dogumTarihi = map(str, line.split())
            kNo = int(kNo)
            kullanici = Kullanici(kNo, isim, soyisim, dogumTarihi)
            print(f"NO: {kullanici.kullaniciNo},  NAME: {kullanici.isim},  SURNAME: {kullanici.soyisim},  BIRTH DATE: {kullanici.dogumTarihi}\n")

# Function to update user information
def kullanici_guncelle():
    class Kullanici:
        def __init__(self, kullaniciNo, isim, soyisim, dogumTarihi):
            self.kullaniciNo = kullaniciNo
            self.isim = isim
            self.soyisim = soyisim
            self.dogumTarihi = dogumTarihi

    # Get the user number to be updated
    arananKullaniciNo = int(input("\nUser Number to be Updated: "))

    with open("kullanicilar.txt", "r") as kullaniciDosyasi:
        lines = kullaniciDosyasi.readlines()

    # Loop through the lines and update the user information
    for i, line in enumerate(lines):
        kNo, isim, soyisim, dogumTarihi = map(str, line.split())
        kNo = int(kNo)

        if kNo == arananKullaniciNo:
            guncelKullanici = Kullanici(kNo, "", "", "")
            guncelKullanici.isim = input("\nNew Name: ")
            guncelKullanici.soyisim = input("New Surname: ")
            guncelKullanici.dogumTarihi = input("New Birth Date (DD.MM.YYYY): ")

            lines[i] = f"{guncelKullanici.kullaniciNo} {guncelKullanici.isim} {guncelKullanici.soyisim} {guncelKullanici.dogumTarihi}\n"

            with open("kullanicilar.txt", "w") as kullaniciDosyasi:
                kullaniciDosyasi.writelines(lines)

            print("\nThe user has been updated successfully.\n")
            break
    else:
        print("User not found.\n")

# Function to delete a user
def kullanici_sil():
    class Kullanici:
        def __init__(self, kullaniciNo, isim, soyisim, dogumTarihi):
            self.kullaniciNo = kullaniciNo
            self.isim = isim
            self.soyisim = soyisim
            self.dogumTarihi = dogumTarihi

    # Get the user number to be deleted
    silinecekKullaniciNo = int(input("\nUser Number to be deleted: "))

    with open("kullanicilar.txt", "r") as kullaniciDosyasi:
        lines = kullaniciDosyasi.readlines()

    # Open a temporary file for writing
    with open("temp_kullanici.txt", "w") as tempFile:
        # Loop through the lines and delete the specified user
        for line in lines:
            kNo, isim, soyisim, dogumTarihi = map(str, line.split())
            kNo = int(kNo)

            if kNo == silinecekKullaniciNo:
                if not kullanici_odunc_alindi_mi(silinecekKullaniciNo):
                    continue
                else:
                    print("Since the user is currently borrowing books, deletion cannot be done.\n")
                    break

            tempFile.write(f"{kNo} {isim} {soyisim} {dogumTarihi}\n")

        else:
            # Remove the original file and rename the temporary file
            os.remove("kullanicilar.txt")
            os.rename("temp_kullanici.txt", "kullanicilar.txt")

            print("\nThe user has been deleted successfully.\n")


# Function to check if a user has borrowed books
def kullanici_odunc_alindi_mi(kullaniciNo):
    class Odunc:
        def __init__(self, kullaniciNo, kitapNo, baslangicTarihi, bitisTarihi):
            self.kullaniciNo = kullaniciNo
            self.kitapNo = kitapNo
            self.baslangicTarihi = baslangicTarihi
            self.bitisTarihi = bitisTarihi

    with open("odunc.txt", "r") as oduncDosyasi:
        for line in oduncDosyasi:
            kNo, bNo, baslangicTarihi, bitisTarihi = map(str, line.split())
            kNo, bNo = int(kNo), int(bNo)

            if kNo == kullaniciNo:
                return True

    return False


# Function to search for a user based on a keyword in the name or surname
def kullanici_ara():
    class Kullanici:
        def __init__(self, kullaniciNo, isim, soyisim, dogumTarihi):
            self.kullaniciNo = kullaniciNo
            self.isim = isim
            self.soyisim = soyisim
            self.dogumTarihi = dogumTarihi

    # Get the search keyword
    aramaKelimesi = input("\nSearch Word: ")

    with open("kullanicilar.txt", "r") as kullaniciDosyasi:
        bulundu = False
        # Loop through the lines and search for the specified keyword in the name or surname
        for line in kullaniciDosyasi:
            kNo, isim, soyisim, dogumTarihi = map(str, line.split())

            if aramaKelimesi.lower() in isim.lower() or aramaKelimesi.lower() in soyisim.lower():
                bulundu = True
                print(f"NO: {kNo},  NAME: {isim},  SURNAME: {soyisim},  BIRTH DATE: {dogumTarihi}")

        if not bulundu:
            print("User Not Found.\n")


# Function to handle the return of a borrowed book
def kitap_geri_getir():
    class Odunc:
        def __init__(self, kullaniciNo, kitapNo, baslangicTarihi, bitisTarihi):
            self.kullaniciNo = kullaniciNo
            self.kitapNo = kitapNo
            self.baslangicTarihi = baslangicTarihi
            self.bitisTarihi = bitisTarihi

    # Get the user and book numbers for the return process
    getirenKullaniciNo = int(input("\nSubmitted User Number: "))
    getirilenKitapNo = int(input("Submitted Book Number: "))

    with open("odunc.txt", "r") as oduncDosyasi:
        lines = oduncDosyasi.readlines()

    # Open a temporary file for writing
    with open("temp_odunc.txt", "w") as tempFile:
        bulundu = False
        # Loop through the lines and search for the specified user and book numbers
        for line in lines:
            kNo, bNo, baslangicTarihi, bitisTarihi = map(str, line.split())
            kNo, bNo = int(kNo), int(bNo)

            # Check if the current record matches the specified user and book numbers
            if kNo == getirenKullaniciNo and bNo == getirilenKitapNo:
                bulundu = True
                # Prompt the user to enter the return date
                bitisTarihi = input("End Date (DD.MM.YYYY): ")
                tempFile.write(f"{kNo} {bNo} {baslangicTarihi} {bitisTarihi}\n")
                print("\nThe book was successfully retrieved.\n")
            else:
                tempFile.write(f"{kNo} {bNo} {baslangicTarihi} {bitisTarihi}\n")

    if not bulundu:
        # If the loan record is not found, print an error message
        print("No loan record found.\n")

    # Remove the original file and rename the temporary file
    os.remove("odunc.txt")
    os.rename("temp_odunc.txt", "odunc.txt")


# Function to list borrowed books
def odunc_listele():
    class Odunc:
        def __init__(self, kullaniciNo, kitapNo, baslangicTarihi, bitisTarihi):
            self.kullaniciNo = kullaniciNo
            self.kitapNo = kitapNo
            self.baslangicTarihi = baslangicTarihi
            self.bitisTarihi = bitisTarihi

    class Kitap:
        def __init__(self, kitapNo, isim, yazar, sayfaSayisi):
            self.kitapNo = kitapNo
            self.isim = isim
            self.yazar = yazar
            self.sayfaSayisi = sayfaSayisi

    class Kullanici:
        def __init__(self, kullaniciNo, isim, soyisim, dogumTarihi):
            self.kullaniciNo = kullaniciNo
            self.isim = isim
            self.soyisim = soyisim
            self.dogumTarihi = dogumTarihi

    with open("odunc.txt", "r") as oduncDosyasi:
        print("\nBorrowers and Books:\n\n")
        for line in oduncDosyasi:
            kNo, bNo, baslangicTarihi, bitisTarihi = map(str, line.split())
            kNo, bNo = int(kNo), int(bNo)

            kullanici = kullanici_bilgisi_getir(kNo)
            kitap = kitap_bilgisi_getir(bNo)

            print(f" USER: {kullanici.isim} {kullanici.soyisim},  BOOK: {kitap.isim},  START DATE: {baslangicTarihi},  END DATE: {bitisTarihi}")

# Function to retrieve user information based on user number
def kullanici_bilgisi_getir(kullaniciNo):
    class Kullanici:
        def __init__(self, kullaniciNo, isim, soyisim, dogumTarihi):
            self.kullaniciNo = kullaniciNo
            self.isim = isim
            self.soyisim = soyisim
            self.dogumTarihi = dogumTarihi

    with open("kullanicilar.txt", "r") as kullaniciDosyasi:
        for line in kullaniciDosyasi:
            kNo, isim, soyisim, dogumTarihi = map(str, line.split())
            kNo = int(kNo)
            if kNo == kullaniciNo:
                return Kullanici(kNo, isim, soyisim, dogumTarihi)

    return None

# Function to retrieve book information based on book number
def kitap_bilgisi_getir(kitapNo):
    class Kitap:
        def __init__(self, kitapNo, isim, yazar, sayfaSayisi):
            self.kitapNo = kitapNo
            self.isim = isim
            self.yazar = yazar
            self.sayfaSayisi = sayfaSayisi

    with open("kitaplar.txt", "r") as kitapDosyasi:
        for line in kitapDosyasi:
            bNo, isim, yazar, sayfaSayisi = map(str, line.split())
            bNo = int(bNo)
            if bNo == kitapNo:
                return Kitap(bNo, isim, yazar, sayfaSayisi)

    return None

if __name__ == '__main__':
    main()