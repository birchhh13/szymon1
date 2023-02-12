import random
import time
import tkinter
from tkinter import *
from tkinter.ttk import *
import os

kamien = 0
kamienIloscA = random.randint(3, 7)
kamienIloscB = random.randint(1, 3)
Rzelazo = 0
SZTzelazo = 0
SZTzloto = 0
Rzloto = 0
szafir = 0
rubin = 0
szmaragd = 0
diament = 0
kilofIloscK = 1
kilofIloscZ = 0
kilofIloscD = 0
KKw = 30
KZw = 0
KDw = 0
Km = "kamienny"
kamienrek = 0
zelazorek = 0
monety = 0
czyPiec = 0


def Kilof():
  global KKw
  global KZw
  global KDw
  global Km
  if (KKw >= 1 and Km == "kamienny"):
    KKw -= 1
    # time.sleep(1)
    # print("kopiesz surowce.")
    # time.sleep(1)
    # print("kopiesz surowce..")
    # time.sleep(1)
    # print("kopiesz surowce...")
    # os.system('clear')
    kopanieK()

  elif (KZw >= 1 and Km == "zelazny"):
    KZw -= 1
    #time.sleep(1)
    #print("kopiesz surowce.")
    #time.sleep(1)
    #print("kopiesz surowce..")
    #os.system('clear')
    kopanieZ()
  elif (KDw >= 1 and Km == "diamentowy"):
    KDw -= 1
    #time.sleep(1)
    #print("kopiesz surowce
    kopanieD()
  else:
    print("Nie masz żadnych kilofów")


