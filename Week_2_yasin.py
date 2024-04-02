#Soru1: Öğrenci Notları İşleme

#Bir öğrenci notlarını işlemek için bir Python programı yazmanız gerekiyor. 
#Programın aşağıdaki işlevleri yerine getirmesi gerekiyor:
#Bir sözlük kullanarak 3 öğrencinin bilgilerini ve notlarını saklayın. 
#Her öğrencinin adı, soyadı ve notları(Vize, Final ve Sozlu notu) olsun.


# Boş bir sözlük oluştur
students = {}

# 3 öğrenci için bilgileri kullanıcıdan al
for i in range(1, 4):
    print(f"\n{i}. öğrenci bilgilerini girin:")
    ad = input("Adi: ")
    soyad = input("Soyadi: ")
    vize = float(input("Vize notu: "))
    final = float(input("Final notu: "))
    sozlu = float(input("Sözlü notu: "))
    
    # Öğrenci bilgilerini sözlüğe ekle
    students[f"ogrenci{i}"] = {"ad": ad, "soyad": soyad, 
                             "notlar": {"vize": vize, "final": final, "sozlu": sozlu} }

# Her bir öğrencinin bilgilerini yazdır
for ogrenci in students.values():
    print(f"\n{ogrenci['ad']} {ogrenci['soyad']} {ogrenci['notlar']['vize']}, {ogrenci['notlar']['final']}, {ogrenci['notlar']['sozlu']}")

# Her öğrencinin not ortalamasını hesaplayın ve sözlüğe ekleyin
for ogrenci in students.values():
    vize = ogrenci["notlar"]["vize"]
    final = ogrenci["notlar"]["final"]
    sozlu = ogrenci["notlar"]["sozlu"]
    not_ortalamasi = (vize + final + sozlu) / 3
    ogrenci["not_ortalamasi"] = not_ortalamasi

# En yüksek not ortalamasına sahip öğrenciyi bulun
en_yuksek_not_ortalamasi = max(ogrenci["not_ortalamasi"] for ogrenci in students.values())
en_iyi_ogrenci = [ogrenci for ogrenci in students.values() if ogrenci["not_ortalamasi"] == en_yuksek_not_ortalamasi][0]

print("\nEn yüksek not ortalamasina sahip öğrenci:", en_iyi_ogrenci["ad"], en_iyi_ogrenci["soyad"],"{:.2f}".format(en_iyi_ogrenci["not_ortalamasi"]))

# Her öğrencinin adını soyadından ayırarak ayrı bir tuple içinde saklayın ve bunları bir listeye ekleyin
ogrenci_adlari = [(ogrenci["ad"], ogrenci["soyad"]) for ogrenci in students.values()]

# Adları alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın
ogrenci_adlari.sort()
print("\nSiralanmiş öğrenci adlari:")
for ad, soyad in ogrenci_adlari:
    print(ad, soyad)

# Not ortalaması 70'in altında olan öğrencileri bir küme (set) içinde saklayın
not_70_alti_ogrenciler = {ogrenci["ad"] for ogrenci in students.values() if ogrenci["not_ortalamasi"] < 70}
print("\nNot ortalamasi 70'in altinda olan öğrenciler:", not_70_alti_ogrenciler)


###################################################################################################################


#Soru_2:
#Proje Açıklaması: Bu proje, kullanıcının kendi film koleksiyonunu yönetmesine yardımcı 
#olacak bir uygulama oluşturmayı amaçlar. Kullanıcılar filmleri ekleyebilir, düzenleyebilir, 
#silebilir ve koleksiyonlarını görüntüleyebilir.

#Kullanılan Veri Yapıları: Sözlükler (filmleri ve ilgili bilgileri saklamak için), 
#listeler (film koleksiyonunu görüntülemek için)


#İlk olarak, json kütüphanesini kullanarak verileri dosyaya yazmak ve 
#dosyadan okumak için gerekli işlevleri içe aktarıyoruz.
#JSON dosyaları, metin tabanlıdır ve genellikle .json uzantısına sahiptir. 
#JSON formatı, anahtar-değer çiftlerini (key-value pairs) kullanarak verileri organize eder. 
#Bu anahtar-değer çiftleri, sözlükler (dictionary) veya nesneler gibi düşünülebilir. 
#JSON dosyası içinde veri, anahtarlarla eşleştirilmiş değerlerin bir listesi şeklinde tanımlanır.

import json

