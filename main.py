from tkinter import *
class Kcal:
    def __init__(self,kcal:int):
        self.kcal = kcal
class Czego_jest_duzo:
    def __init__(self, wartosc_odzywcza:str):
        self.wartosc_odzywcza = wartosc_odzywcza
class Danie(Kcal):
    def __init__(self, nazwa,skladniki:list,kcal,czego_jest_duzo:str):
        Kcal.__init__(self,kcal)
        self.nazwa = nazwa
        self.skladniki = skladniki
        self.czego_jest_duzo = czego_jest_duzo
b = Czego_jest_duzo("Białko")
w = Czego_jest_duzo("Węglowodany")
c = Czego_jest_duzo("Cukier")
skladniki_jajecznica = ["Jajko","Masło","Boczek","Szczypiorek"]
skladniki_jajko_miekko = ["Jajko"]
skladniki_jajko_papryka = ["Jajko","Masło","Olej","Papryka"]
list = []
skladniki_szakszuka = ["Jajko","Pomidor","Rukola","Ser"]
skladniki_jajka_turecku = ["Jajko","Chilli", "Ocet", "Jogurt", "Czosnek","Chleb"]
skladniki_jajka_florenckie = ["Jajko","Ocet","Masło","Czosnek","Chleb"]
skladniki_jajko_kokilkach = ["Jajko","Jogurt","Masło","Czosnek","Cebula","Ser","Pomidor"]
składniki_salatka = ["Jajko","Rzodkiewka","Por","Szczypiorek","Jogurt"]
skladniki_szparagi = ["Jajko","Boczek","Szparagi","Masło","Czosnek"]
skladniki_pasta_jajeczna = ["Jajko","Majonez","Szczypiorek"]
skladniki_pasta_jajeczna_makrela = ["Jajko","Makrela","Szypiorek","Rzodkiewki","Majonez"]
skladniki_omlet = ["Jajko","Mleko","Masło","Szynka","Pomidor"]
dania_maslo = []
dania_papryka = []
dania_pomidor = []
dania_ser = []
dania_boczek = []
dania_jogurt = []
dania_czosnek = []
dania_chleb = []
dania_cebula = []
Jajko_na_miekko = Danie("Jajko na miękko", skladniki_jajko_miekko,155,b)
Jajecznica = Danie("Jajecznica",skladniki_jajecznica,480,b)
Jajko_sadzone_w_papryce = Danie("Jajko sadzone w papryce",skladniki_jajko_papryka,100,b)
Szakszuka = Danie("Szakszuka",skladniki_szakszuka,167,w)
Spis_Treści = Danie("Spis Treści", list,0,w)
Jajka_tureckie = Danie("Jajka po Turecku",skladniki_jajka_turecku,1424,w)
Jajka_florenckie = Danie("Jajka po Florencku",skladniki_jajka_florenckie,536,b)
Jajka_koklilkach = Danie("Jajka w kokilkach",skladniki_jajko_kokilkach,750,b)
salatka = Danie("Sałatka z rzodkiewki i jajka",składniki_salatka,485,b)
szparagi_jajko = Danie("Szparagi z boczkiem i jajkiem",skladniki_szparagi,754,b)
pasta_jajeczna = Danie("Pasta Jajeczna",skladniki_pasta_jajeczna,538,b)
pasta_jajeczna_makrela = Danie("Pasta Jajeczna z Makrelą",skladniki_pasta_jajeczna_makrela,490,b)
omlet = Danie("Omlet z szynką",skladniki_omlet,429,b)
list_dan = [Spis_Treści, Jajecznica, Jajko_na_miekko, Jajko_sadzone_w_papryce, Szakszuka, Jajka_tureckie, Jajka_florenckie,Jajka_koklilkach,salatka,szparagi_jajko,pasta_jajeczna,pasta_jajeczna_makrela,omlet]
dania_jajko = []
lista_skladniki = []
słownik = {}
wyszukiwarka = [dania_maslo,dania_papryka,dania_pomidor,dania_ser,dania_boczek,dania_jogurt,dania_czosnek,dania_chleb,dania_cebula]
for el in list_dan:
    for skladnik in el.skladniki:
        if skladnik == "Jajko":
            dania_jajko.append(str(list_dan.index(el)) + "." + el.nazwa + "\n")
        if skladnik == "Masło":
            dania_maslo.append(str(list_dan.index(el)) + "." + el.nazwa + "\n")
        if skladnik == "Papryka":
            dania_papryka.append(str(list_dan.index(el)) + "." + el.nazwa + "\n")
        if skladnik == "Pomidor":
            dania_pomidor.append(str(list_dan.index(el)) + "." + el.nazwa + "\n")   
        if skladnik == "Ser":
            dania_ser.append(str(list_dan.index(el)) + "." + el.nazwa + "\n") 
        if skladnik == "Boczek":
            dania_boczek.append(str(list_dan.index(el)) + "." + el.nazwa + "\n") 
        if skladnik == "Czosnek":
            dania_czosnek.append(str(list_dan.index(el)) + "." + el.nazwa + "\n")
        if skladnik == "Jogurt":
            dania_jogurt.append(str(list_dan.index(el)) + "." + el.nazwa + "\n")  
        if skladnik == "Chleb":
            dania_chleb.append(str(list_dan.index(el)) + "." + el.nazwa + "\n")  
        if skladnik == "Cebula":
            dania_cebula.append(str(list_dan.index(el)) + "." + el.nazwa + "\n")  