def kopanieD():
  os.system('clear')
  surowiecSzansa = random.randint(1, 100)
  global kamien
  global Rzelazo
  global Rzloto
  global szafir
  global rubin
  global szmaragd
  global diament
  global kilofIlosc
  global kamienIloscA
  global kamienIloscB
  global Km
  if surowiecSzansa >= 33 and surowiecSzansa <= 62:
    zelazoIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscD
    Rzelazo += zelazoIlosc * kilofIloscD
    print("wykopałeś :", zelazoIlosc * kilofIloscD,
          " rud(ę,y) żelaza!\n wykopałeś : ", kamienIloscB * kilofIloscD,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 63 and surowiecSzansa <= 77:
    zlotoIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscD
    Rzloto += zlotoIlosc * kilofIloscD
    print("wykopałeś :", zlotoIlosc * kilofIloscD,
          " rud(ę,y) złota!\n wykopałeś : ", kamienIloscB * kilofIloscD,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 78 and surowiecSzansa <= 84:
    szafirIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscD
    szafir += szafirIlosc * kilofIloscD
    print("wykopałeś :", szafirIlosc * kilofIloscD,
          " szafir(y,ów)!\n wykopałeś : ", kamienIloscB * kilofIloscD,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 85 and surowiecSzansa <= 91:
    rubinIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIlosc
    rubin += rubinIlosc * kilofIloscD
    print("wykopałeś :", rubinIlosc * kilofIloscD,
          " Rubin(y,ów)!\n wykopałeś : ", kamienIloscB * kilofIloscD,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 92 and surowiecSzansa <= 96:
    szmaragdIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscD
    szmaragd += szmaragdIlosc * kilofIloscD
    print("wykopałeś :", szmaragdIlosc * kilofIloscD,
          " Szmaragd(y,ów)!\n wykopałeś : ", kamienIloscB * kilofIloscD,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 97 and surowiecSzansa <= 100:
    diamentIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscD
    diament += diamentIlosc * kilofIloscD
    print("wykopałeś :", diamentIlosc * kilofIloscD,
          " Diament(y,ów)!\n wykopałeś : ", kamienIloscB * kilofIloscD,
          " kamie(ń,nie,ni)")
  else:
    kamien += kamienIloscA * kilofIloscD
    print("wykopałeś :", kamienIloscA * kilofIloscD, " kamie(ń,nie,ni)")
  odswiez()


def kopanieZ():
  os.system('clear')
  surowiecSzansa = random.randint(1, 100)
  global kamien
  global Rzelazo
  global Rzloto
  global szafir
  global rubin
  global szmaragd
  global diament
  global kilofIlosc
  global kamienIloscA
  global kamienIloscB
  global Km
  if surowiecSzansa >= 40 and surowiecSzansa <= 69:
    zelazoIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscZ
    Rzelazo += zelazoIlosc * kilofIloscZ
    print("wykopałeś :", zelazoIlosc * kilofIloscZ,
          " rud(ę,y) żelaza!\n wykopałeś : ", kamienIloscB * kilofIloscZ,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 70 and surowiecSzansa <= 85:
    zlotoIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscZ
    Rzloto += zlotoIlosc * kilofIloscZ
    print("wykopałeś :", zlotoIlosc * kilofIloscZ,
          " rud(ę,y) złota!\n wykopałeś : ", kamienIloscB * kilofIloscZ,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 86 and surowiecSzansa <= 90:
    szafirIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscZ
    szafir += szafirIlosc * kilofIloscZ
    print("wykopałeś :", szafirIlosc * kilofIloscZ,
          " szafir(y,ów)!\n wykopałeś : ", kamienIloscB * kilofIloscZ,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 91 and surowiecSzansa <= 95:
    rubinIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscZ
    rubin += rubinIlosc * kilofIloscZ
    print("wykopałeś :", rubinIlosc * kilofIloscZ,
          " Rubin(y,ów)!\n wykopałeś : ", kamienIloscB * kilofIloscZ,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 96 and surowiecSzansa <= 98:
    szmaragdIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscZ
    szmaragd += szmaragdIlosc * kilofIloscZ
    print("wykopałeś :", szmaragdIlosc * kilofIloscZ,
          " Szmaragd(y,ów)!\n wykopałeś : ", kamienIloscB * kilofIloscZ,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 99 and surowiecSzansa <= 100:
    diamentIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscZ
    diament += diamentIlosc * kilofIloscZ
    print("wykopałeś :", diamentIlosc * kilofIloscZ,
          " Diament(y,ów)!\n wykopałeś : ", kamienIloscB * kilofIloscZ,
          " kamie(ń,nie,ni)")
  else:
    kamien += kamienIloscA * kilofIloscZ
    print("wykopałeś :", kamienIloscA * kilofIloscZ, " kamie(ń,nie,ni)")
  odswiez()


def kopanieK():
  os.system('clear')
  surowiecSzansa = random.randint(1, 100)
  global kamien
  global Rzelazo
  global Rzloto
  global kilofIlosc
  global kamienIloscA
  global kamienIloscB
  global Km
  if surowiecSzansa >= 50 and surowiecSzansa <= 84:
    zelazoIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscK
    Rzelazo += zelazoIlosc * kilofIloscK
    print("wykopałeś :", zelazoIlosc * kilofIloscK,
          " rud(ę,y) żelaza!\n wykopałeś : ", kamienIloscB * kilofIloscK,
          " kamie(ń,nie,ni)")

  elif surowiecSzansa >= 85 and surowiecSzansa <= 100:
    zlotoIlosc = random.randint(1, 3)
    kamien += kamienIloscB * kilofIloscK
    Rzloto += zlotoIlosc * kilofIloscK
    print("wykopałeś :", zlotoIlosc * kilofIloscK,
          " rud(ę,y) złota!\n wykopałeś : ", kamienIloscB * kilofIloscK,
          " kamie(ń,nie,ni)")
  else:
    kamien += kamienIloscA * kilofIloscK
    print("wykopałeś :", kamienIloscA * kilofIloscK, " kamie(ń,nie,ni)")

  odswiez()


def crafting():
  CraftingWindow = Toplevel()
  CraftingWindow.title("Wytwarzanie")
  CraftingWindow.geometry("270x180")
  Label(CraftingWindow, text="Wytwarzanie").pack()
  kamienny_kilof = tkinter.Button(CraftingWindow,
                                  text="Kamienny kilof",
                                  command=tworzKilofK)
  kamienny_kilof.place(x=5, y=30)
  zelazny_kilof = tkinter.Button(CraftingWindow,
                                 text="Zelazny kilof",
                                 command=tworzKilofZ)
  zelazny_kilof.place(x=5, y=60)
  diamentowy_kilof = tkinter.Button(CraftingWindow,
                                    text="Diamentowy kilof",
                                    command=tworzKilofD)
  diamentowy_kilof.place(x=5, y=90)
  moneta = tkinter.Button(CraftingWindow, text="10 monet")
  moneta.place(x=5, y=120)
  kamiennar = tkinter.Button(CraftingWindow, text="Kamienna rękojeść")
  kamiennar.place(x=140, y=30)
  zelaznar = tkinter.Button(CraftingWindow, text="Żelazna rękojeść")
  zelaznar.place(x=140, y=60)


def tworzKilofK():
  os.system('clear')
  global kamien
  global kilofIloscK
  global KKw
  global Km
  if (kamien >= 30):
    print("Stowrzyłeś Kamienny Kilof! Masz teraz ", kilofIloscK,
          " kamienych kilofów w ekwipunku.")
    kilofIloscK += 1
    KKw += 30
    kamien -= 30
    Km = "kamienny"
  else:
    print(
      "nie masz wystarczającej ilości surowców by storzyć ten przedmiot(30 kamieni)"
    )
  odswiez()


def tworzKilofZ():
  os.system('clear')
  global SZTzelazo
  global kilofIloscZ
  global KZw
  global kamienrek
  global Km
  if (SZTzelazo >= 30 and kamienrek >= 1):
    print("Stowrzyłeś Zelazny Kilof! Masz teraz ", kilofIloscZ,
          " Żelaznych kilofów w ekwipunku.")
    kilofIloscZ += 1
    KZw += 70
    kamienrek -= 1
    SZTzelazo -= 30
    Km = "zelazny"
  else:
    print(
      "nie masz wystarczającej ilości surowców by storzyć ten przedmiot(30 Sztabek żelaza i kamienna rękojeść)"
    )
  odswiez()


def tworzKilofD():
  os.system('clear')
  global diament
  global zelazorek
  global kilofIloscD
  global KDw
  global Km
  if (diament >= 30 and zelazorek >= 1):
    print("Stowrzyłeś Diamentowy Kilof! Masz teraz ", kilofIloscD,
          " Diamentowych kilofów w ekwipunku.")
    kilofIloscD += 1
    KDw += 150
    zelazorek -= 1
    diament -= 30
    Km = "diamentowy"
  else:
    print(
      "nie masz wystarczającej ilości surowców by storzyć ten przedmiot(30 Diamentów i żelazna rękojeść)"
    )
  odswiez()


def sklep():
  newWindow2 = Toplevel()
  newWindow2.title("Sklep")
  newWindow2.geometry('270x180')
  Label(newWindow2, text="Sklep").pack()
  piec_craft = tkinter.Button(newWindow2, text="Piec", command=piecKup)
  piec_craft.place(x=5, y=60)
  talizman = tkinter.Button(newWindow2, text="Talizman", command=talizKup)
  talizman.place(x=5, y=90)
  Niewolnik = tkinter.Button(newWindow2, text="Niewolnik")
  Niewolnik.place(x=5, y=120)


def talizKup():
  global SZTzloto
  global szafir
  global rubin
  os.system('clear')
  if (SZTzloto >= 100 and szafir >= 25 and rubin >= 25):
    print("Stworzyłeś Starożytny Talizman !")
    zloto -= 100
    szafir -= 25
    rubin -= 25
  else:
    print(
      "nie masz wystarczającej ilości surowców by stworzyć ten przedmiot(100 Sztabek złota, 25 rubinów, 25 szafirów)"
    )
  odswiez()


def piecKup():
  global czyPiec
  global kamien
  if (czyPiec == 0 and kamien >= 1):
    kamien -= 1
    piec = tkinter.Button(jaskinia, text="Piec", command=przepalanie)
    czyPiec += 1
    piec.place(x=450, y=190)
  elif (czyPiec > 0):
    print("posiadasz już jeden piec.")
  else:
    print("nie masz wystarczającej ilości kamienia!(175 kamieni)")
  odswiez()


def idk():
  pb1['value'] += 20


def przetzel():
  global Rzelazo
  global SZTzelazo
  if (Rzelazo >= 10):
    Rzelazo -= 10
    SZTzelazo += 10
  else:
    print("Brak wystarczającej liczby Rudy Żelaza (10 rud)")

  ekwipOdswiez()


def przepalanie():
  newWindow3 = Toplevel()
  newWindow3.title("Piec")
  newWindow3.geometry('270x180')
  Label(newWindow3, text="Piec").pack()
  przetop_z = tkinter.Button(newWindow3,
                             text="Przetop żelazo",
                             command=przetzel)
  przetop_z.place(x=5, y=60)
  pb1 = Progressbar(newWindow3,
                    orient='horizontal',
                    length=100,
                    mode='determinate')
  pb1.place(x=150, y=70)
  przetop_zł = tkinter.Button(newWindow3, text="Przetop złoto  ")
  przetop_zł.place(x=5, y=90)
  
def ekwip():
  global zelazorek
  global kamienrek
  global lista2
  global monety
  global SZTzelazo
  global SZTzloto
  EkwipWindow = tkinter.Tk()
  EkwipWindow.title("Ekwipunek")
  EkwipWindow.geometry('270x180')
  Label(EkwipWindow, text="Ekwipunek").pack()
  lista2 = tkinter.Label(EkwipWindow,
                         text='Kamienna Rękojeść: ' + str(kamienrek) +
                         '\n Zelazna Rękojeść: ' + str(zelazorek) +
                         "\n Sztabki żelaza: " + str(SZTzelazo) +
                         "\n Sztabki złota: " + str(SZTzloto))
  lista2.pack(side=tkinter.LEFT)


jaskinia = tkinter.Tk()
jaskinia.geometry('600x300')
jaskinia.title("Ciemna Jaskinia")

craft = tkinter.Button(jaskinia, text="Wytwarzanie", command=crafting)
craft.place(x=450, y=130)

ekwipunek = tkinter.Button(jaskinia, text="Ekwipunek", command=ekwip)
ekwipunek.place(x=450, y=100)

sklep1 = tkinter.Button(jaskinia, text="Sklep", command=sklep)
sklep1.place(x=450, y=160)

etykieta = tkinter.Label(jaskinia, text='Ciemna Jaskinia')
etykieta.pack()

button1 = tkinter.Button(jaskinia, text="kop", command=Kilof)
button1.pack(side=tkinter.TOP)

ki = tkinter.Label(jaskinia, text="aktualny kilof: " + Km)
ki.pack(side=tkinter.BOTTOM)


def odswiez():
  global lista
  global kamien
  global Rzelazo
  global Rzloto
  global kamienrek
  global zelazorek
  global rubin
  global szafir
  global szmaragd
  global diament
  global kilofIlosc
  global kamienIloscA
  global kamienIloscB
  lista.destroy()
  lista = tkinter.Label(jaskinia,
                        text="Surowce\n" + str(kamien) + " Kamieni\n" +
                        str(Rzelazo) + " Rud żelaza\n" + str(Rzloto) +
                        " Rud zlota\n" + str(rubin) + " Rubinów\n" +
                        str(szafir) + " Szafirów\n" + str(szmaragd) +
                        " Szmaragdów\n" + str(diament) + " Diamentów\n")
  lista.pack(side=tkinter.LEFT)


def ekwipOdswiez():
  global SZTzelazo
  global SZTzloto
  global lista2
  global zelazorek
  global kamienorek
  global monety
  lista2.destroy()
  lista2 = tkinter.Label(EkwipWindow,text=
                         'Kamienna Rękojeść: ' + str(kamienrek) +
                         '\n Zelazna Rękojeść: ' + str(zelazorek) +
                         "\n Sztabki żelaza: " + str(SZTzelazo) +
                         "\n Sztabki złota" + str(SZTzloto))
  lista2.pack(side=tkinter.LEFT)



lista = tkinter.Label(
  jaskinia,
  text="Surowce\n" + str(kamien) + " Kamieni\n" + str(Rzelazo) +
  " Rud żelaza\n" + str(Rzloto) + " Rud zlota\n" + str(rubin) + " Rubinów\n" +
  str(szafir) + " Szafirów\n" + str(szmaragd) + " Szmaragdów\n" +
  str(diament) + " Diamentów\n")
lista.pack(side=tkinter.LEFT)