#kullanıcıdan film bilgilerini alır ve bir sözlük olarak döndürür.
def film_ekle():
    ad = input("Film adi: ")
    yonetmen = input("Yönetmen adi: ")
    yil = input("Yayin yili: ")
    tur = input("Film türü: ")
    return {"ad": ad, "yonetmen": yonetmen, "yil": yil, "tur": tur}

#Kullanıcıya düzenlemek istediği bilgi sorulur, bu bilgiyi güncellenere sözlüğü günceller.
def film_duzenle(filmler, index):
    secim = input("Ne düzenlemek istiyorsunuz? (ad/yonetmen/yil/tur): ").lower()
    if secim in filmler[index]:
        yeni_veri = input(f"Yeni {secim} bilgisini girin: ")
        filmler[index][secim] = yeni_veri
        print("Film güncellendi.")
    else:
        print("Geçersiz seçim!")

#Sözlükten seçilen filmi siler.
def film_sil(filmler, index):
    del filmler[index]
    print("Film silindi.")

#fonksiyon, mevcut film koleksiyonunu ekrana yazdırır. Her bir film sözlüğünü gösterir.
def koleksiyonu_goruntule(filmler):
    for i, film in enumerate(filmler):
        print(f"{i + 1}. Film Adi: {film['ad']} - Yönetmen: {film['yonetmen']} - Yil: {film['yil']} - Tür: {film['tur']}")

#mevcut film koleksiyonunu bir JSON dosyasına kaydeder.
def veriyi_kaydet(filmler):
    with open("film_koleksiyonu.json", "w") as dosya:
        json.dump(filmler, dosya)

#program başlatıldığında mevcut film koleksiyonunu JSON dosyasından yükler.
def veriyi_yukle():
    try:
        with open("film_koleksiyonu.json", "r") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return []
    
#fonksiyon, programın ana kontrol akışını sağlar. 
#Kullanıcıya ana menüyü gösterir ve seçimlerine göre ilgili işlevi çağırır. 
#Programdan çıkana kadar döngü devam eder.
def ana_menu():
    filmler = veriyi_yukle()
    
    while True:
        print("\n-- Film Koleksiyonu Yöneticisi --")
        print("1. Film Ekle")
        print("2. Film Düzenle")
        print("3. Film Sil")
        print("4. Koleksiyonu Görüntüle")
        print("5. Çikis")

        secim = input("Lütfen bir seçenek seçin: ")

        if secim == "1":
            film = film_ekle()
            filmler.append(film)
            veriyi_kaydet(filmler)
            print("Film eklendi.")
        elif secim == "2":
            index = int(input("Düzenlemek istediğiniz film numarasi: ")) - 1
            if 0 <= index < len(filmler):
                film_duzenle(filmler, index)
                veriyi_kaydet(filmler)
            else:
                print("Geçersiz film numarasi!")
        elif secim == "3":
            index = int(input("Silmek istediğiniz film numarasi: ")) - 1
            if 0 <= index < len(filmler):
                film_sil(filmler, index)
                veriyi_kaydet(filmler)
            else:
                print("Geçersiz film numarasi!")
        elif secim == "4":
            koleksiyonu_goruntule(filmler)
        elif secim == "5":
            print("Programdan çikis...")
            break
        else:
            print("Geçersiz seçim!")

#blok, Python programının başlangıç noktasıdır. ana_menu() fonksiyonunu çağırarak programı başlatır.
if __name__ == "__main__":
    ana_menu()



#########################################################################################################
#Soru_3: Musteri Yonetim Sistemi
# Müşteri bilgilerini saklamak için bir sözlük yapısı kullanın.
# Her müşteri için bir benzersiz müşteri kimliği (ID) atayın ve müşteri bilgilerini bu kimlikle ilişkilendirin.

clients = {}

def yeni_musteri_ekle():
    while True:
        musteri_id = input("Müşteri ID'sini girin: ")
        if musteri_id in clients:
            print("Bu müşteri ID zaten mevcut, farkli bir ID girin.")
        else:
            break

    ad = input("Adi: ")
    soyad = input("Soyadi: ")
    email = input("E-posta adresi: ")
    telefon = input("Telefon numarasi: ")
    
    musteri = {"ad": ad, "soyad": soyad, "email": email, "telefon": telefon}
    clients[musteri_id] = musteri
    print("Yeni müşteri eklendi.")

