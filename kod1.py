#zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu,
# a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
#Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci:
#Idę do <sklep> i kupuję tam <rzeczy>.
#Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów i towarów były wypisane wielką literą (sięgnij do oficjalnej dokumentacji, by odnaleźć taką funkcjonalność).
#Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.. X to sumaryczna liczba towarów, które są na listach.

#Stworzyć słownik z kilkoma wartościami
zakupy1={"warzywniak":["marchew","seler","rukola"]}
zakupy2={"piekarnia":["chleb","pączek","bułki"]}
print(zakupy1)
print(zakupy2)
print()
#Iteracja po słowniku
#Iteracja z pętlą po kluczu
for klucz in zakupy1.keys():
    print("Idę do", klucz.capitalize())

for value in zakupy1.values():
    print("kupuję tu", value)
#jak to ze sobą połączyć?

for klucz in zakupy2.keys():
    print("Idę do", klucz.capitalize())

for value in zakupy2.values():
    print("kupuję tu", value)

shopping_list = ["marchew", "seler", "rukola","chleb","pączek","bułki"]
print ("W sumie kupię ", len(shopping_list),"produktów")

