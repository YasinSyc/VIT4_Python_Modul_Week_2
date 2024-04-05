#Cevap_1: Öğrenci Notları İşleme
#Bir sözlük kullanarak 3 öğrencinin bilgilerini ve notlarını saklayın. 
#Her öğrencinin adı, soyadı ve notları(Vize, Final ve Sozlu notu) olsun.

# Boş bir sözlük oluştur
students={}

# 10 öğrenci için bilgileri kullanıcıdan al
for i in range(1, 11):
    print(f"\n{i}. öğrenci bilgilerini giriniz:")
    ad = input("Adi: ")
    soyad = input("Soyadi: ")
    vize = float(input("Vize notu: "))
    final = float(input("Final notu: "))
    sozlu = float(input("Sozlu notu: "))
    
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
print("\nSiralanmis öğrenci adlari:")
for ad, soyad in ogrenci_adlari:
    print(ad, soyad)

# Not ortalaması 70'in altında olan öğrencileri bir küme (set) içinde saklayın
not_70_alti_ogrenciler = {ogrenci["ad"] for ogrenci in students.values() if ogrenci["not_ortalamasi"] < 70}
print("\nNot ortalamasi 70'in altinda olan öğrenciler:", not_70_alti_ogrenciler)


#Cevap_2:

class MovieCollection:
    def __init__(self):
        self.movies = {}
        self.load_movies()

    def load_movies(self):
        try:
            with open('movies.txt', 'r') as f:
                for line in f:
                    name, director, release_year, genre = line.strip().split(',')
                    self.movies[name] = {'director': director, 'release_year': int(release_year), 'genre': genre}
        except FileNotFoundError:
            pass

    def save_movies(self):
        with open('movies.txt', 'w') as f:
            for name, details in self.movies.items():
                f.write(f"{name},{details['director']},{details['release_year']},{details['genre']}\n")

    def modify_movie(self, name, director, release_year, genre):
        self.movies[name] = {'director': director, 'release_year': release_year, 'genre': genre}
        self.save_movies()

    def delete_movie(self, name):
        if name in self.movies:
            del self.movies[name]
            self.save_movies()

    def list_all_movies(self):
        return self.movies.items()

def main():
    collection = MovieCollection()

    while True:
        print("\nMenu:")
        print("1. Add Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. View Collection")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name, director, release_year, genre = input("Name: "), input("Director: "), int(input("Year: ")), input("Genre: ")
            collection.modify_movie(name, director, release_year, genre)
            print("Added!")
        elif choice == '2':
            name = input("Name to edit: ")
            if name in collection.movies:
                director, release_year, genre = input("New director: "), int(input("New release year: ")), input("New genre: ")
                collection.modify_movie(name, director, release_year, genre)
                print("Edited!")
            else:
                print("Not found!")
        elif choice == '3':
            name = input("What to delete: ")
            if name in collection.movies:
                collection.delete_movie(name)
                print("Deleted!")
            else:
                print("Not found!")
        elif choice == '4':
            print("\nMovie Collection:")
            for name, details in collection.list_all_movies():
                print(f" Name: {name} | Director: {details['director']} | Release Year: {details['release_year']} | Genre: {details['genre']}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()




#Cevap_3:

customers={}

def customer_registration():
   c_name=input("Please enter your name and surname:")
   c_email=input("Please enter your e-mail address:")
   c_phone_number=input("Please enter your phone number:")
   c_info={
       "Name Surname":c_name,
       "Email":c_email,
       "Phone Number":c_phone_number
   }
   numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
   import random
   c_id= ''.join([random.choice(numbers) for i in range(4)])
   customers[c_id]=c_info
   print(customers)
   print("Customer is successfully registered")

def customer_info_update():
   id=input("Please enter the customer id: ")
   print(f"Existing information about customer with id number {id}:", customers.get(id))
   if id in customers:
       print("1. Name Surname")
       print("2. Email Address")
       print("3. Phone Number")
       print("Which customer information do you want to change?")
       which_info = input("Enter one of the numbers above: ")
       if which_info == "1":
           new_name = input("New Name Surname: ")
           customers[id]["Name Surname"] = new_name
       elif which_info == "2":
           new_mail = input("New Email: ")
           customers[id]["Email"] = new_mail
       elif which_info == "3":
           new_phone = input("New Phone Number: ")
           customers[id]["Phone Number"] = new_phone
       print(f"New information about customer with id number {id}:", customers.items(id))
       print(" Customer informations are successfully updated")

  
def customer_del():
   c_del=input("Please enter the customer id to delete: ")
   if c_del in customers:
       customers.pop(c_del)
       print(" Customer is successfully deleted")

def customer_info_list():
   if not customers:
       print("No customer information available.")
     
   else:
       print("All customers' informations:")
       for keys,values in customers.items():
           print("Customer ID:", keys)
           print("Other informations:", values)   

def main_menu():
   while True:
       print("\nMain Menu:")
       print("1. Register a new customer ")
       print("2. Update the information of a customer")
       print("3. Delete a customer")
       print("4. List the information of all customers")
       print("5. Exit")

       menu_choice = input("Enter one of the number above: ")

       if menu_choice == "1":
           customer_registration()
       elif menu_choice == "2":
           customer_info_update()
       elif menu_choice == "3":
           customer_del()
       elif menu_choice == "4":
           customer_info_list()
       elif menu_choice == "5":
           print("Exit program...")
           break       
main_menu()