def musteri_guncelle():
    musteri_id = input("Güncellemek istediğiniz müşteri ID'sini girin: ")
    if musteri_id in clients:
        print("Mevcut müşteri bilgileri:")
        print(clients[musteri_id])
        
        ad = input("Yeni adi girin: ")
        if ad:
            clients[musteri_id]["ad"] = ad
        
        soyad = input("Yeni soyadi girin: ")
        if soyad:
            clients[musteri_id]["soyad"] = soyad
        
        email = input("Yeni e-posta adresini girin: ")
        if email:
            clients[musteri_id]["email"] = email
        
        telefon = input("Yeni telefon numarasi girin: ")
        if telefon:
            clients[musteri_id]["telefon"] = telefon
        
        print("Müşteri bilgileri güncellendi.")
    else:
        print("Belirtilen müşteri ID'si bulunamadi.")

def musteri_sil():
    musteri_id = input("Silmek istediğiniz müşteri ID'sini girin: ")
    if musteri_id in clients:
        del clients[musteri_id]
        print("Müşteri silindi.")
    else:
        print("Belirtilen müşteri ID'si bulunamadi.")

def tum_musterileri_listele():
    if clients:
        for musteri_id, musteri in clients.items():
            print("\nMüşteri ID:", musteri_id)
            for bilgi, deger in musteri.items():
                print(f"{bilgi.capitalize()}: {deger}")
            print("---------------------")
    else:
        print("Mevcut müşteri bulunmamaktadir.")

def ana_menu():
    while True:
        print("\n-- Müşteri Yönetim Sistemi --")
        print("1. Yeni müşteri ekle")
        print("2. Müşteri bilgilerini güncelle")
        print("3. Müşteri sil")
        print("4. Tüm müşterileri listele")
        print("5. Cikis")
        
        secim = input("Lütfen bir seçenek seçin: ")
        
        if secim == "1":
            yeni_musteri_ekle()
        elif secim == "2":
            musteri_guncelle()
        elif secim == "3":
            musteri_sil()
        elif secim == "4":
            tum_musterileri_listele()
        elif secim == "5":
            print("Programdan cikiliyor..")
            break
        else:
            print("Geçersiz seçim!")

# Programı başlatan kod
if __name__ == "__main__":
    ana_menu()

# Student information stored in a dictionary
students = {
    "Ahmet Yilmaz": [85, 90, 78],
    "Mehmet Demir": [92, 88, 76],
    "Ayse Kaya": [85, 90, 95],
    "Yusuf Sert": [55, 85, 72],
    "Eymen Sahin": [62, 80, 75],
    "Omer Yildiz": [65, 91, 92],
    "Kerem Yildirim": [82, 87, 76],
    "Hamza Ozturk": [42, 55, 67],
    "Ahmet Aydin": [65, 68, 71],
    "Ali Ozdemir": [70, 80, 90]
}

#1 Calculating each student's GPA and adding it to the dictionary
for student, grades in students.items():
    gpa = sum(grades) / len(grades)
    students[student].append(round(gpa,2))

#2 Finding and printing the information of the student with the highest GPA
highest_gpa_student = max(students.items(), key=lambda x: x[1][-1])
print("Student with the highest GPA:")
print("Name:", highest_gpa_student[0])
print("Grades:", highest_gpa_student[1][:-1])  # Exclude GPA from grades
print("GPA:", highest_gpa_student[1][-1])

#3 Separating each student's name from their surname and storing them in a separate tuple and adding them to a list
names_surnames = [student.split() for student in students]

#4 Sorting the names in alphabetical order and printing the sorted list
names_surnames.sort()
print("\nNames sorted in alphabetical order:")
for name, surname in names_surnames:
    print(name, surname)

#5 Keeping and printing the students with a GPA below 70 in a set
gpa_below_70_students = {student for student, grades in students.items() if grades[-1] < 70}
print("\nStudents with a GPA below 70:")
for student in gpa_below_70_students:
    print(student)
    
# Movie library data structure (dictionary)
movie_library = {}

# Adding a movie
def add_movie():
    name = input("Movie name: ")
    director = input("Director: ")
    year = input("Release year: ")
    genre = input("Genre: ")
    movie_library[name] = {"Director": director, "Release Year": year, "Genre": genre}
    print(f"{name} added to the library.")