for el in list_dan:
    for skladnik in el.skladniki:
        if skladnik not in lista_skladniki:
            lista_skladniki.append(skladnik)
for el in list_dan:
    for skladnik in el.skladniki:
        if skladnik not in słownik:
            słownik[skladnik] = []
        słownik[skladnik].append(f"{list_dan.index(el)}.{el.nazwa}\n")
for i,el in enumerate(lista_skladniki):
    if i % 2 == 1:
        lista_skladniki[i] =" "+ el + ",\n"
    if i % 2 == 0:
        lista_skladniki[i] =el + ","
root = Tk()
root.title("Książka Kucharska - Moja")
window_width = 800
window_height = 900
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.config(background = "#ccc")
f1 = Frame(root)
f11 = Frame(f1)
for frame in (f1,f11):
   frame.config(background = "#ccc")
   frame.pack()
my_label = Label(f1, text="")
my_label1 = Label(f1, text="")
my_label2 = Label(f1, text="")
my_label3 = Label(f1, text="")
my_label4 = Label(f1, text="")
my_label5 = Label(f1, text="")
my_label6 = Label(f1, text="")
my_label7 = Label(f1, text="")
my_label8 = Label(f1, text="")
my_label.config(text="Spis Treści",background = "#ccc",fg = "black",font = ("comic sans ms", 40),padx=20,bg="#ccc",pady=0.01)
my_label.pack()
my_label1.config(text="(Jeśli chcesz przejść do jakiegoś z przepisów wpisz jego numer w konsoli np. jeśli chcesz wybrać jajecznice wpisz 1 i potwierdź klikając enter)\n (Możesz też wyszukać dania z danym składnikiem np. jeśli wpiszesz jajko wyskoczą ci przepisy z jajkiem)",background = "#ccc",fg = "black",font = ("comic sans ms", 7),padx=20,bg="#ccc",pady=0.01)
my_label1.pack()
my_label2.config(text="1.Jajecznica\n2.Jajko na Miękko\n3.Jajko sadzone w papryce\n4.Szakszuka\n5.Jajka po Turecku\n6.Jajka po Florencku\n7.Jajka w kokilkach\n8.Sałatka z rzodkiewki i jajka\n9.Szparagi z boczkiem i jajkiem\n10.Pasta jajeczna\n11.Pasta jajeczna z makrelą\n12.Ekspresowy omlet z szynką\n13.Lista Składników wszystkich dań",background = "#ccc",fg = "black",font = ("comic sans ms", 30),padx=20,pady=10)
my_label2.pack()
def entry(event):
    global my_label
    global my_label1
    global my_label2
    global my_label3
    global my_label4
    global my_label5
    global my_label6
    global my_label7
    global my_label8
    global list_dan
    strona = w.get()
    w.delete(0,END)
    try:
        strona = int(strona)
    except ValueError:
        wyszukiwarka = str(strona)
    if strona == 1:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01  
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nNa trzy jajka daj około 50 gramów boczku surowego wędzonego.\nBoczek umieść na suchej i zimnej patelni.\n Jeśli masz boczek w kawałku,\n to przed wyłożeniem na patelnię pokrój go w drobną kosteczkę.\nZacznij nagrzewać patelnię na średniej mocy palnika.\n W ciągu kilku minut tłuszcz z boczku zacznie się wytapiać,\n a boczek lekko się zarumieni.\n Gdy boczek będzie już ładnie podsmażony zdejmij go na chwilę z patelni na miseczkę,\n zaś na patelnię z tłuszczem po boczku dodaj płaską łyżkę masła.\n Zmniejsz moc palnika. Na patelnię wbij trzy średnie lub duże jajka.\n Dodaj też część siekanego szczypiorku.\n Zacznij mieszać jajecznicę przy pomocy drewnianej łyżki.\n Ponieważ ustawiona jest mała moc palnika, to jajka będą się ścinały bardzo powoli.\n Jajecznica przez kilka minut będzie nadal rzadka,\n jednak podczas ciągłego mieszania zacznie gęstnieć.\n  ",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 2:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nJajka przed włożeniem do garnka trzeba umyć,\n gdyż na ich skorupce mogą być bakterie salmonelli\nNajpierw zagotuj wodę z odrobiną soli i octu.\n Dzięki temu łatwiej będzie później obrać ugotowane jajka.\n Kiedy woda zacznie wrzeć, włóż jajka do rondelka przy pomocy łyżeczki.\nJajko na miękko powinno gotować się przez 3 do 4 minut,\nzależy to w dużej mierze od wielkości jajka.\n Jeśli wolisz, aby żółtko nie było całkowicie płynne,\n gotuj je przez 6 minut, będzie ugotowane na półmiękko.",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n" + "\n" + "\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n" + "\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
    if strona == 0:
        my_label.config(
            text="Spis Treści",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 40),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz przejść do jakiegoś z przepisów wpisz jego numer w konsoli np. jeśli chcesz wybrać jajecznice wpisz 1 i potwierdź klikając enter)\n (Możesz też wyszukać dania z danym składnikiem np. jeśli wpiszesz jajko wyskoczą ci przepisy z jajkiem)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="1.Jajecznica\n2.Jajko na Miękko\n3.Jajko sadzone w papryce\n4.Szakszuka\n5.Jajka po Turecku\n6.Jajka po Florencku\n7.Jajka w kokilkach\n8.Sałatka z rzodkiewki i jajka\n9.Szparagi z boczkiem i jajkiem\n10.Pasta jajeczna\n11.Pasta jajeczna z makrelą\n12.Ekspresowy omlet z szynką\n13.Lista Składników wszystkich dań",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label2.pack()
        my_label3.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label3.pack()
        my_label4.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label6.pack()
        my_label7.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label7.pack()
        my_label8.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label8.pack()
    if strona == 3:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nPrzygotuj trzy krążki z papryki, na trzy jajka smażone w papryce.\nJajka wyjmij wcześniej z lodówki a paprykę umyj i osusz.\nPaprykę przetnij w 1/4 i wytnij trzy krążki ze środkowej części,\n w której papryka jest najgrubsza.\nZ krążków usuń ewentualne pestki oraz białe,\n bardziej gąbczaste wewnętrzne fragmenty.\n Na nagrzaną patelnię wylej łyżeczkę delikatnej oliwy\nKrążki przewróć na drugą stronę.\n Po dwóch minutach do każdego kawałka papryki ostrożnie wbij jajko.\nw ciągu maksymalnie czterech minut białko jajka będzie idealnie ścięte.\n Przy pomocy szpatułki zdejmij gotowe jajka w papryce na talerz.  ",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n" + "\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n" + "\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 4:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nZacznij od posiekania cebuli oraz umycia i obrania pomidorów,\nmożesz je sparzyć i zdjąć skórkę lub obrać delikatnie nożykiem\nNa patelni rozgrzej oliwę lub olej rzepakowy i podsmaż cebulę.\nDodaj pokrojone pomidory oraz przyprawy.Całość duś na małym ogniu ok. 5 min. \nJeśli lubisz paprykę to pokrój ją na kawałki i duś razem z pomidorami.\nZrób w pomidorach na patelni trzy zagłębienia i wlej tam jajka.\nPokrój kilka pomidorków koktajlowych i dodaj do szakszuki.\nDodaj także kilka kostek sera.\nGdy jajka się zetną posyp całość szczypiorkiem, rukolą i bazylią.",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n"+"\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n"+ "\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 5:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nW garnku z grubym dnem należy rozpuścić masło i podgrzewać je do momentu,\n aż stanie się złoto-brązowe i zacznie przyjemnie pachnieć.\n Następnie należy dodać do niego suszone płatki chili.\n Następnie w oddzielnym garnku z wrzątkiem należy ugotować jajka w koszulce.\n Jajka należy gotować pojedynczo w wodzie z octem winnym na średnim ogniu.\n Gotowanie jednego jajka zajmuje około 2-3 minuty.\n Gotowe jajka w koszulce należy wyjąć przy pomocy łyżki cedzakowej\n i odłożyć delikatnie do miski.\n W mniejszym garnku należy połączyć jogurt grecki\n z posiekanym ząbkami czosnku i solą.\n Taki sos należy powoli podgrzewać, ale nie dopuścić do wrzenia.",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 6:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nDo wrzątku z octem i solą wrzuć kolejno rozbite jajka,\n mieszając łyżką wodę, aby wzburzyć ją i ułatwić jajku ścięcie białka z płynnym żółtkiem\n gotowe jajko wyjmij łyżką cedzakową i odsącz na ręczniku papierowym,\n na rozgrzanej patelni rozpuść masło, dodaj posiekany czosnek i liście szpinaku,\n smaż do utraty połowy objętości, chleb zarumień na patelni lub w tosterze,\n gdy będzie złoto-brązowy, połóż na talerzu,\n na chlebie ułóż szpinak, jajko w koszulce,\n gotowe jajka po florencku oprósz świeżo zmielonym czarnym pieprzem.",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n"+"\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n"+"\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 7:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nCebulę i czosnek obierz, posiekaj i obsmaż na rozgrzanej patelni,\n razem z suszonymi pomidorami,\n dodaj świeże liście szpinaku i smaż do zmniejszenia objętości,\n dopraw pieprzem i suszonym oregano; kokilki wysmaruj masłem,\n rozłóż w nich farsz ze szpinakiem, dodaj po łyżce śmietany lub jogurtu greckiego,\n umieść na wierzchu rozbite jajko, obok jajka połóż plastry mozzarelli,\n kokilki wstaw do żaroodpornego naczynia z wrzątkiem do połowy wysokości,\n piecz w 190°C przez 10 minut do ścięcia białka przy płynnym żółtku.\n",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n"+"\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 8:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nUgotowane i wystudzone jajka obierz i drobno posiekaj. Przełóż do miseczki.\n Rzodkiewkę umyj, odetnij końce i pokrój w plastry lub kostkę.\n Pora umyj, odetnij koniec i zielone liście,\n zdejmij także pierwsze, grubsze warstwy.\n Pokrój pora na plasterki i przełóż do garnka,\n zalej wrzącą wodą i odstaw na 5 minut. Odcedź pora i dodaj do sałatki.\n Dopraw całość szczypiorkiem, majonezem lub jogurtem,\n solą i pieprzem do smaku. Wymieszaj.",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n"+"\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n"+"\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 9:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nZacznij od nastawienia jajek do gotowania.\n Ugotuj je, jak wolisz, na miękko lub na twardo.\n Obierz i przekrój na pół. Umyj szparagi i oderwij ich zdrewniałe końcówki.\n Jeśli chcesz, by szparagi w daniu były bardzo miękkie,\n zagotuj wodę z łyżeczką soli i cukru i wrzuć szparagi do wrzątku na 2 min.\n Odcedź. Zwiń w boczek po 3 szparagi.\n Na patelni rozgrzej 2 łyżki masła klarowanego.\n Obsmażaj szparagi w boczku z obu stron, aż się zrumienią, ok. 5 min.\n Zdejmij szparagi z patelni,\n zmniejsz ogień i dodaj pozostałe 2 łyżki masła klarowanego,\n szczyptę soli, posiekaną pietruszką i posiekany czosnek.\n Smaż tylko chwilę, by czosnek się nie spalił.\n Takim sosem polej szparagi i jajka na talerzu.",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 10:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nUgotowane na twardo jajka obierz ze skorupek\n i dokładnie rozgnieć widelcem lub krajalnicą do jajek.\n W przypadku dużej ilości pasty jajecznej użyj praski do ziemniaków.\n Dodaj majonez i opcjonalnie musztardę.\n Wymieszaj do uzyskania jednolitej masy.\n Dopraw pastę świeżo zmielonym czarnym pieprzem i posiekanymi ziołami.\n Podawaj rozsmarowaną na świeżo upieczonym chlebie,\n kajzerce lub chrupiących grzankach.",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n"+"\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n"+"\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 11:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nJajka ugotuj na twardo,\n obierz i drobno posiekaj (możesz użyć krajalnicy do jajek).\n Makrelę odcedź z oleju i przełóż do miseczki.\n Szczypiorek umyj, osusz i posiekaj.\n Rzodkiewki umyj i pokrój w drobną kostkę.\n Wszystkie składniki wymieszaj w misce,\n dodaj majonez lub serek wiejski,\n dopraw solą i pieprzem.\n Całość dokładnie wymieszaj.",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n"+"\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n"+"\n"+"\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 12:
        my_label.config(
            text=str(strona) + "." + list_dan[strona].nazwa,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text="Składniki:\n" + (' '.join(list_dan[strona].skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 17),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label2.pack()
        my_label3.config(
            text="Przepis\nW miseczce roztrzep jajka z wodą lub mlekiem,\n dodaj szczyptę soli i odrobinę pieprzu.\n Umyj rukolę, roszponkę i pomidorki.\n Pokrój wędlinę na paseczki.\n Na patelni rozpuść masło,\n wlej jajka i smaż,\n aż masa się zetnie.\n Gdy masa się zetnie,\n przełóż omlet na drugą stronę.\n Najłatwiej to zrobić za pomocą dużej pokrywki przykryj patelnię,\n obróć do góry nogami, a następnie zsuń omlet z powrotem na patelnię.\n Smaż, aż masa się zetnie (około minutę).\n Na gotowy omlet połóż wędlinę, pomidorki, rukolę i roszponkę.\n Omlet złóż na pół i przełóż na talerz.",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 15),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label3.pack()
        my_label4.config(text="\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="\n",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(
            text="Jaki składnik odżywczy przeważa w tym daniu?",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label6.pack()
        my_label7.config(
            text=list_dan[strona].czego_jest_duzo.wartosc_odzywcza,
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label7.pack()
        my_label8.config(
            text="\t"+ "\t" + "\t" + "\t" + "\t" + "     " + str(list_dan[strona].kcal) + "kcal",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 20),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label8.pack()
    if strona == 13:
        my_label.config(
            text="Lista składników",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 40),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label.pack()
        my_label1.config(
            text="(Jeśli chcesz wrócic do Spisu Treści wpisz 0 w konsoli)",
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 7),
            padx=20,
            bg="#ccc",
            pady=0.01
        )
        my_label1.pack()
        my_label2.config(
            text=(''.join(lista_skladniki)),
            background = "#ccc",
            fg = "black",
            font = ("comic sans ms", 30),
            padx=20,
            bg="#ccc",
            pady=10
        )
        my_label2.pack()
        my_label3.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label3.pack()
        my_label4.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label4.pack()
        my_label5.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label5.pack()
        my_label6.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label6.pack()
        my_label7.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
        my_label7.pack()
        my_label8.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
        my_label8.pack()
    ####################################################
    for klucz in słownik:
        if wyszukiwarka.lower() == klucz.lower():
            my_label.config(
                text="Dania z " + klucz,
                background = "#ccc",
                fg = "black",
                font = ("comic sans ms", 40),
                padx=20,
                bg="#ccc",
                pady=0.01
            )
            my_label.pack()
            my_label1.config(
                text="(Jeśli chcesz przejść do jakiegoś z przepisów wpisz jego numer w konsoli np. jeśli chcesz wybrać jajecznice wpisz 1 i potwierdź klikając enter)\n(Możesz też wrócić do spisu treści wpisując 0 w konsoli)",
                background = "#ccc",
                fg = "black",
                font = ("comic sans ms", 7),
                padx=20,
                bg="#ccc",
                pady=0.01
            )
            my_label1.pack()
            my_label2.config(
                text=(''.join(słownik[klucz])),
                background = "#ccc",
                fg = "black",
                font = ("comic sans ms", 30),
                padx=20,
                bg="#ccc",
                pady=10
            )
            my_label2.pack()
            my_label3.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
            my_label3.pack()
            my_label4.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
            my_label4.pack()
            my_label5.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
            my_label5.pack()
            my_label6.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
            my_label6.pack()
            my_label7.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=0.01)
            my_label7.pack()
            my_label8.config(text="",background = "#ccc",fg = "black",font = ("comic sans ms", 20),padx=20,bg="#ccc",pady=10)
            my_label8.pack()
w = Entry(f11,
        bd=5)
w.grid(sticky='S')
w.bind('<Return>', entry)
root.mainloop()