# Editing a movie
def edit_movie(name):
    if name in movie_library:
        print(f"Current details for {name}:")
        print(f"Director: {movie_library[name]['Director']}")
        print(f"Release Year: {movie_library[name]['Release Year']}")
        print(f"Genre: {movie_library[name]['Genre']}")
        option = input("What would you like to change? (Director/Release Year/Genre): ").capitalize()
        new_info = input(f"Enter new {option}: ")
        movie_library[name][option] = new_info
        print(f"{name} successfully updated.")
    else:
        print("Movie not found in the library.")

# Deleting a movie
def delete_movie(name):
    if name in movie_library:
        del movie_library[name]
        print(f"{name} deleted from the library.")
    else:
        print("Movie not found in the library.")

# Displaying collection
def display_collection():
    if movie_library:
        print("\nMovie Collection:")
        for movie, details in movie_library.items():
            print(f"{movie}:")
            for key, value in details.items():
                print(f"{key}: {value}")
            print()
    else:
        print("The movie library is empty.")

# Saving a movie
def save_data():
    with open("movie_library.txt", "w") as file:
        for movie, details in movie_library.items():
            file.write(f"{movie},{details['Director']},{details['Release Year']},{details['Genre']}\n")
    print("Movie library data saved.")

# Loading movie data
def load_data():
    try:
        with open("movie_library.txt", "r") as file:
            for line in file:
                movie, director, year, genre = line.strip().split(",")
                movie_library[movie] = {"Director": director, "Release Year": year, "Genre": genre}
        print("Movie library data loaded.")
    except FileNotFoundError:
        print("No existing movie library data found.")

# Main menu
def main():
    load_data()
    while True:
        print("\nMovie Library Management System")
        print("1. Add Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. Display Collection")
        print("5. Save Data")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_movie()
        elif choice == "2":
            name = input("Enter the name of the movie to edit: ")
            edit_movie(name)
        elif choice == "3":
            name = input("Enter the name of the movie to delete: ")
            delete_movie(name)
        elif choice == "4":
            display_collection()
        elif choice == "5":
            save_data()
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# Customer management system data structure (dictionary)
customer_database = {}

# Function to add a new customer
def add_customer():
    print("\nAdd New Customer")
    customer_id = input("Enter Customer ID: ")
    if customer_id in customer_database:
        print("Customer ID already exists. Please try again.")
        return
    name = input("Enter Name: ")
    surname = input("Enter Surname: ")
    email = input("Enter Email: ")
    phone_number = input("Enter Phone Number: ")
    customer_database[customer_id] = {"Name": name, "Surname": surname, "Email": email, "Phone Number": phone_number}
    print("Customer added successfully.")

# Function to update customer information
def update_customer():
    print("\nUpdate Customer Information")
    customer_id = input("Enter Customer ID to update: ")
    if customer_id not in customer_database:
        print("Customer ID not found.")
        return
    print("Current Information:")
    print("Name:", customer_database[customer_id]["Name"])
    print("Surname:", customer_database[customer_id]["Surname"])
    print("Email:", customer_database[customer_id]["Email"])
    print("Phone Number:", customer_database[customer_id]["Phone Number"])
    name = input("Enter New Name (Press Enter to keep the current value): ")
    surname = input("Enter New Surname (Press Enter to keep the current value): ")
    email = input("Enter New Email (Press Enter to keep the current value): ")
    phone_number = input("Enter New Phone Number (Press Enter to keep the current value): ")
    if name:
        customer_database[customer_id]["Name"] = name
    if surname:
        customer_database[customer_id]["Surname"] = surname
    if email:
        customer_database[customer_id]["Email"] = email
    if phone_number:
        customer_database[customer_id]["Phone Number"] = phone_number
    print("Customer information updated successfully.")

# Function to delete a customer
def delete_customer():
    print("\nDelete Customer")
    customer_id = input("Enter Customer ID to delete: ")
    if customer_id not in customer_database:
        print("Customer ID not found.")
        return
    del customer_database[customer_id]
    print("Customer deleted successfully.")

# Function to list all customers
def list_customers():
    print("\nList of Customers")
    if not customer_database:
        print("No customers found.")
        return
    for customer_id, customer_info in customer_database.items():
        print("Customer ID:", customer_id)
        for key, value in customer_info.items():
            print(f"{key}: {value}")
        print()

# Main function
def main():
    while True:
        print("\nCustomer Management System")
        print("1. Add New Customer")
        print("2. Update Customer Information")
        print("3. Delete Customer")
        print("4. List All Customers")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_customer()
        elif choice == "2":
            update_customer()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            list_customers()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
